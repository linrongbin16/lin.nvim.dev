#!/usr/bin/env python3

import datetime
import logging
import sys
from typing import Iterable, Optional, Union

from selenium.webdriver import Chrome, ChromeOptions, DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

STARS = 400
LASTCOMMIT = 2 * 365 * 24 * 3600  # 2 years * 365 days * 24 hours * 3600 seconds
INDENT_SIZE = 4
INDENT = " " * INDENT_SIZE
HEADLESS = False

LUA_FILE = "colors-list.lua"
VIM_FILE = "colors-list.vim"


def parse_numbers(s: str) -> int:
    def impl(s1: str) -> int:
        s1 = s1.lower()
        suffix_map = {"k": 1000, "m": 1000000, "b": 1000000000}
        if s1[-1] in suffix_map.keys():
            suffix = s1[-1]
            f = float(s1[:-1]) * suffix_map[suffix]
        else:
            f = float(s1)
        return int(f)

    i = 0
    retrieved = None
    while i < len(s):
        c = s[i]
        assert isinstance(c, str)
        i += 1
        if c.isdigit() or c == "." or c.lower() in ["k", "m", "b"]:
            if retrieved is None:
                retrieved = c
            else:
                retrieved = retrieved + c
        else:
            if retrieved is None:
                continue
            else:
                return impl(retrieved)
    assert False


def find_element(driver: Chrome, xpath: str):
    WebDriverWait(driver, 30).until(
        expected_conditions.presence_of_element_located((By.XPATH, xpath))
    )
    return driver.find_element(By.XPATH, xpath)


def find_elements(driver: Chrome, xpath: str):
    WebDriverWait(driver, 30).until(
        expected_conditions.presence_of_element_located((By.XPATH, xpath))
    )
    return driver.find_elements(By.XPATH, xpath)


def make_driver() -> Chrome:
    options = ChromeOptions()
    if HEADLESS:
        options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--single-process")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--allow-running-insecure-content")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--allow-insecure-localhost")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    desired_capabilities = DesiredCapabilities().CHROME.copy()
    # desired_capabilities["pageLoadStrategy"] = "eager"
    desired_capabilities["acceptInsecureCerts"] = True

    return Chrome(options=options, desired_capabilities=desired_capabilities)


class PluginData:
    def __init__(
        self,
        path: str,
        stars: Union[int, float],
        last_update: Optional[datetime.datetime],
    ) -> None:
        assert isinstance(path, str)
        assert isinstance(stars, int) or isinstance(stars, float)
        assert isinstance(last_update, datetime.datetime) or last_update is None
        path = path.strip()
        while path.startswith("/"):
            path = path[1:]
        while path.endswith("/"):
            path = path[:-1]
        self.path = path
        self.stars = int(stars)
        self.last_update = last_update

    def __str__(self) -> str:
        return f"<PluginData path:{self.path}, stars:{self.stars}, last_update:{self.last_update.isoformat() if isinstance(self.last_update, datetime.datetime) else None}>"

    def __hash__(self) -> int:
        return hash(self.path.lower())

    def __eq__(self, other) -> bool:
        return isinstance(other, PluginData) and self.path.lower() == other.path.lower()

    def github_url(self) -> str:
        return f"https://github.com/{self.path}"

    def postprocess_branch(self, branch: Optional[str]) -> Optional[str]:
        if "projekt0n/github-nvim-theme" == self.path:
            return "0.0.x"
        return branch

    def fetch_lazy_branch(self) -> Optional[str]:
        has_main = False
        has_master = False
        try:
            with make_driver() as driver:
                driver.get(self.github_url() + "/branches")
                branches = find_elements(driver, "//branch-filter-item")
                for b in branches:
                    if b.get_attribute("branch") == "main":
                        has_main = True
                    if b.get_attribute("branch") == "master":
                        has_master = True
        except Exception as e:
            logging.error(e)

        result = None
        if has_main and has_master:
            result = "main, master"
        elif not has_main and not has_master:
            result = "?"
        return self.postprocess_branch(result)

    def invalid_name(self, name: str) -> bool:
        return name == "vim" or name == "nvim" or name == "neovim"

    def lazy_name(self) -> Optional[str]:
        path_splits = self.path.split("/")
        org = path_splits[0]
        repo = path_splits[1]

        return org if self.invalid_name(repo) else None

    def color_name(self) -> str:
        url_splits = self.path.split("/")
        org = url_splits[0]
        repo = url_splits[1]

        def preprocess(name: str) -> str:
            if name.find("-") > 0:
                name_splits = name.split("-")
                return ",".join([n for n in name_splits if not self.invalid_name(n)])
            elif name.find(".") > 0:
                name_splits = name.split(".")
                return ",".join([n for n in name_splits if not self.invalid_name(n)])
            else:
                return name

        if self.invalid_name(repo):
            return preprocess(org)
        else:
            return preprocess(repo)

    def lazy_config(self) -> Optional[str]:
        if self.path == "rose-pine/neovim":
            return 'require("rose-pine").setup()'
        return None


