---
layout: default
title: Manage LSP Servers
nav_order: 1
parent: User Guide
---

# Manage LSP Servers

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

LSP server management is supported by _mason.nvim_, it provides vim command `:Mason` to search/install/uninstall LSP servers. Additionally, _mason-lspconfig.nvim_ provides `:LspInstall`(see [mason-lspconfig.nvim - Available LSP servers](https://github.com/williamboman/mason-lspconfig.nvim#available-lsp-servers)), and _mason-null-ls.nvim_ provides `NullLsInstall`(see [mason-null-ls.nvim - Available Null-ls sources](https://github.com/jay-babu/mason-null-ls.nvim#available-null-ls-sources)) to install LSP servers as well.

But installing LSP is just the first step to making LSP work for you.

later you will see, a config file is provided to avoid manual work, which is recommended.

For other formatters/linters that cannot work with nvim-cmp as a LSP server, register them via _nvim-ls.nvim_. For examples:

1. [Pyright](https://github.com/microsoft/pyright) cannot format code itself, while [black](https://pypi.org/project/black/)/[isort](https://pypi.org/project/isort/) are not working with nvim-cmp as python's LSP servers. Registering them in _null-ls.nvim_ as formatters could solve the issue.
2. Want [eslint](https://eslint.org/)/[prettier](https://prettier.io/) as extra linter/formatter, but they're not even LSP servers. Registering them in _null-ls.nvim_ as linter/formatter could solve the issue.

To ensure LSP servers and formatters embedded, [mason-lspconfig.nvim](https://github.com/williamboman/mason-lspconfig.nvim) (for LSP servers), [null-ls.nvim](https://github.com/jose-elias-alvarez/null-ls.nvim) and [mason-null-ls.nvim](https://github.com/jay-babu/mason-null-ls.nvim) (for formatters/linters) are introduced as well.

To simplify the setup for all above plugins, all you need is to define 4 components in below configurations:

1. LSP server (used by _mason-lspconfig.nvim_ for ensure installation). For example `clangd`, `pyright`. Please refer to [mason-lspconfig.nvim - Available LSP servers](https://github.com/williamboman/mason-lspconfig.nvim#available-lsp-servers) for more LSP servers .
2. Configuration for lspconfig (used by [nvim-lspconfig](https://github.com/neovim/nvim-lspconfig)). Usually it's just an empty table `{}`.
3. (Optional) Extra formatter/linter (used by _mason-null-ls.nvim_ for ensure installation). For example `eslint`, `prettierd`, `black`. Please refer to [mason-lspconfig.nvim - Available Null-ls sources](https://github.com/jay-babu/mason-null-ls.nvim#available-null-ls-sources) for more mason-null-ls sources.
4. (Optional) Extra null-ls sources (used by _null-ls.nvim_ to enable the sources). For example `null_ls.builtins.code_actions.eslint`, `null_ls.builtins.formatting.prettierd`, `null_ls.builtins.formatting.black`. Please refer to [null-ls.nvim - BUILTINS.md](https://github.com/jose-elias-alvarez/null-ls.nvim/blob/main/doc/BUILTINS.md) for more null-ls builtin sources.

Let's see how to configure LSP server and formatter for python in real world:

```lua
local lsp_servers = {
    python = {
        "pyright",  -- 1. LSP server
        {},         -- 2. lspconfig
        {"black", "isort"},     -- formatters
        {
            null_ls.builtins.formatting.black, -- sources for null-ls
            null_ls.builtins.formatting.isort
        }
    },
}
```

You could add new or configure embedded LSP servers in _~/.vim/lsp-settings.vim_.
