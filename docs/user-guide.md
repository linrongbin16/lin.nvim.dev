---
layout: default
title: User Guide
nav_order: 4
has_children: true
has_toc: false
---

<!-- markdownlint-disable MD013 MD025 -->

# User Guide

---

- [Principle](#principle)
- [Terms](#terms)
- [Key Mappings](#key-mappings)
  - [Hot Keys](#hot-keys)
  - [Ctrl+? Cmd+? Keys](#ctrl-cmd-keys)
  - [Biscuits](#biscuits)
- [UI](#ui)
  - [File Explorer](#file-explorer)
  - [Tabline](#tabline)
  - [Highlight Words](#highlight-words)
  - [GUI Font](#gui-font)
- [IDE Features](#ide-features)
  - [Auto-Complete](#auto-complete)
  - [Navigation](#navigation)
  - [Symbols](#symbols)
  - [Diagnostics](#diagnostics)
  - [Code Format](#code-format)
  - [Code Actions](#code-actions)
- [Search](#search)
  - [Text Search](#text-search)
  - [File Search](#file-search)
  - [History Search](#history-search)
  - [Git Search](#git-search)
  - [Vim Search](#vim-search)
- [Editing Enhancement](#editing-enhancement)
  - [Key Bindings](#key-bindings)
  - [Cursor Motion](#cursor-motion)
  - [Git](#git)
  - [Easy Comment](#easy-comment)
  - [Better Repeat](#better-repeat)
  - [Better Matching](#better-matching)
  - [Auto Pair/Close/End](#auto-pair-close-end)
- [Customization](#customization)

---

## Principle

### Key Mapping

1. First letter of each words as a mapping sequence, unless it conflicts.
2. Same prefix for same functionality.
3. Shorter keys for higher frequency.
4. Map less editing modes(mostly normal mode), unless it makes sense.
5. Following classic, popular behavior, or plugin author's recommendation.

Specifically, we have below rules:

- `<Leader>` as a prefix for commands.
- `<Space>` as a prefix for fzf commands.
- `g` as a prefix for LSP navigations.
- `]`/`[` as prefix for next/previous navigations.
- `.`/`,`(or `>`/`<`) for right/left(or down/up) directions.
- Capitalized last letter for a command bang, or a lower frequency variant.

---

## Terms

In this section, vim editing modes are specified with:

<!-- alphabet emoji: https://emojicombos.com/emoji-letters -->
<!-- complete emoji list: https://dev.to/nikolab/complete-list-of-github-markdown-emoji-markup-5aia -->
<!-- complete emoji list 2: https://gist.github.com/rxaviers/7360908 -->

- 🄽 - Normal mode.
- 🅅 - Visual/select mode.
- 🅇 - Visual mode.
- 🅂 - Select mode.
- 🄾 - Operator-pending mode.
- 🄸 - Insert mode.
- 🄻 - Command-line mode.

Meta-key (_M_), alt-key (_A_) on Windows/Linux, and command-key (_D_) on macOS are collectively represented by:

- _M_

---

## Key Mappings

### Hot Keys

- `F1` 🄽 - Toggle file explorer.
- `F2` 🄽 - Toggle undo-tree.
- `F3` 🄽 - Toggle structure outlines(tags).
- `F4` 🄽 - Switch between C/C++ header and source.
- `F9` 🄽 - Open markdown preview.
- `F10` 🄽 - Toggle terminal.

### Ctrl+? Cmd+? Keys

Ctrl+? follows the classic behavior under Windows:

- `<C-a>` 🄽 🅅 🄸 - Select all.
- `<C-c>` 🄽 🅅 🄸 - Copy to clipboard.
- `<C-x>` 🄽 🅅 🄸 - Cut to clipboard.
- `<C-v>` 🄽 🅅 🄸 - Paste from clipboard.
- `<C-s>` 🄽 🅅 🄸 - Save file.
- `<C-y>` 🄽 🅅 🄸 - Redo.
- `<C-z>` 🄽 🅅 🄸 - Undo.
- `<C-q>` 🄽 - Switch to block-visual mode, same as vim's original _ctrl+v_ (since we mapped it to paste).

For macOS, cmd+? follows the same behavior(ctrl+? works as well):

- `<D-a>` 🄽 🅅 🄸 - Same as `<C-a>`.
- `<D-c>` 🄽 🅅 🄸 - Same as `<C-c>`.
- `<D-x>` 🄽 🅅 🄸 - Same as `<C-x>`.
- `<D-v>` 🄽 🅅 🄸 - Same as `<C-v>`.
- `<D-s>` 🄽 🅅 🄸 - Same as `<C-s>`.
- `<D-y>` 🄽 🅅 🄸 - Same as `<C-y>`.
- `<D-z>` 🄽 🅅 🄸 - Same as `<C-z>`.

### Biscuits

Plugins:

- `<Leader>ms` 🄽 - `:Mason<CR>`.
- `<Leader>lz` 🄽 - `:Lazy<CR>`.
- `<Leader>wk` 🄽 - `:WhichKey`.
- `<Leader>gd` 🄽 - `:DogeGenerate`.

Save file without formatting:

- `<Leader>ww` 🄽 - Save file without formatting, e.g.`:noa w<CR>`.

Quit:

- `<Leader>qt` 🄽 - `:quit<CR>`.
- `<Leader>qT` 🄽 - `:quit!<CR>`.
- `<Leader>qa` 🄽 - `:qall<CR>`.
- `<Leader>qA` 🄽 - `:qall!<CR>`.

Folding:

- `<Leader>zz` 🄽 - Toggle folding.

Copy/paste across different vim instances through remote ssh could be difficult, introduce two shortcuts using local cache:

- `<Leader>y` 🅇 - Copy selected text to _~/.nvim/.copypaste_.
- `<Leader>p` 🄽 - Paste from _~/.nvim/.copypaste_ to current cursor.

{: .note}

> View all key mappings with:
>
> - 🄽 - `:WhichKey`.
> - 🅅 - `:WhichKey '' v`.
> - 🄸 - `:WhichKey '' i`.
>
> Configure these key mappings in _~/.nvim/settings.vim_.

---

## UI

### File Explorer

Supported by [nvim-tree.lua](https://github.com/nvim-tree/nvim-tree.lua).
Please use _g?_ to toggle help in nvim-tree, or refer to nvim-tree's default key mappings: `:h nvim-tree-mappings`.

A few keys are added for convenience:

- `h` 🄽 - Collapse current directory.
- `l` 🄽 - Expand directory or open file.
- `]d` 🄽 - Next(👉) diagnostic item.
- `[d` 🄽 - Previous(👈) diagnostic item.
- `<Leader>.`/`<Leader>,` 🄽 - Resize explorer width bigger/smaller.

A few keys are removed:

- `]e` 🄽 - Next(👉) diagnostic item, replaced by `]d`.
- `[e` 🄽 - Previous(👈) diagnostic item, replaced by `[d`.

### Tabline

Supported by [bufferline.nvim](https://github.com/akinsho/bufferline.nvim) and [vim-bbye](https://github.com/moll/vim-bbye).

1. Navigation:
   - `<Leader>1` ~ `<Leader>9` 🄽 - Go to buffer-1 ~ buffer-9.
   - `<Leader>0` 🄽 - Go to the last buffer.
   - `]b` 🄽 - Go to next(👉) buffer.
   - `[b` 🄽 - Go to previous(👈) buffer.
   - `<Leader>bd` 🄽 - Close current buffer by `:Bdelete`.
   - `<Leader>bD` 🄽 - Forcibly close current buffer by `:Bdelete!`.
2. Move/re-order:
   - `<Leader>.`/`<Leader>,` 🄽 - Move(re-order) current buffer to next(👉)/previous(👈) position.
3. Mouse:
   - `<LeftMouse>` 🄽 - Go to target buffer.
   - `<RightMouse>` 🄽 - Close target buffer.

### Highlight Words

Highlight words with different colors, supported by [vim-mark](https://github.com/inkarkat/vim-mark).

All keys are mapped with prefix `<Leader>h` to avoid key conflicts with other plugins:

- `<Leader>hw` 🄽 🅅 - Highlight/unhighlight cursor word.
- `<Leader>hW` 🄽 - Clear all highlighting words.
- `<Leader>hn` 🄽 - Navigate to next(👇) highlighting word.
- `<Leader>hN` 🄽 - Navigate to previous(👆) highlighting word.

### GUI Font

Patched-fonts [Hack Nerd Font Mono](https://github.com/ryanoasis/nerd-fonts/releases) is enabled by default.

{: .note}

> Configure GUI font in _~/.nvim/settings.vim_.

---

## IDE Features

Supported by [nvim-cmp](https://github.com/hrsh7th/nvim-cmp), [null-ls.nvim](https://github.com/jose-elias-alvarez/null-ls.nvim) and many other plugins.
Please see [Manage LSP Servers](/lin.nvim.dev/docs/manage-lsp-servers) for more details.

### Auto-Complete

- `<C-n>`/`<Down>` 🄸 - Navigate to next(👇) suggestion.
- `<C-p>`/`<Up>` 🄸 - Navigate to previous(👆) suggestion.
- `<C-u>` 🄸 - Scroll up(👆) the suggestion docs.
- `<C-d>` 🄸 - Scroll down(👇) the suggestion docs.
- `<TAB>`/`<CR>` 🄸 - Confirm current suggestion.
- `<ESC>`/`<C-[>` 🄸 - Close suggestion.
- `<C-f>` 🄸 - Navigate to next(👉) snippet placeholder.
- `<C-b>` 🄸 - Navigate to previous(👈) snippet placeholder.

### Navigation

Navigate with a preview window, supported by [glance.nvim](https://github.com/DNLHC/glance.nvim).

A few keys are changed for convenience:

1. List window:
   - `s`(jump in split) 🄽 - Re-mapped to `<C-s>`.
   - `v`(jump in vsplit) 🄽 - Re-mapped to `<C-v>`.
   - `t`(jump in new tab) 🄽 - Re-mapped to `<C-t>`.
   - `Q`(close window) 🄽 - Removed for duplicated with `q`.
2. Preview window:
   - `<Tab>`/`<S-Tab>`(jump to next/previous location) 🄽 - Removed, you need to go back to list window before jump to other locations.
   - `Q`(close window) 🄽 - Re-mapped to `q`.

### Symbols

- `K` 🄽 - Show hover information.
- `<C-k>` 🄽 - Show signature help.
- `<Leader>rn` 🄽 - Rename symbol.

### Diagnostics

- `[d` 🄽 - Go to previous(👆) diagnostic location.
- `]d` 🄽 - Go to next(👇) diagnostic location.
- `[e` 🄽 - Go to previous(👆) error location.
- `]e` 🄽 - Go to next(👇) error location.
- `[w` 🄽 - Go to previous(👆) warning location.
- `]w` 🄽 - Go to next(👇) warning location.
- `<Leader>dc` 🄽 - Show diagnostic under cursor.
  <!-- - `<Leader>ds` 🄽 - Show diagnostics in current buffer. -->
  <!-- - `<Leader>da` 🄽 - Show all diagnostics. -->

### Code Format

Code format runs on file save asynchronous by default. To forcibly trigger code format:

- `<Leader>cf` 🄽 🅇 - Synchronously format code in current buffer(normal mode) or selected code(visual mode).
- `<Leader>ww` 🄽 - Save file without formatting, e.g.`:noa w<CR>`.

### Code Actions

- `<Leader>ca` 🄽 🅇 - Run code actions under cursor(normal mode) or in selected code(visual mode).

{: .note}

> Configure these key mappings in _~/.nvim/lua/conf/lsp.lua_.

---

## Search

Supported by [fzf.vim](https://github.com/junegunn/fzf.vim). All fzf commands are renamed with the prefix `Fzf`, for example `:Files` are renamed to `:FzfFiles`, `:Rg` are renamed to `:FzfRg`.

### Text Search

- `<Space>r` 🄽 - Live grep by `FzfRg`, by default filter ignored and hidden files.
  - `<Space>ur` 🄽 - Unrestricted(`--no-ignore --hidden`) live grep by `FzfUnrestrictedRg`.
  - `<Space>pr` 🄽 - Precise(no fuzzy) live grep by `FzfPrecisedRg`.
  - `<Space>upr` 🄽 - Unrestricted(`--no-ignore --hidden`) precise(no fuzzy) live grep by `FzfUnrestrictedPrecisedRg`.
  - `<Space>wr` 🄽 - Search cursor word by `FzfCWordRg`, by default filter ignored and hidden files.
  - `<Space>uwr` 🄽 - Unrestricted(`--no-ignore --hidden`) search cursor word by `FzfUnrestrictedCWordRg`.
- `<Space>ln` 🄽 - Search lines in current buffer by `FzfLines`.
- `<Space>tg` 🄽 - Search tags by `FzfTags`.

### File Search

- `<Space>f` 🄽 - Search files by `FzfFiles`, by default filter ignored and hidden files.
  - `<Space>uf` 🄽 - Unrestricted(`--no-ignore --hidden`) search files by `FzfUnrestrictedFiles`.
  - `<Space>wf` 🄽 - Search files by cursor word by `FzfCWordFiles`.
  - `<Space>uwf` 🄽 - Unrestricted(`--no-ignore --hidden`) search files by cursor word by `FzfUnrestrictedCWordFiles`.
- `<Space>b` 🄽 - Search opened buffers by `FzfBuffers`.
- `<Space>hf` 🄽 - Search history files (v:oldfiles) and opened buffers by `FzfHistory`.

### History Search

- `<Space>hs` 🄽 - Search searching history(`/` in command line) by `FzfHistory/`.
- `<Space>hc` 🄽 - Search vim command history(`:` in command line) by `FzfHistory:`.

### Git Search

- `<Space>gc` 🄽 - Search git commits by `FzfCommits`.
- `<Space>gf` 🄽 - Search `git ls-files` files by `FzfGFile`.
- `<Space>gs` 🄽 - Search `git status` files by `FzfGFiles?`.

### Vim Search

- `<Space>mk` 🄽 - Search vim marks by `FzfMarks`.
- `<Space>mp` 🄽 - Search vim key mappings by `FzfMaps`.
- `<Space>cm` 🄽 - Search vim commands by `FzfCommands`.
- `<Space>ht` 🄽 - Search vim helptags by `FzfHelptags`.
- `<Space>cs` 🄽 - Search vim colorschemes by `FzfColors`.
- `<Space>tp` 🄽 - Search vim filetypes by `FzfFiletypes`.

---

---

## Editing Enhancement

### Key Bindings

Supported by [which-key.nvim](https://github.com/folke/which-key.nvim).

### Cursor Motion

Supported by [leap.nvim](https://github.com/ggandor/leap.nvim) and [hop.nvim](https://github.com/phaazon/hop.nvim).

Leap keeps its default key mappings: `s`/`S` (🄽), `x`/`X` (🅇).
While keys for hop are mapped following its predecessor [vim-easymotion](https://github.com/easymotion/vim-easymotion):

- `<Leader>f{char}` 🄽 🅇 - Move forward by a single {char}.
- `<Leader>F{char}` 🄽 🅇 - Move backward by a single {char}.
- `<Leader>s{char}{char}` 🄽 🅇 - Move forward by two consequent {char}{char}.
- `<Leader>S{char}{char}` 🄽 🅇 - Move backward by two consequent {char}{char}.
- `<Leader>wd` 🄽 🅇 - Move forward by word.
- `<Leader>wD` 🄽 🅇 - Move backward by word.
- `<Leader>ln` 🄽 🅇 - Move forward by line.
- `<Leader>lN` 🄽 🅇 - Move backward by line.

### Git

- `]c` 🄽 - Go to next(👇) git hunk in current buffer.
- `[c` 🄽 - Go to previous(👆) git hunk in current buffer.
- `<Leader>gb` 🄽 - Toggle git blame info on current line.
- `<Leader>gl`/`<Leader>gL` 🄽 🅅 - Open git link in browser/copy to clipboard.

### Easy Comment

Supported by [Comment.nvim](https://github.com/numToStr/Comment.nvim).

### Better Repeat

Better repeat(`.`) operation, supported by [vim-repeat](https://github.com/tpope/vim-repeat).

### Better Surroundings

Better operation on surroundings such as quotes/brackets, supported by [nvim-surround](https://github.com/kylechui/nvim-surround).

### Better Matching

Better matching for brackets, parentheses, HTML tags, if-endif, etc, supported by [vim-matchup](https://github.com/andymass/vim-matchup).

### Auto Pair/Close

Auto-pair braces/parentheses, auto-close html/xml tags, auto-end if-endif/function-endfunction. Supported by [nvim-autopairs](https://github.com/windwp/nvim-autopairs) and [vim-closetag](https://github.com/alvan/vim-closetag).

---

## Customization

The configs are structured as(`+` for folder, `*` for file):

```
+ ~/.nvim
  + conf                    - basic configs
  |  * basic.vim
  + deps                    - installer (third-party dependencies)
  |  * apt.sh
  |  * brew.sh
  |  * brew.sh
  + lazy (generated)        - all plugins metadata(git repository), managed by lazy.nvim
  + lua
  |  + conf                 - lua configs/utils
  |  |  * constants.lua     - global configs across multiple plugins
  |  |  * keymap.lua        - keymap utils
  |  |  * lsp.lua           - lsp configs
  |  + repo                 - plugin configs, written in lua
  |  |  + airblade
  |  |  |  + vim-gitgutter  - plugin: https://github.com/airblade/vim-gitgutter
  |  |  |  |  * keys.lua    - `keys` property for lazy
  |  |  + akinsho
  |  |  |  + bufferline-nvim
  |  |  |  |  * config.lua  - `config` property for lazy
  |  |  |  |  * keys.lua
  |  |  + junegunn
  |  |  |  + fzf-vim
  |  |  |  |  * keys.lua
  |  |  ...
  |  * lspservers.lua (generated)       - ensure installed lsp servers and lspconfig setups
  |  * plugins.lua (generated)          - plugins list, managed by lazy.nvim
  + mason (generated)       - all lsp server metadata(installed files), managed by mason.nvim
  + repo                    - plugin configs, written in vim
  |  + airblade
  |  |  + vim-gitgutter     - plugin: https://github.com/airblade/vim-gitgutter
  |  |  |  * init.vim       - `init` property for lazy
  |  ...
  |  + junegunn
  |  |  + fzf.vim           - plugin: https://github.com/junegunn/fzf.vim
  |  |  |  * config.vim     - `config` property for lazy
  |  |  |  * init.vim       - `init` property for lazy
  |  ...
  + temp                    - installer (generator templates)
  |  * colorschemes-footer.vim
  |  * colorschemes-header.vim
  |  ...
  * colorschemes.vim (generated)        - colorscheme
  * generator.py                        - installer (generator)
  * init.vim (generated)                - config entry
  * install.ps1                         - installer (for windows)
  * install.sh                          - installer (for unix)
  * LICENSE
  * README.md
  * settings.vim (generated)            - other settings
```

The config entry `init.vim` will load below components:

1. `conf/*` and `lua/conf/*` - The very basic and common configs.
2. `repo/**/*` and `lua/repo/**/*` - All plugins and their configs. Besides:
   - `lua/plugins.lua` - The plugins list. _Lazy.nvim_ use it to load all plugins and their configs.
   - `lua/lspservers.lua` - Lsp servers(and null-ls sources) list. _Mason.nvim_ use it to manage all ensure installed lsp servers and their setups.
3. `colorscheme.vim` - Colors.
4. `settings.vim` - Other settings.

Each plugin's configs are in `repo/{org}{repo}/` folder(written in vim), or `lua/repo/{org}/{repo}` folder(written in lua). Choose any one of them according to your preference.

A plugin's config contains below sections:

- `init.vim`/`init.lua` - Used by _lazy.nvim_ `init` property. Global variables defined here, executed before loading so the plugin could see them.
- `config.vim`/`config.lua` - Used by _lazy.nvim_ `config` property. Lua plugin's `setup` and other related things.
- `keys.vim`/`keys.lua` - Used by _lazy.nvim_ `keys` property. Key mappings defined here.

{: .important-title}

> Notice
>
> Since `.`(dot) in lua require means path separator, so we translate all path's `.`(dot) to `-`(hyphen) in `lua/repo`.
>
> For example: `lua/repo/junegunn/fzf-vim` and `repo/junegunn/fzf.vim`.

---

## Next

- See [complete list of installed colorschemes/plugins/lsps](/lin.nvim.dev/docs/appendix).