class Vcs:
    def pages(self) -> Iterable[str]:
        i = 0
        while True:
            if i == 0:
                yield "https://vimcolorschemes.com/top"
            else:
                yield f"https://vimcolorschemes.com/top/page/{i+1}"
            i += 1

    def make_plugin(self, element: WebElement) -> PluginData:
        path = "/".join(
            element.find_element(By.XPATH, "./a[@class='card__link']")
            .get_attribute("href")
            .split("/")[-2:]
        )
        stars = int(
            element.find_element(
                By.XPATH,
                "./a/section/header[@class='meta-header']//div[@class='meta-header__statistic']//b",
            ).text
        )
        creates_updates = element.find_elements(
            By.XPATH,
            "./a/section/footer[@class='meta-footer']//div[@class='meta-footer__column']//p[@class='meta-footer__row']",
        )
        last_update = datetime.datetime.fromisoformat(
            creates_updates[1]
            .find_element(By.XPATH, "./b/time")
            .get_attribute("datetime")
        )
        return PluginData(path, stars, last_update)

    def parse(self):
        plugins = []
        with make_driver() as driver:
            for page_url in self.pages():
                driver.get(page_url)
                any_valid_stars = False
                for element in find_elements(driver, "//article[@class='card']"):
                    plugin = self.make_plugin(element)
                    logging.debug(f"vsc plugin:{plugin}")
                    if plugin.stars < STARS:
                        logging.debug(f"vsc skip for stars - plugin:{plugin}")
                        continue
                    assert isinstance(plugin.last_update, datetime.datetime)
                    if (
                        plugin.last_update.timestamp() + LASTCOMMIT
                        < datetime.datetime.now().timestamp()
                    ):
                        logging.debug(f"vsc skip for last_update - plugin:{plugin}")
                        continue
                    logging.debug(f"vsc get - plugin:{plugin}")
                    plugins.append(plugin)
                    any_valid_stars = True
                if not any_valid_stars:
                    logging.debug(f"vsc no valid stars, exit")
                    break
            return plugins


class Acs:
    def make_plugin(self, element: WebElement) -> PluginData:
        a = element.find_element(By.XPATH, "./a").text
        a_splits = a.split("(")
        path = a_splits[0]
        stars = parse_numbers(a_splits[1])
        return PluginData(path, stars, None)

    def parse_color(self, driver, tag_id) -> list[PluginData]:
        plugins = []
        colors_group = find_element(
            driver,
            f"//main[@class='markdown-body']/h4[@id='{tag_id}']/following-sibling::ul",
        )
        for e in colors_group.find_elements(By.XPATH, "./li"):
            plugin = self.make_plugin(e)
            logging.debug(f"acs plugin:{plugin}")
            plugins.append(plugin)
        return plugins

    def parse(self) -> list[PluginData]:
        plugins = []
        with make_driver() as driver:
            driver.get(
                "https://www.trackawesomelist.com/rockerBOO/awesome-neovim/readme"
            )
            colors = self.parse_color(
                driver, "tree-sitter-supported-colorscheme"
            ) + self.parse_color(driver, "lua-colorscheme")
            for plugin in colors:
                if plugin.stars < STARS:
                    logging.debug(f"asc skip for stars - plugin:{plugin}")
                    continue
                logging.debug(f"acs get - plugin:{plugin}")
                plugins.append(plugin)
        return plugins


