#!/usr/bin/env python3

import datetime
import logging
import os
import pathlib
import shutil
from dataclasses import is_dataclass

from colorutil import INDENT, GitObject, Repo, init_logging, parse_options


def dedup() -> set[Repo]:
    def greater_than(a: Repo, b: Repo) -> bool:
        if a.priority != b.priority:
            return a.priority > b.priority
        if a.stars != b.stars:
            return a.stars > b.stars
        # for duplicated colors, we suppose neovim/lua plugins are better
        # and we don't fetch last commit datetime in awesome-neovim's plugins
        # so the repo don't have last_update has higher priority
        if a.last_update is None or b.last_update is None:
            return True if a.last_update is None else False
        return a.last_update.timestamp() > b.last_update.timestamp()

    colors: dict[str, Repo] = dict()
    repos: set[Repo] = set()

    for repo in Repo.get_all():
        with GitObject(repo) as candidate:
            for color in candidate.colors:
                # detect duplicated color
                if color in colors:
                    old_repo = colors[color]
                    logging.info(
                        f"detect duplicated color on new repo:{repo} and old repo:{old_repo}"
                    )
                    # replace old repo if new repo has higher priority
                    if greater_than(repo, old_repo):
                        logging.info(
                            f"replace old repo:{old_repo} with new repo:{repo}"
                        )
                        colors[color] = repo
                        repos.add(repo)
                        repos.remove(old_repo)
                else:
                    # add new color
                    colors[color] = repo
                    repos.add(repo)
    return repos


def path2str(p: pathlib.Path) -> str:
    result = str(p)
    if result.find("\\") >= 0:
        result = result.replace("\\", "/")
    return result


def dump_color(luafp, vimfp, repo: Repo) -> None:
    colors_dir = pathlib.Path(f"candidate/{repo.url}/colors")
    colors_files = [
        f
        for f in colors_dir.iterdir()
        if f.is_file() and (str(f).endswith(".vim") or str(f).endswith(".lua"))
    ]
    colors = [str(c.name)[:-4] for c in colors_files]
    for c in colors:
        vimfp.writelines(f"{INDENT*3}\\ '{c}',\n")
    name = repo.name()
    optional_name = f"{INDENT * 2}name = '{name}',\n" if name else ""
    branch = repo.config.branch if repo.config and repo.config.branch else None
    optional_branch = f"{INDENT * 2}branch = '{branch}',\n" if branch else ""
    luafp.writelines(
        f"""{INDENT}{{
{INDENT*2}-- stars:{int(repo.stars)}, repo:{repo.get_github_url()}
{INDENT*2}'{repo.url}',
{INDENT*2}lazy = true,
{INDENT*2}priority = 1000,
{optional_name}{optional_branch}{INDENT}}},\n"""
    )


def build() -> None:
    # clean candidate dir
    candidate_path = pathlib.Path("candidate")
    if candidate_path.exists() and candidate_path.is_dir():
        shutil.rmtree(candidate_path)

    # clone candidates
    for repo in Repo.get_all():
        with GitObject(repo) as candidate:
            candidate.clone()

    # dedup candidates
    deduped_repos = dedup()

    # dump colors
    with open("colors.lua", "w") as luafp, open("colors.vim", "w") as vimfp:
        luafp.writelines("return {\n")
        vimfp.writelines("let s:colors=[\n")
        for repo in deduped_repos:
            dump_color(luafp, vimfp, repo)
        luafp.writelines("}\n")
        vimfp.writelines(f"{INDENT*3}\\]\n")


if __name__ == "__main__":
    options = parse_options()
    init_logging(options)
    build()
