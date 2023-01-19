---
layout: default
title: Appendix
nav_order: 5
---

# Appendix

- [Dependencies](#dependencies)
- [Plugins](#plugins)
  - [Infrastructure](#infrastructure)
  - [Color Scheme](#color-scheme)
  - [Highlight](#highlight)
  - [UI](#ui)
  - [Tags](#tags)
  - [Search Engine](#search-engine)
  - [LSP](#lsp)
  - [Specific Language Support](#specific-language-support)
  - [Editing Enhancement](#editing-enhancement)
- [LSP Servers](#lsp-servers)
- [Extra Formatter/Linter/Diagnostic/CodeAction](#extra-formatterlinterdiagnosticcodeaction)
- [Reference](#reference)

## Dependencies

- [Git](https://git-scm.com/).
- [Neovim](https://github.com/neovim/neovim/wiki/Installing-Neovim).
- C/C++ tool chain([clang](https://clang.llvm.org/)/[gcc](https://gcc.gnu.org/), [make](https://www.gnu.org/software/make/), [pkg-config](https://www.freedesktop.org/wiki/Software/pkg-config/), [autoconf](https://www.gnu.org/software/autoconf/), [automake](https://www.gnu.org/software/automake/) and [cmake](https://cmake.org/)).
- [Python3](https://www.python.org/)(python2 is not supported) and some pip packages([pynvim](https://pypi.org/project/pynvim/), [click](https://pypi.org/project/click/)).
- [Node.js](https://nodejs.org/) and some npm packages([neovim](https://www.npmjs.com/package/neovim)).
- [Rust](https://www.rust-lang.org/) and some modern commands([fd](https://github.com/sharkdp/fd), [rg](https://github.com/BurntSushi/ripgrep), [bat](https://github.com/sharkdp/bat)).
- [Curl](https://curl.se/), [wget](https://www.gnu.org/software/wget/), [unzip](https://linux.die.net/man/1/unzip) and [gzip](https://www.gnu.org/software/gzip/).
- [Universal-ctags](https://github.com/universal-ctags/ctags).
- [Hack nerd font](https://github.com/ryanoasis/nerd-fonts/releases/download/v2.2.2/Hack.zip).

---

## Plugins

### Infrastructure

- [wbthomason/packer.nvim](https://github.com/wbthomason/packer.nvim)
- [nathom/filetype.nvim](https://github.com/nathom/filetype.nvim)
- [lewis6991/impatient.nvim](https://github.com/lewis6991/impatient.nvim)
- [neovim/nvim-lspconfig](https://github.com/neovim/nvim-lspconfig)

### Color Scheme

{: .note-title}

> Notice
>
> Option `--no-color` could disable all these plugins.

- [bluz71/vim-moonfly-colors](https://github.com/bluz71/vim-moonfly-colors)
- [bluz71/vim-nightfly-colors](https://github.com/bluz71/vim-nightfly-colors)
- [catppuccin/nvim](https://github.com/catppuccin/nvim)
- [challenger-deep-theme/vim](https://github.com/challenger-deep-theme/vim)
- [cocopon/iceberg.vim](https://github.com/cocopon/iceberg.vim)
- [EdenEast/nightfox.nvim](https://github.com/EdenEast/nightfox.nvim)
- [embark-theme/vim](https://github.com/embark-theme/vim)
- [fenetikm/falcon](https://github.com/fenetikm/falcon)
- [folke/tokyonight.nvim](https://github.com/folke/tokyonight.nvim)
- [ishan9299/nvim-solarized-lua](https://github.com/ishan9299/nvim-solarized-lua)
- [junegunn/seoul256.vim](https://github.com/junegunn/seoul256.vim)
- [KeitaNakamura/neodark.vim](https://github.com/KeitaNakamura/neodark.vim)
- [luisiacc/gruvbox-baby](https://github.com/luisiacc/gruvbox-baby)
- [marko-cerovac/material.nvim](https://github.com/marko-cerovac/material.nvim)
- [mhartington/oceanic-next](https://github.com/mhartington/oceanic-next)
- [Mofiqul/dracula.nvim](https://github.com/Mofiqul/dracula.nvim)
- [navarasu/onedark.nvim](https://github.com/navarasu/onedark.nvim)
- [NLKNguyen/papercolor-theme](https://github.com/NLKNguyen/papercolor-theme)
- [olimorris/onedarkpro.nvim](https://github.com/olimorris/onedarkpro.nvim)
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
- [sonph/onehalf](https://github.com/sonph/onehalf)
- [srcery-colors/srcery-vim](https://github.com/srcery-colors/srcery-vim)

### Highlight

{: .note-title}

> Notice
>
> Option `--no-hilight` could disable all these plugins.

- [RRethy/vim-illuminate](https://github.com/RRethy/vim-illuminate)
- [NvChad/nvim-colorizer.lua](https://github.com/NvChad/nvim-colorizer.lua)
- [andymass/vim-matchup](https://github.com/andymass/vim-matchup)
- [inkarkat/vim-mark](https://github.com/inkarkat/vim-mark)

### UI

- [romgrk/barbar.nvim](https://github.com/romgrk/barbar.nvim)
- [nvim-tree/nvim-tree.lua](https://github.com/nvim-tree/nvim-tree.lua)
- [jlanzarotta/bufexplorer](https://github.com/jlanzarotta/bufexplorer)
- [lukas-reineke/indent-blankline.nvim](https://github.com/lukas-reineke/indent-blankline.nvim)
- [nvim-lualine/lualine.nvim](https://github.com/nvim-lualine/lualine.nvim)
- [nvim-lua/lsp-status.nvim](https://github.com/nvim-lua/lsp-status.nvim)
- [lewis6991/gitsigns.nvim](https://github.com/lewis6991/gitsigns.nvim)
- [akinsho/toggleterm.nvim](https://github.com/akinsho/toggleterm.nvim)

### Tags

- [liuchengxu/vista.vim](https://github.com/liuchengxu/vista.vim)
- [ludovicchabant/vim-gutentags](https://github.com/ludovicchabant/vim-gutentags)

### Search Engine

- [junegunn/fzf](https://github.com/junegunn/fzf)
- [junegunn/fzf.vim](https://github.com/junegunn/fzf.vim)
- [ojroques/nvim-lspfuzzy](https://github.com/ojroques/nvim-lspfuzzy)

### LSP

{: .note-title}

> Notice
>
> Option `--no-lang` could disable all these plugins.

- [williamboman/mason.nvim](https://github.com/williamboman/mason.nvim)
- [williamboman/mason-lspconfig.nvim](https://github.com/williamboman/mason-lspconfig.nvim)
- [jose-elias-alvarez/null-ls.nvim](https://github.com/jose-elias-alvarez/null-ls.nvim)
- [jay-babu/mason-null-ls.nvim](https://github.com/jay-babu/mason-null-ls.nvim)
- [hrsh7th/cmp-nvim-lsp](https://github.com/hrsh7th/cmp-nvim-lsp)
- [hrsh7th/cmp-buffer](https://github.com/hrsh7th/cmp-buffer)
- [hrsh7th/cmp-path](https://github.com/hrsh7th/cmp-path)
- [hrsh7th/cmp-cmdline](https://github.com/hrsh7th/cmp-cmdline)
- [hrsh7th/nvim-cmp](https://github.com/hrsh7th/nvim-cmp)
- [L3MON4D3/LuaSnip](https://github.com/L3MON4D3/LuaSnip)
- [saadparwaiz1/cmp_luasnip](https://github.com/saadparwaiz1/cmp_luasnip)
- [rafamadriz/friendly-snippets](https://github.com/rafamadriz/friendly-snippets)

### Specific Language Support

{: .note-title}

> Notice
>
> Option `--no-lang` could disable all these plugins.

- [iamcco/markdown-preview.nvim](https://github.com/iamcco/markdown-preview.nvim)
- [p00f/clangd_extensions.nvim](https://github.com/p00f/clangd_extensions.nvim)
- # [simrat39/rust-tools.nvim](https://github.com/simrat39/rust-tools.nvim)
- [justinmk/vim-syntax-extra](https://github.com/justinmk/vim-syntax-extra)
- [rhysd/vim-llvm](https://github.com/rhysd/vim-llvm)
- [zebradil/hive.vim](https://github.com/zebradil/hive.vim)
- [slim-template/vim-slim](https://github.com/slim-template/vim-slim)

### Movement

{: .note-title}

> Notice
>
> Option `--no-edit` could disable all these plugins.

- [phaazon/hop.nvim](https://github.com/phaazon/hop.nvim)
- [ggandor/leap.nvim](https://github.com/ggandor/leap.nvim)
- [chaoren/vim-wordmotion](https://github.com/chaoren/vim-wordmotion)

### Editing Enhancement

{: .note-title}

> Notice
>
> Option `--no-edit` could disable all these plugins.

- [alvan/vim-closetag](https://github.com/alvan/vim-closetag)
- [numToStr/Comment.nvim](https://github.com/numToStr/Comment.nvim)
- [windwp/nvim-autopairs](https://github.com/windwp/nvim-autopairs)
- [haya14busa/is.vim](https://github.com/haya14busa/is.vim)
- [tpope/vim-repeat](https://github.com/tpope/vim-repeat)
- [mbbill/undotree](https://github.com/mbbill/undotree)
- [editorconfig/editorconfig-vim](https://github.com/editorconfig/editorconfig-vim)

---

## LSP Servers

- Bash: bashls(only for macOS/Linux)
- C/C++: clangd
- CMake: cmake
- CSS: cssls, cssmodules_ls
- HTML: html
- JSON: jsonls
- Javascript/typescript/etc: tsserver
- Lua: sumneko_lua
- PowerShell: powershell_es(only for Windows)
- Python: pyright
- Rust: rust_analyzer
- Yaml: yamlls
- Vim: vimls
- XML: lemminx

---

## Extra Formatter/Linter/Diagnostic/CodeAction

- Bash: shfmt(only for macOS/Linux)
- Javascript/typescript: prettierd, eslint_d
- Python: black, isort

---

## Reference

- [mason.nvim - Mason Package Index](https://github.com/williamboman/mason.nvim/blob/main/PACKAGES.md)
- [mason-lspconfig.nvim - Available LSP servers](https://github.com/williamboman/mason-lspconfig.nvim#available-lsp-servers)
- [mason-null-ls.nvim - Available Null-ls sources](https://github.com/jay-babu/mason-null-ls.nvim#available-null-ls-sources)
- [null-ls.nvim - Built-in Sources](https://github.com/jose-elias-alvarez/null-ls.nvim/blob/main/doc/BUILTINS.md#built-in-sources)
