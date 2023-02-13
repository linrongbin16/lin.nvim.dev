---
layout: default
title: Manage LSP Servers
nav_order: 1
parent: User Guide
has_toc: false
---

# Manage LSP Servers

---

- [Plugins](#plugins)
- [Use Cases](#use-cases)

---

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
_~/.nvim/lua/lspservers.lua_ provides two groups of lua tables:

- `embeded_servers`/`embeded_server_setups`: Former setup mason's lsp servers, latter setup lsp configs.
- `embeded_nulllses`/`embeded_nullls_setups`: Former setup null-ls sources, latter setup null-ls configs.

Since we're using mason-lspconfig and mason-null-ls, both setup could be done automatically by the **default setup** handler.
So simply add/remove the items in `embeded_servers` and `embeded_nulllses` can meet most needs, or specific setup handlers for customization.

Here's an example:

```lua
local null_ls = require("null-ls")

-- { mason's config
local embeded_servers = {
  -- clang
  "clangd",
  -- lua
  "lua_ls",
  -- python
  "pyright",
}
local embeded_server_setups = {
  -- default setup
  function(server)
    require("lspconfig")[server].setup({})
  end,
  -- specific setup
  clangd = function()
    require("clangd_extensions").setup({
      extensions = {
        ast = {
          role_icons = {
            type = "",
            declaration = "",
            expression = "",
            specifier = "",
            statement = "",
            ["template argument"] = "",
          },
          kind_icons = {
            Compound = "",
            Recovery = "",
            TranslationUnit = "",
            PackExpansion = "",
            TemplateTypeParm = "",
            TemplateTemplateParm = "",
            TemplateParamObject = "",
          },
        },
      },
    })
  end,
  -- ["rust_analyzer"] = function()
  --   require("rust-tools").setup({})
  -- end,
}
-- }

-- {
local embeded_nulllses = {
  -- js/ts
  "eslint_d",
  "prettierd",
  -- lua
  "stylua", -- Better lua formatter
  -- python
  "black", -- Since pyright doesn't include code format.
  "isort", -- Use black/isort as code formatter.
}
local embeded_nullls_setups = {
  -- default setup
  function(source, methods)
    require("mason-null-ls.automatic_setup")(source, methods)
  end,
  -- specific setup
  stylua = function(source, methods)
    null_ls.register(null_ls.builtins.formatting.stylua)
  end,
}
-- }

```

{: .important-title}

> Notice
>
> - For `embeded_servers`, please refer to:
>   - [mason-lspconfig's Available LSP servers](https://github.com/williamboman/mason-lspconfig.nvim#available-lsp-servers) for all LSP server names.
> - For `embeded_nulllses`/`embeded_nullls_setups`, please refer to:
>   - [mason-null-ls's Available Null-ls sources](https://github.com/jay-babu/mason-null-ls.nvim#available-null-ls-sources) for all source names.
>   - [null-ls's BUILTINS](https://github.com/jose-elias-alvarez/null-ls.nvim/blob/main/doc/BUILTINS.md) for all null-ls builtin configs.

{: .note}

> Configure these LSP servers in _~/.nvim/lua/lspservers.lua_.
