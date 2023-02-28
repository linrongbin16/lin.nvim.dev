---
layout: default
title: Appendix
nav_order: 5
---

<!-- markdownlint-disable MD013 MD025 -->

# Appendix

---

- [Dependencies](#dependencies)
- [Plugins](#plugins)
- [Available LSP Servers](#available-lsp-servers)
- [Reference](#reference)

---

## Dependencies

- [Git](https://git-scm.com/).
- [Neovim](https://github.com/neovim/neovim/wiki/Installing-Neovim).
- Programming languages:
  - C/C++ tool chain([clang](https://clang.llvm.org/)/[gcc](https://gcc.gnu.org/), [make](https://www.gnu.org/software/make/), [pkg-config](https://www.freedesktop.org/wiki/Software/pkg-config/), [autoconf](https://www.gnu.org/software/autoconf/), [automake](https://www.gnu.org/software/automake/) and [cmake](https://cmake.org/)).
  - [Python3](https://www.python.org/)(python2 is not supported) and [pynvim](https://pypi.org/project/pynvim/) package.
  - [Node.js](https://nodejs.org/) and [neovim](https://www.npmjs.com/package/neovim) package.
- Download tools: [curl](https://curl.se/), [wget](https://www.gnu.org/software/wget/).
- Unzip tools: [unzip](https://linux.die.net/man/1/unzip), [gzip](https://www.gnu.org/software/gzip/), [7-zip](https://www.7-zip.org/).
- Tags: [universal-ctags](https://github.com/universal-ctags/ctags).
- Modern commands written in rust: [rg](https://github.com/BurntSushi/ripgrep), [fd](https://github.com/sharkdp/fd), [bat](https://github.com/sharkdp/bat), [delta](https://github.com/dandavison/delta).
- Patched-fonts: [hack nerd font](https://github.com/ryanoasis/nerd-fonts/releases/latest).

---

## Plugins

For complete plugins list, please checkout [lua/cfg/plugins.lua](https://github.com/linrongbin16/lin.nvim/blob/main/lua/cfg/plugins.lua).

---

## Available LSP Servers

- assembly:
  - lsp servers: `asm_lsp`
  - null-ls sources: empty
- bash:
  - lsp servers: `bashls`
  - null-ls sources: empty
- c/c++:
  - lsp servers: `clangd`
  - null-ls sources: `cpplint`, `clang_format`
- clojure:
  - lsp servers: `clojure_lsp`
  - null-ls sources: `joker`
- cmake:
  - lsp servers: `cmake`, `neocmake`
  - null-ls sources: empty
- crystal:
  - lsp servers: `crystalline`
  - null-ls sources: empty
- csharp:
  - lsp servers: `csharp_ls`, `omnisharp_mono`, `omnisharp`
  - null-ls sources: `csharpier`, `clang_format`
- css:
  - lsp servers: `cssls`, `cssmodules_ls`, `unocss`
  - null-ls sources: empty
- docker:
  - lsp servers: `dockerls`
  - null-ls sources: `hadolint`
- dot(graphviz):
  - lsp servers: `dotls`
  - null-ls sources: empty
- elixir:
  - lsp servers: `elixirls`
  - null-ls sources: empty
- erlang:
  - lsp servers: `erlangls`
  - null-ls sources: empty
- fortran:
  - lsp servers: `fortls`
  - null-ls sources: empty
- fsharp:
  - lsp servers: `fsautocomplete`
  - null-ls sources: empty
- go:
  - lsp servers: `golangci_lint_ls`, `gopls`
  - null-ls sources: `gofumpt`, `goimports`, `goimports_reviser`, `golangci_lint`, `golines`, `revive`, `staticcheck`
- groovy:
  - lsp servers: `groovyls`
  - null-ls sources: empty
- haskell:
  - lsp servers: `hls`
  - null-ls sources: empty
- html:
  - lsp servers: `html`
  - null-ls sources: `curlylint`
- java:
  - lsp servers: `jdtls`
  - null-ls sources: `clang_format`
- javascript/typescript:
  - lsp servers: `quick_lint_js`, `tsserver`, `vtsls`, `eslint`
  - null-ls sources: `rome`, `xo`, `eslint_d`, `prettier`, `prettierd`
- json:
  - lsp servers: `jsonls`
  - null-ls sources: `fixjson`, `jq`, `cfn_lint`
- julia:
  - lsp servers: `julials`
  - null-ls sources: `fixjson`, `jq`
- kotlin:
  - lsp servers: `kotlin_language_server`
  - null-ls sources: `ktlint`
- latex:
  - lsp servers: `ltex`, `texlab`
  - null-ls sources: `proselint`, `vale`
- lua:
  - lsp servers: `lua_ls`
  - null-ls sources: `selene`, `stylua`
- luarocks:
  - lsp servers: empty
  - null-ls sources: `luacheck`
- markdown:
  - lsp servers: `marksman`, `prosemd_lsp`, `remark_ls`, `zk`
  - null-ls sources: `alex`, `markdownlint`, `write_good`, `cbfmt`, `proselint`, `vale`
- ocaml:
  - lsp servers: `ocamllsp`
  - null-ls sources: empty
- perl:
  - lsp servers: `perlnavigator`
  - null-ls sources: empty
- php:
  - lsp servers: `intelephense`, `phpactor`, `psalm`
  - null-ls sources: `phpcbf`, `psalm`
- powershell:
  - lsp servers: `powershell_es`
  - null-ls sources: empty
- protobuf:
  - lsp servers: `bufls`
  - null-ls sources: `buf`, `protolint`
- python:
  - lsp servers: `jedi_language_server`, `pyre`, `pyright`, `sourcery`, `pylsp`, `ruff_lsp`
  - null-ls sources: `autopep8`, `black`, `blue`, `flake8`, `isort`, `mypy`, `pylint`, `vulture`, `yapf`
- R:
  - lsp servers: `r_language_server`
  - null-ls sources: empty
- ruby:
  - lsp servers: `ruby_ls`, `solargraph`
  - null-ls sources: `rubocop`, `standardrb`, `erb_lint`
- rust:
  - lsp servers: `rust_analyzer`
  - null-ls sources: empty
- sql:
  - lsp servers: `sqlls`, `sqls`
  - null-ls sources: `sqlfluff`, `sql_formatter`
- sh:
  - lsp servers: empty
  - null-ls sources: `shellcheck`, `shellharden`, `shfmt`
- solidity:
  - lsp servers: `solang`, `solc`, `solidity`
  - null-ls sources: `solhint`
- toml:
  - lsp servers: `taplo`
  - null-ls sources: `taplo`
- vim:
  - lsp servers: `vimls`
  - null-ls sources: `vint`
- xml:
  - lsp servers: `lemminx`
  - null-ls sources: empty
- yaml:
  - lsp servers: `yamlls`
  - null-ls sources: `actionlint`, `yamlfmt`, `yamllint`, `cfn_lint`

---

## Reference

- [mason.nvim - Mason Package Index](https://github.com/williamboman/mason.nvim/blob/main/PACKAGES.md)
- [mason-lspconfig.nvim - Available LSP servers](https://github.com/williamboman/mason-lspconfig.nvim#available-lsp-servers)
- [mason-null-ls.nvim - Available Null-ls sources](https://github.com/jay-babu/mason-null-ls.nvim#available-null-ls-sources)
- [null-ls.nvim - Built-in Sources](https://github.com/jose-elias-alvarez/null-ls.nvim/blob/main/doc/BUILTINS.md#built-in-sources)
