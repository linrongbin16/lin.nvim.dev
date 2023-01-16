---
layout: default
title: Manage LSP Servers
nav_order: 1
parent: User Guide
---

# Manage LSP Servers

- [Introduction](#introduction)
- [Use Cases](#use-cases)

## Introduction

By default, [a bunch of language servers](/lin.nvim.dev/appendix/#lsp-servers) are already embedded. But sooner or later you will manage LSP servers yourself.

Unlike [coc.nvim](https://github.com/neoclide/coc.nvim), there's no such all-in-one framework in neovim's LSP world. Quite a few [plugins](/lin.nvim.dev/user-guide/#ide-like-editing-features) are assembled to work it out:

- [nvim-lspconfig](https://github.com/neovim/nvim-lspconfig) for LSP servers configuration.
- [nvim-cmp](https://github.com/hrsh7th/nvim-cmp) for complete engine, and its sources([cmp-nvim-lsp](https://github.com/hrsh7th/cmp-nvim-lsp), [cmp-buffer](https://github.com/hrsh7th/cmp-buffer), [cmp-path](https://github.com/hrsh7th/cmp-path), [cmp-cmdline](https://github.com/hrsh7th/cmp-cmdline), [LuaSnip](https://github.com/L3MON4D3/LuaSnip), [cmp_luasnip](https://github.com/saadparwaiz1/cmp_luasnip), [friendly-snippets](rafamadriz/friendly-snippets)).
- [mason.nvim](https://github.com/williamboman/mason.nvim) for LSP server management, and ensure LSP servers installed through [mason-lspconfig.nvim](https://github.com/williamboman/mason-lspconfig.nvim).
- [null-ls.nvim](https://github.com/jose-elias-alvarez/null-ls.nvim) for injecting LSP server with extra capability sources(formatter/linter/codeAction/diagnostic), and integrated with mason through [mason-null-ls.nvim](https://github.com/jay-babu/mason-null-ls.nvim).

Besides there're more plugins for UI improvement, leave them to you to find out.

---

## Use Cases

_~/.vim/lsp-settings.vim_ provides two config list `embeded_servers`/`embeded_extras` to automatically install and setup all the packages.

- Case-1: add LSP server name in `embeded_servers`, it will work as a nvim-cmp source, ensure-installed through mason-lspconfig.
- Case-2: add extra null-ls source in `embeded_extras`, it will be registered as a null-ls source, work as an extra formatter/linter/diagnostic/codeAction/etc, ensure-installed through mason-null-ls.

Here're some examples:

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

{: .note-title}

> Notice
>
> Each item in `embeded_servers` is a string for a valid LSP server name. They will be ensure-installed through mason-lspconfig, registered as LSP server, and working through nvim-cmp.
> Please refer to [mason-lspconfig Available LSP servers](https://github.com/williamboman/mason-lspconfig.nvim#available-lsp-servers) for all LSP server names.
>
> Each item in `embeded_extras` is an array with two elements:
>
> 1. The first is a string for a valid mason package name, it will be ensure-installed through mason-null-ls. Please refer to [mason-null-ls Available Null-ls sources](https://github.com/jay-babu/mason-null-ls.nvim#available-null-ls-sources) for all packages.
> 2. The second is another array with related null-ls source configs. They will be registered in null-ls, and working through null-ls LSP server. Please refer to [null-ls BUILTINS](https://github.com/jose-elias-alvarez/null-ls.nvim/blob/main/doc/BUILTINS.md) for all null-ls builtin configs.

Configure all embedded LSP servers in _~/.vim/lsp-settings.vim_.
