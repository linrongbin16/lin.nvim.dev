---
layout: default
title: Manage LSP Servers
nav_order: 1
parent: User Guide
---

# Manage LSP Servers

TL;DR: check [Configuration](#configuration) for adding new or configuring existing LSP servers, and [Non-Manual Configuration](#non-manual-configuration) for fully automated.

## Introduction

By default, [a bunch of language servers](/lin.nvim.dev/appendix/#lsp-servers) are already embedded. But sooner or later you will manage LSP servers yourself.

Unlike [coc.nvim](https://github.com/neoclide/coc.nvim), there's no such all-in-one framework in neovim's LSP world. Quite a few [plugins](/lin.nvim.dev/user-guide/#ide-like-editing-features) are assembled to work it out:

- [nvim-lspconfig](https://github.com/neovim/nvim-lspconfig) for LSP servers configuration.
- [nvim-cmp](https://github.com/hrsh7th/nvim-cmp) for complete engine, and its sources:
  - [cmp-nvim-lsp](https://github.com/hrsh7th/cmp-nvim-lsp)
  - [cmp-buffer](https://github.com/hrsh7th/cmp-buffer)
  - [cmp-path](https://github.com/hrsh7th/cmp-path)
  - [cmp-cmdline](https://github.com/hrsh7th/cmp-cmdline)
  - [LuaSnip](https://github.com/L3MON4D3/LuaSnip)
  - [cmp_luasnip](https://github.com/saadparwaiz1/cmp_luasnip)
  - [friendly-snippets](rafamadriz/friendly-snippets)
- [mason.nvim](https://github.com/williamboman/mason.nvim) for LSP server manager, and its extensions:
  - [mason-lspconfig.nvim](https://github.com/williamboman/mason-lspconfig.nvim)
  - [mason-null-ls.nvim](https://github.com/jay-babu/mason-null-ls.nvim).
- [null-ls.nvim](https://github.com/jose-elias-alvarez/null-ls.nvim) for extra formatters/linters.

Besides there're more plugins for UI improvement, leave them to you to find out.

---

## Functions and Roles

- _nvim-lspconfig_: provides default config for most LSP servers, and an infrastructure for almost all other LSP plugins(since the naive nvim LSP client is not ready to use).
- _nvim-cmp_: a complete engine, provides the IDE-like editing abilities directly: auto-complete, code format, lint, diagnostics, code actions, etc. But it needs other plugins as completion sources.
- _null-ls_: a complementary for _nvim-cmp_, provides extra formatters/linters/diagnostics/code actions/etc(for example eslint/prettier/spellcheck).
- _mason_: LSP servers management. It uses pip/npm/cargo to manage LSP servers, and maybe some specific language compiler for the related LSP server(for example gopls for go).
- _mason-lspconfig_: provides ensure installed ability to manage LSP servers for _mason_, which originally only provides vim commands (`:Mason`,`:MasonInstall`,`:MasonUninstall`,etc) for manual management.
- _mason-null-ls_: provides both ensure installed ability and vim commands(`:NullLsInstall`,`:NullLsUninstall`,etc) to manage sources for _null-ls_, which originally doesn't have a way to manage its sources.

Here's some cases to show you how these plugins working together:

1. [Clangd](https://clangd.llvm.org/) as a c/c++ LSP. After install and config, clangd will do everything(auto-complete/code-format/lint/diagnostics) via _nvim-cmp_ for you, no extra work needed.
2. [Pyright](https://github.com/microsoft/pyright) as a python LSP, cannot code-format through _nvim-cmp_. Even after installed [black](https://pypi.org/project/black/)/[isort](https://pypi.org/project/isort/) in _mason_, they're not working with _nvim-cmp_ as LSP servers. To fix this, we need to register black/isort in _null-ls_ as formatters to make it work.
3. [Eslint](https://eslint.org/)/[prettier](https://prettier.io/) as linter/formatter, they're not even LSP servers, and cannot be installed via _mason_. Thus we need to install them via _mason-null-ls_, and register them in _null-ls_ as linter/formatter. Issue solved.

---

## Configuration

To add support for a specific language:

### Option-1: Use _mason_ + _nvim-cmp_

1. Install the specific LSP server using _mason_(`:MasonInstall`) or _mason-lspconfig_(`:LspInstall`), for example `clangd`, `pyright`. Please refer to [mason-lspconfig.nvim - Available LSP servers](https://github.com/williamboman/mason-lspconfig.nvim#available-lsp-servers) for more LSP servers.
2. Setup config for _nvim-lspconfig_, usually it's just an empty table `{}`. Then _nvim-cmp_ should be working for you.

### Option-2: Use _mason-null-ls_ + _null-ls_

Option-1 should be enough for most languages. But still there're some cases that exceed the limit of LSP. For example:

1. _Pyright_: lack of code formatting.
2. _eslint_/_prettier_: powerful linter/formatter, but not a LSP server.

In this case, we need to:

1. Install the sources using _mason-null-ls_(`NullLsInstall`), for example `prettier`. Please refer to [mason-null-ls.nvim - Available Null-ls sources](https://github.com/jay-babu/mason-null-ls.nvim#available-null-ls-sources) for more sources.
2. Setup source for _null-ls_. Find built-in source in [null-ls.nvim - BUILTINS](https://github.com/jose-elias-alvarez/null-ls.nvim/blob/main/doc/BUILTINS.md), or config your own source following [null-ls.nvim - CONFIG](https://github.com/jose-elias-alvarez/null-ls.nvim/blob/main/doc/CONFIG.md).

---

### Non-Manual Configuration

_~/.vim/lsp-settings.vim_ provides a config list to avoid all the manual work. Here's an example:

```lua
local lsp_servers = {
    c = { "clangd", nil, nil },
    python = {
        "pyright",              -- 1. LSP server for nvim-cmp, installed via mason-lspconfig.
        {"black", "isort"},     -- 2. Sources for null-ls, installed via mason-null-ls.
        {                       -- 3. Source configurations for null-ls.
            null_ls.builtins.formatting.black,
            null_ls.builtins.formatting.isort
        },
    },
    prettier = {
        nil,                    -- Set nil if you don't need it.
        {"prettierd"},
        {
            null_ls.builtins.formatting.prettierd
        }
    },
    -- other things
}
```

In each config item, there're 3 components(see comments in above) for a specific language:

1. LSP server.
2. Null-ls sources.
3. Null-ls source configs.

They're doing exactly the same work as option-1 and option-2 in [Configuration](#configuration).

You could add new or configure embedded LSP servers in _~/.vim/lsp-settings.vim_.
