---
layout: default
title: User Guide
nav_order: 4
---

# User Guide

- [Global Key Mappings](#global-key-mappings)
  - [Hot Keys](#hot-keys)
  - [Ctrl+? Cmd+? Keys](#ctrl-cmd-keys)
- [UI](#ui)
  - [File Explorer](#file-explorer)
- [IDE-like Editing Features](#ide-like-editing-features)
  - [Code Complete](#code-complete)
  - [Symbols](#symbols)
  - [Diagnostics](#diagnostics)
  - [Code Format](#code-format)
  - [Code Actions](#code-actions)
  - [Git](#git)
  - [Manage LSP Servers](#manage-lsp-servers)
- [Search](#search)
  - [Text Search](#text-search)
  - [File Search](#file-search)
  - [Git Search](#git-search)
  - [Other Search](#other-search)
- [Editing Enhancement](#editing-enhancement)
  - [Easy Comment](#easy-comment)
  - [Cursor Motion](#cursor-motion)
  - [Word Movement](#word-movement)
  - [Better Repeat](#better-repeat)
  - [Better Matching](#better-matching)
  - [Auto Pair and Close HTML Tag](#auto-pair-and-close-html-tag)
- [Customization](#customization)

In this section, vim editing modes are specified with:

<!-- alphabet emoji: https://emojicombos.com/emoji-letters -->
<!-- complete emoji list: https://dev.to/nikolab/complete-list-of-github-markdown-emoji-markup-5aia -->
<!-- complete emoji list 2: https://gist.github.com/rxaviers/7360908 -->

- **🅽**: normal mode.
- **🆅**: visual/select mode.
- **🅸**: insert mode.

Meta-key (_M_), alt-key (_A_) (on Windows/Linux), and command-key (_D_) (on macOS) are collectively referred as:

- _M_

---

## Global Key Mappings

### Hot Keys

- `F1` **🅽** - Toggle file explorer.
- `F2` **🅽** - Toggle undo-tree.
- `F3` **🅽** - Toggle structure outlines(tags).
- `F4` **🅽** - Switch between C/C++ headers and sources.
- `F7` **🅽** - Toggle git blame on current line.
- `F8` **🅽** - Open markdown preview.
- `F9` **🅽** - Toggle terminal.
- `F10` **🅽** - Toggle buffers explorer.

### Ctrl+? Cmd+? Keys

Ctrl+? follows the classic behavior under Windows:

- `<C-a>` **🅽** **🆅** **🅸** - Select all.
- `<C-c>` **🅽** **🆅** **🅸** - Copy to clipboard.
- `<C-x>` **🅽** **🆅** **🅸** - Cut to clipboard.
- `<C-v>` **🅽** **🆅** **🅸** - Paste from clipboard.
- `<C-s>` **🅽** **🆅** **🅸** - Save file.
- `<C-y>` **🅽** **🆅** **🅸** - Redo.
- `<C-z>` **🅽** **🆅** **🅸** - Undo.
- `<C-q>` **🅽** - Switch to block-visual mode, same as vim's original _ctrl+v_ (since we mapped it to paste).

For macOS, cmd+? follows the same behavior(ctrl+? works as well):

- `<D-a>` **🅽** **🆅** **🅸** - Same as `<C-a>`.
- `<D-c>` **🅽** **🆅** **🅸** - Same as `<C-c>`.
- `<D-x>` **🅽** **🆅** **🅸** - Same as `<C-x>`.
- `<D-v>` **🅽** **🆅** **🅸** - Same as `<C-v>`.
- `<D-s>` **🅽** **🆅** **🅸** - Same as `<C-s>`.
- `<D-y>` **🅽** **🆅** **🅸** - Same as `<C-y>`.
- `<D-z>` **🅽** **🆅** **🅸** - Same as `<C-z>`.

Copy/paste across different vim instances through remote ssh could be difficult, so introduce two shortcuts using local cache:

- `<Leader>y` **🆅** - Copy selected text to cache.
- `<Leader>p` **🅽** - Paste from cache to current cursor.

Configure these key mappings in _~/.vim/settings.vim_.

---

## UI

### File Explorer

Supported by [nvim-tree.lua](https://github.com/kyazdani42/nvim-tree.lua). Please refer to [:help nvim-tree.view.mappings](https://github.com/nvim-tree/nvim-tree.lua/blob/master/doc/nvim-tree-lua.txt) for default key mappings. A few keys add for convenience:

1. Navigation:
   - `h` **🅽** - Collapse directory.
   - `l` **🅽** - Expand directory or open file.
2. Copy/paste/cut:
   - `C` **🅽** - Copy file/directory into an internal clipboard, just like in Windows ctrl+c.
   - `X` **🅽** - Cut file/directory into an internal clipboard, just like in Windows ctrl+x.
   - `V` **🅽** - Paste file/directory from an internal clipboard to current directory, just like in Windows ctrl+v.
3. Adjust width:
   - `<M-.>`/`<M-Right>`/`<C-.>`/`<C-Right>` **🅽** - Make explorer bigger size.
   - `<M-,>`/`<M-Left>`/`<C-,>`/`<C-Left>` **🅽** - Make explorer smaller size.

Configure these key mappings in _~/.vim/repository/kyazdani42/nvim-tree.lua.vim_.

### Tabline

Support by [barbar.nvim](https://github.com/romgrk/barbar.nvim).

1. Navigation:
   - `<Leader>bn`/`<M-.>`/`<C-.>`/`<M-Right>`/`<C-Right>` **🅽** - Go to next(👉) buffer.
   - `<Leader>bp`/`<M-,>`/`<C-,>`/`<M-Left>`/`<C-Left>` **🅽** - Go to previous(👈) buffer.
   - `<Leader>bd` **🅽** - Close current buffer without closing vim window.
   - `<M-1>`/`<C-1>` **🅽** - Go to buffer-1.
   - `<M-2>`/`<C-2>` **🅽** - Go to buffer-2.
   - `<M-3>`/`<C-3>` **🅽** - Go to buffer-3.
   - `<M-4>`/`<C-4>` **🅽** - Go to buffer-4.
   - `<M-5>`/`<C-5>` **🅽** - Go to buffer-5.
   - `<M-6>`/`<C-6>` **🅽** - Go to buffer-6.
   - `<M-7>`/`<C-7>` **🅽** - Go to buffer-7.
   - `<M-8>`/`<C-8>` **🅽** - Go to buffer-8.
   - `<M-9>`/`<C-9>` **🅽** - Go to buffer-9.
   - `<M-0>`/`<C-0>` **🅽** - Go to the last buffer.
2. Re-order:
   - `<M-S-Right>`/`<C-S-Right>` **🅽** - Re-order(move) current buffer to next(👉) position.
   - `<M-S-Left>`/`<C-S-Left>` **🅽** - Re-order(move) current buffer to previous(👈) position.
3. Mouse:
   - `<LeftMouse>` **🅽** - Go to target buffer.
   - `<MiddleMouse>` **🅽** - Close target buffer.

{: .note-title}

> Notice
>
> On different platforms, terminals and GUI clients, a few ctrl+?/alt+?/meta+? keys could be overwritten by app. Please try all the ways to make sure of the availability.

### GUI Font

[Hack Nerd Font Mono](https://github.com/ryanoasis/nerd-fonts/releases) is enabled by default.

Install other nerd fonts and configure in _~/.vim/settings.vim_ to customize.

## IDE-like Editing Features

Supported by:

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

### Code Complete

- `<C-n>`/`<Down>` **🅸** - Navigate to next(👇) suggestion.
- `<C-p>`/`<Up>` **🅸** - Navigate to previous(👆) suggestion.
- `<C-u>` **🅸** - Scroll up(👆) the suggestion docs.
- `<C-d>` **🅸** - Scroll down(👇) the suggestion docs.
- `<TAB>`/`<CR>` **🅸** - Confirm current suggestion.
- `<ESC>`/`<C-[>` **🅸** - Close suggestion.
- `<C-f>` **🅸** - Navigate to next(👉) snippet placeholder.
- `<C-b>` **🅸** - Navigate to previous(👈) snippet placeholder.

### Symbols

- `gd` **🅽** - Go to definition.
- `gD` **🅽** - Go to declaration.
- `gt` **🅽** - Go to type definition.
- `gi` **🅽** - Go to implemention.
- `gr` **🅽** - Go to references.
- `K` **🅽** - Show hover information.
- `<C-k>` **🅽** - Show signature help.
- `<Leader>rs` **🅽** - Rename symbol.

### Diagnostics

- `[d` **🅽** - Go to previous(👆) diagnostic location.
- `]d` **🅽** - Go to next(👇) diagnostic location.

### Code Format

Code format runs on file save asynchronous by default.

If you need to forcibly trigger code format, please use below synchronous code format:

- `<Leader>cf` **🅽** - Format code on whole buffer.
- `<Leader>cf` **🆅** - Format selected code.

If you need to save file without code format, please use:

- `:noa w` **🅽** - Save file without _vim's autocmd_.

### Code Actions

- `<Leader>ca` **🅽** - Run code actions under cursor.
- `<Leader>ca` **🆅** - Run code actions on selected code.

### Git

- `]c` **🅽** - Go to next(👇) git chunk in current buffer.
- `[c` **🅽** - Go to previous(👆) git chunk in current buffer.
- `<Leader>gb` **🅽** - Toggle git blame info on current line.

### Manage LSP Servers

By default, [a bunch of language servers](/lin.nvim.dev/appendix/#embedded-language-servers) are already embedded. But sooner or later you need to manage these LSP servers yourself.

LSP server manager is supported by [mason.nvim](https://github.com/williamboman/mason.nvim). Please try `:Mason` command in neovim for more information.

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

---

## Next

- See [Embedded LSP Servers](/lin.nvim.dev/appendix/#embedded-lsp-servers).
- See [Embedded Formatters/Linters](/lin.nvim.dev/appendix/#embedded-formatters-linters).
- See [Plugin List](/lin.nvim.dev/appendix/#plugins).
