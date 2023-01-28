---
layout: default
title: Manage LSP Servers
nav_order: 1
parent: User Guide
has_toc: false
---

# Manage LSP Servers

- [Plugins](#plugins)
- [Use Cases](#use-cases)

By default, [a bunch of language servers](/lin.nvim.dev/appendix/#lsp-servers) are already embedded. But sooner or later you will manage LSP servers yourself.

---

## Plugins

Unlike [coc.nvim](https://github.com/neoclide/coc.nvim), there's no such all-in-one framework in neovim's LSP world. Quite a few [plugins](/lin.nvim.dev/user-guide/#ide-like-editing-features) are assembled to work it out:

- [nvim-lspconfig](https://github.com/neovim/nvim-lspconfig) for LSP servers configuration, as a pre-requirement of other plugins.
- [nvim-cmp](https://github.com/hrsh7th/nvim-cmp) for complete engine, and its sources([cmp-nvim-lsp](https://github.com/hrsh7th/cmp-nvim-lsp), [cmp-buffer](https://github.com/hrsh7th/cmp-buffer), [cmp-path](https://github.com/hrsh7th/cmp-path), [cmp-cmdline](https://github.com/hrsh7th/cmp-cmdline), [LuaSnip](https://github.com/L3MON4D3/LuaSnip), [cmp_luasnip](https://github.com/saadparwaiz1/cmp_luasnip)).
- [mason.nvim](https://github.com/williamboman/mason.nvim) for LSP server management, and ensure LSP servers installed by [mason-lspconfig.nvim](https://github.com/williamboman/mason-lspconfig.nvim).
- [null-ls.nvim](https://github.com/jose-elias-alvarez/null-ls.nvim) for extra capability(formatter/linter/codeAction/diagnostic) by injecting LSP server with sources, and ensure sources installed by [mason-null-ls.nvim](https://github.com/jay-babu/mason-null-ls.nvim).

More UI improve plugins leave to you to find out.

---

## Use Cases

You could install new LSP servers by manual commands `:Mason`/`:LspInstall`/`:NullLsInstall`, but that's only recommanded when the server cannot be ensure-installed by mason-lspconfig or mason-null-ls.

<!-- found in [mason-lspconfig's Available LSP servers](https://github.com/williamboman/mason-lspconfig.nvim#available-lsp-servers) or [mason-null-ls's Available Null-ls sources](https://github.com/jay-babu/mason-null-ls.nvim#available-null-ls-sources). -->

_~/.nvim/lua/lspservers.lua_ provides two config list `embeded_servers`/`embeded_extras` to automatically setup all the packages.

- Case-1: add LSP server name in `embeded_servers`, it will work as a nvim-cmp source, ensure-installed by mason-lspconfig.
- Case-2: add extra null-ls source in `embeded_extras`, it will work as a null-ls source, ensure-installed by mason-null-ls.

Here's an example:

```lua
local embeded_servers = {
    "clangd",   -- c/c++
    "cmake",    -- cmake
    "pyright",  -- python
}
local embeded_extras = {
    -- js/ts
    -- eslint_d and prettierd are not valid LSP servers,
    -- They're not working through nvim-cmp when editing js/ts files.
    -- So registered them as null-ls sources to let them work.
    {
        "eslint_d",
        {
            null_ls.builtins.diagnostics.eslint_d,
            null_ls.builtins.formatting.eslint_d,
            null_ls.builtins.code_actions.eslint_d,
        }
    },
    { "prettierd", { null_ls.builtins.formatting.prettierd } },

    -- python
    -- pyright doesn't have a formatter.
    -- So registered black/isort as null-ls sources to let them work.
    { "black", { null_ls.builtins.formatting.black } },
    { "isort", { null_ls.builtins.formatting.isort } },
}
```

{: .important-title}

> Notice
>
> - For `embeded_servers`, please refer to [mason-lspconfig's Available LSP servers](https://github.com/williamboman/mason-lspconfig.nvim#available-lsp-servers) for all LSP server names.
> - For `embeded_extras`, please refer to:
>   1. [mason-null-ls's Available Null-ls sources](https://github.com/jay-babu/mason-null-ls.nvim#available-null-ls-sources) for all source names.
>   2. [null-ls's BUILTINS](https://github.com/jose-elias-alvarez/null-ls.nvim/blob/main/doc/BUILTINS.md) for all null-ls builtin configs.

{: .note}

> Configure these LSP servers in _~/.nvim/lua/lspservers.lua_.