def duplicate_color(plugins: list[PluginData], p: PluginData) -> Optional[PluginData]:
    def position(path: str) -> int:
        if path.endswith(".vim"):
            return path.find(".vim")
        if path.endswith(".nvim"):
            return path.find(".nvim")
        if path.endswith("-vim"):
            return path.find("-vim")
        if path.endswith("-nvim"):
            return path.find("-nvim")
        return -1

    def same(r11: PluginData, r22: PluginData):
        r1 = r11.path.split("/")[-1]
        r2 = r22.path.split("/")[-1]
        if r1 == r2 and (
            r1 != "vim"
            and r1 != "nvim"
            and r1 != "neovim"
            and r2 != "vim"
            and r2 != "nvim"
            and r2 != "neovim"
        ):
            return True
        pos1 = position(r1)
        pos2 = position(r2)
        if pos1 <= 0 or pos2 <= 0:
            return False
        base1 = r1[:pos1]
        base2 = r2[:pos2]
        return base1 == base2

    for r1 in plugins:
        if p == r1 or same(r1, p):
            return r1
    return None


def plugin_backlist(p: PluginData) -> bool:
    if p.path.find("rafi/awesome-vim-colorschemes") >= 0:
        return True
    if p.path.find("sonph/onehalf") >= 0:
        return True
    if p.path.find("mini.nvim#minischeme") >= 0:
        return True
    if p.path.find("olimorris/onedarkpro.nvim") >= 0:
        return True
    return False


def filter(existed_plugins: list[PluginData], plugin: PluginData, hint: str) -> bool:
    if plugin_backlist(plugin):
        logging.warning(f"{hint} plugin:{plugin} in blacklist, skip")
        return True
    dup = duplicate_color(existed_plugins, plugin)
    if dup:
        logging.warning(f"{hint} plugin:{plugin} is duplicated with {dup}, skip")
        return True
    return False


def format_lua(plugin: PluginData) -> str:
    name = plugin.lazy_name()
    optional_name = f"{INDENT * 2}name = '{name}',\n" if name else ""
    branch = plugin.fetch_lazy_branch()
    optional_branch = f"{INDENT * 2}branch = '{branch}',\n" if branch else ""
    config = plugin.lazy_config()
    optional_config = (
        f"""{INDENT*2}config = function
{INDENT*3}{config}
{INDENT*2}end,
"""
        if config
        else ""
    )
    return f"""{INDENT}{{
{INDENT*2}-- stars:{int(plugin.stars)}, repo:{plugin.github_url()}
{INDENT*2}'{plugin.path}',
{INDENT*2}lazy = true,
{INDENT*2}priority = 1000,
{optional_name}{optional_branch}{optional_config}{INDENT}}},
"""


def format_vim(plugin: PluginData) -> str:
    return f"{INDENT*3}\\ '{plugin.color_name()}',\n"


if __name__ == "__main__":
    log_level = logging.WARNING
    if "--debug" in sys.argv:
        log_level = logging.DEBUG
    if "--info" in sys.argv:
        log_level = logging.INFO
    logging.basicConfig(
        format="%(asctime)s %(levelname)s [%(filename)s:%(lineno)d](%(funcName)s) %(message)s",
        level=log_level,
    )

    vcs = Vcs().parse()
    acs = Acs().parse()
    existed_plugins: list[PluginData] = []
    with open(LUA_FILE, "w") as luafp, open(VIM_FILE, "w") as vimfp:
        luafp.writelines("return {\n")
        luafp.writelines(f"{INDENT}-- awesome-neovim#colorscheme\n")
        vimfp.writelines("let s:colors=[\n")
        for plugin in sorted(acs, key=lambda r: r.stars, reverse=True):
            if filter(existed_plugins, plugin, "acs"):
                continue
            luafp.writelines(format_lua(plugin))
            vimfp.writelines(format_vim(plugin))
            existed_plugins.append(plugin)
        luafp.writelines(f"\n{INDENT}-- vimcolorschemes.com\n")
        for plugin in sorted(vcs, key=lambda r: r.stars, reverse=True):
            if filter(existed_plugins, plugin, "vcs"):
                continue
            luafp.writelines(format_lua(plugin))
            vimfp.writelines(format_vim(plugin))
            existed_plugins.append(plugin)
        luafp.writelines("}\n")
        vimfp.writelines(f"{INDENT*3}\\]\n")
