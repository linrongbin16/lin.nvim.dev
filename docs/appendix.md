---
layout: default
title: Appendix
nav_order: 5
---

# Appendix

---

- [Dependencies](#dependencies)
- [Plugins](#plugins)
  - [Infrastructure](#infrastructure)
  - [Color Scheme](#color-scheme)
  - [Highlight](#highlight)
  - [UI](#ui)
  - [Search Engine](#search-engine)
  - [Tags](#tags)
  - [LSP](#lsp)
  - [Specific Language Support](#specific-language-support)
  - [Editing Enhancement](#editing-enhancement)
- [LSP Servers](#lsp-servers)
- [Reference](#reference)

---

## Dependencies

- [Git](https://git-scm.com/).
- [Neovim](https://github.com/neovim/neovim/wiki/Installing-Neovim).
- Programming languages:
  - C/C++ tool chain([clang](https://clang.llvm.org/)/[gcc](https://gcc.gnu.org/), [make](https://www.gnu.org/software/make/), [pkg-config](https://www.freedesktop.org/wiki/Software/pkg-config/), [autoconf](https://www.gnu.org/software/autoconf/), [automake](https://www.gnu.org/software/automake/) and [cmake](https://cmake.org/)).
  - [Python3](https://www.python.org/)(python2 is not supported) and some pip packages([pynvim](https://pypi.org/project/pynvim/), [click](https://pypi.org/project/click/)).
  - [Node.js](https://nodejs.org/) and some npm packages([neovim](https://www.npmjs.com/package/neovim)).
- Download tools: [curl](https://curl.se/), [wget](https://www.gnu.org/software/wget/).
- Unzip tools: [unzip](https://linux.die.net/man/1/unzip), [gzip](https://www.gnu.org/software/gzip/), [7-zip](https://www.7-zip.org/).
- Tags: [universal-ctags](https://github.com/universal-ctags/ctags).
- Modern commands written in rust: [rg](https://github.com/BurntSushi/ripgrep), [fd](https://github.com/sharkdp/fd), [bat](https://github.com/sharkdp/bat), [delta](https://github.com/dandavison/delta).
- Patched-fonts: [hack nerd font](https://github.com/ryanoasis/nerd-fonts/releases/latest).

---

## Plugins

### Infrastructure

- [folke/lazy.nvim](https://github.com/folke/lazy.nvim)
- [nathom/filetype.nvim](https://github.com/nathom/filetype.nvim)
- [nvim-lua/plenary.nvim](https://github.com/nvim-lua/plenary.nvim)

### Color Scheme

{: .important-title}

> Notice
>
> Option `--no-color` could disable all these plugins.

- [bluz71/vim-nightfly-colors](https://github.com/bluz71/vim-nightfly-colors)
- [bluz71/vim-moonfly-colors](https://github.com/bluz71/vim-moonfly-colors)
- [catppuccin/nvim](https://github.com/catppuccin/nvim)
- [challenger-deep-theme/vim](https://github.com/challenger-deep-theme/vim)
- [cocopon/iceberg.vim](https://github.com/cocopon/iceberg.vim)
- [EdenEast/nightfox.nvim](https://github.com/EdenEast/nightfox.nvim)
- [embark-theme/vim](https://github.com/embark-theme/vim)
- [fenetikm/falcon](https://github.com/fenetikm/falcon)
- [folke/tokyonight.nvim](https://github.com/folke/tokyonight.nvim)
- [ishan9299/nvim-solarized-lua](https://github.com/ishan9299/nvim-solarized-lua)
- [junegunn/seoul256.vim](https://github.com/junegunn/seoul256.vim)
- [luisiacc/gruvbox-baby](https://github.com/luisiacc/gruvbox-baby)
- [marko-cerovac/material.nvim](https://github.com/marko-cerovac/material.nvim)
- [mhartington/oceanic-next](https://github.com/mhartington/oceanic-next)
- [Mofiqul/dracula.nvim](https://github.com/Mofiqul/dracula.nvim)
- [navarasu/onedark.nvim](https://github.com/navarasu/onedark.nvim)
- [NLKNguyen/papercolor-theme](https://github.com/NLKNguyen/papercolor-theme)
- [pineapplegiant/spaceduck](https://github.com/pineapplegiant/spaceduck)
- [preservim/vim-colors-pencil](https://github.com/preservim/vim-colors-pencil)
- [projekt0n/github-nvim-theme](https://github.com/projekt0n/github-nvim-theme)
- [raphamorim/lucario](https://github.com/raphamorim/lucario)
- [rebelot/kanagawa.nvim](https://github.com/rebelot/kanagawa.nvim)
- [Rigellute/rigel](https://github.com/Rigellute/rigel)
- [romainl/Apprentice](https://github.com/romainl/Apprentice)
- [rose-pine/neovim](https://github.com/rose-pine/neovim)
- [sainnhe/edge](https://github.com/sainnhe/edge)
- [sainnhe/everforest](https://github.com/sainnhe/everforest)
- [sainnhe/sonokai](https://github.com/sainnhe/sonokai)
- [shaunsingh/nord.nvim](https://github.com/shaunsingh/nord.nvim)
- [srcery-colors/srcery-vim](https://github.com/srcery-colors/srcery-vim)

### Highlight

{: .important-title}

> Notice
>
> Option `--no-hilight` could disable all these plugins.

- [RRethy/vim-illuminate](https://github.com/RRethy/vim-illuminate)
- [NvChad/nvim-colorizer.lua](https://github.com/NvChad/nvim-colorizer.lua)
- [andymass/vim-matchup](https://github.com/andymass/vim-matchup)
- [lfv89/vim-interestingwords](https://github.com/lfv89/vim-interestingwords)
- [haya14busa/is.vim](https://github.com/haya14busa/is.vim)
- [winston0410/range-highlight.nvim](https://github.com/winston0410/range-highlight.nvim)
- [winston0410/cmd-parser.nvim](https://github.com/winston0410/cmd-parser.nvim)

### UI

- [nvim-neo-tree/neo-tree.nvim](https://github.com/nvim-neo-tree/neo-tree.nvim)
- [MunifTanjim/nui.nvim](https://github.com/MunifTanjim/nui.nvim)
- [nvim-tree/nvim-web-devicons](https://github.com/nvim-tree/nvim-web-devicons)
- [akinsho/bufferline.nvim](https://github.com/akinsho/bufferline.nvim)
- [moll/vim-bbye](https://github.com/moll/vim-bbye)
- [lukas-reineke/indent-blankline.nvim](https://github.com/lukas-reineke/indent-blankline.nvim)
- [nvim-lualine/lualine.nvim](https://github.com/nvim-lualine/lualine.nvim)
- [linrongbin16/lsp-progress.nvim](https://github.com/linrongbin16/lsp-progress.nvim)
- [itchyny/vim-gitbranch](https://github.com/itchyny/vim-gitbranch)
- [airblade/vim-gitgutter](https://github.com/airblade/vim-gitgutter)
- [f-person/git-blame.nvim](https://github.com/f-person/git-blame.nvim)
- [akinsho/toggleterm.nvim](https://github.com/akinsho/toggleterm.nvim)
- [stevearc/dressing.nvim](https://github.com/stevearc/dressing.nvim)

### Search Engine

- [junegunn/fzf](https://github.com/junegunn/fzf)
- [junegunn/fzf.vim](https://github.com/junegunn/fzf.vim)
- [ojroques/nvim-lspfuzzy](https://github.com/ojroques/nvim-lspfuzzy)

### Tags

{: .important-title}

> Notice
>
> Option `--no-lang` could disable all these plugins.

- [liuchengxu/vista.vim](https://github.com/liuchengxu/vista.vim)
- [ludovicchabant/vim-gutentags](https://github.com/ludovicchabant/vim-gutentags)

### LSP

{: .important-title}

> Notice
>
> Option `--no-lang` could disable all these plugins.

- [williamboman/mason.nvim](https://github.com/williamboman/mason.nvim)
- [williamboman/mason-lspconfig.nvim](https://github.com/williamboman/mason-lspconfig.nvim)
- [neovim/nvim-lspconfig](https://github.com/neovim/nvim-lspconfig)
- [p00f/clangd_extensions.nvim](https://github.com/p00f/clangd_extensions.nvim)
- [jose-elias-alvarez/null-ls.nvim](https://github.com/jose-elias-alvarez/null-ls.nvim)
- [jay-babu/mason-null-ls.nvim](https://github.com/jay-babu/mason-null-ls.nvim)
- [hrsh7th/nvim-cmp](https://github.com/hrsh7th/nvim-cmp)
- [hrsh7th/cmp-nvim-lsp](https://github.com/hrsh7th/cmp-nvim-lsp)
- [hrsh7th/cmp-buffer](https://github.com/hrsh7th/cmp-buffer)
- [hrsh7th/cmp-path](https://github.com/hrsh7th/cmp-path)
- [hrsh7th/cmp-cmdline](https://github.com/hrsh7th/cmp-cmdline)
- [L3MON4D3/LuaSnip](https://github.com/L3MON4D3/LuaSnip)
- [saadparwaiz1/cmp_luasnip](https://github.com/saadparwaiz1/cmp_luasnip)

### Specific Language Support

{: .important-title}

> Notice
>
> Option `--no-lang` could disable all these plugins.

- [iamcco/markdown-preview.nvim](https://github.com/iamcco/markdown-preview.nvim)
- [justinmk/vim-syntax-extra](https://github.com/justinmk/vim-syntax-extra)
- [rhysd/vim-llvm](https://github.com/rhysd/vim-llvm)
- [zebradil/hive.vim](https://github.com/zebradil/hive.vim)
- [slim-template/vim-slim](https://github.com/slim-template/vim-slim)

### Editing Enhancement

{: .important-title}

> Notice
>
> Option `--no-edit` could disable all these plugins.

- [phaazon/hop.nvim](https://github.com/phaazon/hop.nvim)
- [ggandor/leap.nvim](https://github.com/ggandor/leap.nvim)
- [windwp/nvim-autopairs](https://github.com/windwp/nvim-autopairs)
- [alvan/vim-closetag](https://github.com/alvan/vim-closetag)
- [numToStr/Comment.nvim](https://github.com/numToStr/Comment.nvim)
- [tpope/vim-repeat](https://github.com/tpope/vim-repeat)
- [kylechui/nvim-surround](https://github.com/kylechui/nvim-surround)
- [mbbill/undotree](https://github.com/mbbill/undotree)
- [editorconfig/editorconfig-vim](https://github.com/editorconfig/editorconfig-vim)

## LSP Servers

- Bash: bashls(macOS/Linux only)
- C/C++: clangd
- CMake: cmake
- CSS: cssls, cssmodules_ls
- HTML: html
- JSON: jsonls
- Javascript/typescript: tsserver
- Lua: sumneko_lua
- PowerShell: powershell_es(Windows only)
- Python: pyright
- Yaml: yamlls
- Vim: vimls
- XML: lemminx

Null-ls sources:

- Bash: shfmt(macOS/Linux only)
- Javascript/typescript: prettierd, eslint_d
- Lua: stylua
- Python: black, isort

## Reference

- [mason.nvim - Mason Package Index](https://github.com/williamboman/mason.nvim/blob/main/PACKAGES.md)
- [mason-lspconfig.nvim - Available LSP servers](https://github.com/williamboman/mason-lspconfig.nvim#available-lsp-servers)
- [mason-null-ls.nvim - Available Null-ls sources](https://github.com/jay-babu/mason-null-ls.nvim#available-null-ls-sources)
- [null-ls.nvim - Built-in Sources](https://github.com/jose-elias-alvarez/null-ls.nvim/blob/main/doc/BUILTINS.md#built-in-sources)
