---
layout: default
title: User Guide
nav_order: 4
has_children: true
---

# User Guide

- [Global Key Mappings](#global-key-mappings)
  - [Hot Keys](#hot-keys)
  - [Ctrl+? Cmd+? Keys](#ctrl-cmd-keys)
  - [Enhanced Copy/Paste](#enhanced-copypaste)
- [UI](#ui)
  - [File Explorer](#file-explorer)
  - [Tabline](#tabline)
  - [GUI Font](#gui-font)
- [IDE-like Editing Features](#ide-like-editing-features)
  - [Code Complete](#code-complete)
  - [Symbols](#symbols)
  - [Diagnostics](#diagnostics)
  - [Code Format](#code-format)
  - [Code Actions](#code-actions)
  - [Git](#git)
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
  - [Highlight Words](#highlight-words)
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
- `F7` **🅽** - Enable/disable highlighting word marks, see [Highlight Words](#highlight-words).
- `<S-F7>` **🅽** - Clear all highlighting word marks.
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

### Enhanced Copy/Paste

Copy/paste across different vim instances through remote ssh could be difficult, so introduce two shortcuts using local cache:

- `<Leader>y` **🆅** - Copy selected text to cache.
- `<Leader>p` **🅽** - Paste from cache to current cursor.

Configure these key mappings in _~/.vim/settings.vim_.

---

## UI

### File Explorer

Supported by [nvim-tree.lua](https://github.com/kyazdani42/nvim-tree.lua). Please use _g?_ to toggle help in nvim-tree, or refer to [:help nvim-tree.view.mappings](https://github.com/nvim-tree/nvim-tree.lua/blob/master/doc/nvim-tree-lua.txt) for default key mappings. A few keys are added for convenience:

1. Navigation:
   - `h` **🅽** - Collapse directory.
   - `l` **🅽** - Expand directory or open file.
2. Copy/paste/cut:
   - `C` **🅽** - Copy file/directory into an internal clipboard, just like _ctrl+c/cmd+c_ in other editors.
   - `X` **🅽** - Cut file/directory into an internal clipboard, just like _ctrl+x/cmd+c_ in other editors.
   - `V` **🅽** - Paste file/directory from an internal clipboard to current cursor, just like _ctrl+v/cmd+v_ in other editors.
3. Adjust width:
   - `<M-.>`/`<M-Right>`/`<C-.>`/`<C-Right>` **🅽** - Make explorer bigger(👉).
   - `<M-,>`/`<M-Left>`/`<C-,>`/`<C-Left>` **🅽** - Make explorer smaller(👈).

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

---

## IDE-like Editing Features

Supported by [nvim-cmp](https://github.com/hrsh7th/nvim-cmp) and a bunch of other plugins, please see [Manage LSP Servers](/lin.nvim.dev/manage-lsp-servers) for more details.

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

Configure these key mappings in _~/.vim/repository/hrsh7th/nvim-cmp.vim_, or configure embedded LSP servers in _~/.vim/lsp-settings.vim_.

---

### Search

Search engine is supported by [fzf.vim](https://github.com/junegunn/fzf.vim) and [nvim-lspfuzzy](https://github.com/ojroques/nvim-lspfuzzy). All fzf commands are renamed with the prefix _Fzf_, for example `:Files` are renamed to `:FzfFiles`, `:Rg` are renamed to `:FzfRg`.

#### Text Search

- `<Space>r` **🅽** - Search text by self-defined command `:LinFzfRg`.
- `<Space>w` **🅽** - Search word under cursor by self-defined command `:LinFzfRgCWord`.
- `<Space>ln` **🅽** - Search lines on current buffer by `:FzfLines`.
- `<Space>tg` **🅽** - Search tags by `:FzfTags`.

#### History Search

- `<Space>sh` **🅽** - Search searched history by `:FzfHistory/`.
- `<Space>ch` **🅽** - Search vim command history by `:FzfHistory:`.

#### File Search

- `<Space>f`/`<C-p>` **🅽** - Search files by `:FzfFiles`.
- `<Space>b` **🅽** - Search opened buffers by `:FzfBuffers`.
- `<Space>hf` **🅽** - Search history files (v:oldfiles) and opened buffers by `:FzfHistory`.

#### Git Search

- `<Space>gc` **🅽** - Search git commits by `:FzfCommits`.
- `<Space>gf` **🅽** - Search files in git repository by `:FzfGFile`.
- `<Space>gs` **🅽** - Search files in git status by `:FzfGFiles?`.

#### Other Search

- `<Space>mk` **🅽** - Search marks by `:FzfMarks`.
- `<Space>mp` **🅽** - Search normal mode vim key mappings by `:FzfMaps`.
- `<Space>cm` **🅽** - Search vim commands by `:FzfCommands`.
- `<Space>ht` **🅽** - Search help tags by `:FzfHelptags`.

Configure these key mappings in _~/.vim/repository/junegunn/fzf.vim.vim_.

---

## Editing Enhancement

#### Easy Comment

Support by [Comment.nvim](https://github.com/numToStr/Comment.nvim).

#### Cursor Motion

Support by [hop.nvim](https://github.com/phaazon/hop.nvim).

- `<Leader>f{char}` **🅽** - Move by a single {char}.
- `<Leader>s{char}{char}` **🅽** - Move by two consequent {char}{char}.
- `<Leader>w` **🅽** - Move by word.
- `<Leader>l` **🅽** - Move by line.

#### Word Movement

Better movement respects words that missing whitespaces.

Support by [vim-wordmotion](https://github.com/chaoren/vim-wordmotion).

- `,w`/`,W` **🅽** - word/WORD forward(👉), exclusive.
- `,b`/`,B` **🅽** - word/WORD backward(👈), exclusive.
- `,e`/`,E` **🅽** - Forward to the end of word/WORD, inclusive.
- `,ge`/`,gE` **🅽** - Backward to the end of word/WORD, inclusive.

#### Better Repeat

Better repeat(`.`) operation.

Supported by [vim-repeat](https://github.com/tpope/vim-repeat).

#### Better Matching

Better matching for brackets, parentheses, HTML tags, if-endif, etc.

Supported by [vim-matchup](https://github.com/andymass/vim-matchup).

#### Auto Pair and Close HTML Tag

Auto pair brackets and close html tags.

Supported by [nvim-autopairs](https://github.com/windwp/nvim-autopairs) and [vim-closetag](https://github.com/alvan/vim-closetag).

#### Highlight Words

Highlight all the words with different colors.

Supported by [vim-mark](https://github.com/inkarkat/vim-mark).

- `<Leader>m` **🅽** **🆅** - Mark/clear mark under cursor.
- `<Leader>*` **🅽** - Navigate to next(👇) mark.
- `<Leader>#` **🅽** - Navigate to previous(👆) mark.

---

## Customization

_init.vim_ will load below components:

- _lua/plugins.lua_ - Vim plugins managed by [packer.nvim](https://github.com/wbthomason/packer.nvim). Please see [Plugins](/lin.nvim.dev/appendix/#plugins) to find all plugins installed in this distribution.
- _standalone_ directory - Pure vim settings for basic neovim behavior.
- _repository_ and _lua/repository_ directory - Plugin settings for each installed plugin, these settings will be included by _init.vim_.
- _lsp-settings.vim_ - LSP server management.
- _color-settings.vim_ - Color scheme management.
- _settings.vim_ - Other settings include GUI font, global key mappings, etc.

To add/remove plugins, please configure _lua/plugins.lua_, related settings under _repository_ and _lua/repository_ directory, and modify _init.vim_.

For basic install mode, the _init.vim_ is _standalone/basic.vim_, no more else, see [More Options](#more-options).

---

## Next

- See [Installed Plugins](/lin.nvim.dev/appendix/#plugins).
- See [Installed LSP Servers](/lin.nvim.dev/appendix/#lsp-servers).
- See [Installed Formatter/Linter/Diagnostic/CodeAction](/lin.nvim.dev/appendix/#extra-formatterlinterdiagnosticcodeaction).
