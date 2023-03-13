---
layout: default
title: Manage LSP Servers
nav_order: 1
parent: User Guide
has_toc: false
---

<!-- markdownlint-disable MD013 MD025 -->

# Manage LSP Servers

---

- [Plugins](#plugins)
- [Use Cases](#use-cases)
- [Embeded LSP Servers](#embeded-lsp-servers)
- [Reference](#reference)

---

Unlike [coc.nvim](https://github.com/neoclide/coc.nvim), there's no such all-in-one framework in neovim's LSP world.
But with the help of [mason.nvim](https://github.com/williamboman/mason.nvim) and [null-ls.nvim](https://github.com/jose-elias-alvarez/null-ls.nvim), install and configure new lsp servers is just a piece of cake now.

---

## Plugins

To bring this easy-to-use LSP based auto-complete feature to users, quite a few [plugins](/lin.nvim.dev/docs/appendix/#lsp) are assembled together:

- [nvim-lspconfig](https://github.com/neovim/nvim-lspconfig) for LSP servers configuration, as a pre-requirement of other plugins.
- [nvim-cmp](https://github.com/hrsh7th/nvim-cmp) for complete engine, and its sources([cmp-nvim-lsp](https://github.com/hrsh7th/cmp-nvim-lsp), [cmp-buffer](https://github.com/hrsh7th/cmp-buffer), [cmp-path](https://github.com/hrsh7th/cmp-path), [cmp-cmdline](https://github.com/hrsh7th/cmp-cmdline), [LuaSnip](https://github.com/L3MON4D3/LuaSnip), [cmp_luasnip](https://github.com/saadparwaiz1/cmp_luasnip)).
- [mason.nvim](https://github.com/williamboman/mason.nvim) for LSP server management, and ensure LSP servers installed by [mason-lspconfig.nvim](https://github.com/williamboman/mason-lspconfig.nvim).
- [null-ls.nvim](https://github.com/jose-elias-alvarez/null-ls.nvim) for extra capability(formatter/linter/codeAction/diagnostic) by injecting LSP server with sources, and ensure sources installed by [mason-null-ls.nvim](https://github.com/jay-babu/mason-null-ls.nvim).

More UI improve plugins leave to you to find out.

---

## Use Cases

By default, You could just install new LSP servers by `:LspInstall`, and manage/remove them by `:Mason`, and that's all!

But if you want to customize setups, _~/.nvim/lua/lspservers.lua_ provides two groups of lua tables:

- `embeded_servers`/`embeded_servers_setups`: Former setup mason's LSP servers, latter setup LSP configs.
- `embeded_nullls`/`embeded_nullls_setups`: Former setup null-ls sources, latter setup null-ls configs.

Here's an example:

```lua
local null_ls = require("null-ls")

-- { mason's servers
local embeded_servers = {
  -- bash
  "bashls",
  -- clang
  "clangd",
  -- lua
  "lua_ls",
  -- python
  "pyright",
}
local embeded_servers_setups = {
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
  ["rust_analyzer"] = function()
    require("rust-tools").setup({})
  end,
}
-- }

-- { null-ls's sources
local embeded_nullls = {
  -- js/ts
  "eslint_d",
  "prettierd",
  -- lua
  "stylua", -- Better lua formatter.
  -- python
  "black", -- Since pyright doesn't include code format.
  "isort", -- Use black/isort as code formatter.
  -- bash
  "shfmt", -- Bash formatter.
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

## Reference

- For `embeded_servers`/`embeded_servers_setups`, please refer to:
  - [mason-lspconfig's Available LSP servers](https://github.com/williamboman/mason-lspconfig.nvim#available-lsp-servers) for all LSP server names.
  - [nvim-lspconfig's LSP configurations](https://github.com/neovim/nvim-lspconfig/blob/master/doc/server_configurations.md) for all LSP configurations.
  - [nvim-lspconfig's recommended specific language plugins](https://github.com/neovim/nvim-lspconfig/wiki/Language-specific-plugins) for enhancements for specific languages.
- For `embeded_nullls`/`embeded_nullls_setups`, please refer to:
  - [mason-null-ls's Available Null-ls sources](https://github.com/jay-babu/mason-null-ls.nvim#available-null-ls-sources) for all source names.
  - [null-ls's BUILTINS](https://github.com/jose-elias-alvarez/null-ls.nvim/blob/main/doc/BUILTINS.md) for all null-ls builtin configs.

{: .note}

> Configure these LSP servers in _~/.nvim/lua/cfg/lspservers.lua_.
