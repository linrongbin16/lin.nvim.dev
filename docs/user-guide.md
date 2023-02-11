---
layout: default
title: User Guide
nav_order: 4
has_children: true
has_toc: false
---

# User Guide

---

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
  - [Workspace](#workspace)
  - [Git](#git)
- [Search](#search)
  - [Text Search](#text-search)
  - [File Search](#file-search)
  - [History Search](#history-search)
  - [Git Search](#git-search)
  - [Vim Search](#vim-search)
- [Editing Enhancement](#editing-enhancement)
  - [Key Mappings](#key-mappings)
  - [Cursor Motion](#cursor-motion)
  - [Easy Comment](#easy-comment)
  - [Better Repeat](#better-repeat)
  - [Better Matching](#better-matching)
  - [Auto Pair/Close/End](#auto-pair-close-end)
- [Customization](#customization)

---

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
- `<Leader>wk` 🄽 - `:WhichKey `.

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

> Configure these key mappings in _~/.nvim/settings.vim_.

---

## UI

### File Explorer

Supported by [neo-tree.nvim](https://github.com/nvim-neo-tree/neo-tree.nvim). Please use _?_ to toggle help in neo-tree, or refer to [neo-tree's default configs](https://github.com/nvim-neo-tree/neo-tree.nvim/blob/v2.x/lua/neo-tree/defaults.lua).

A few keys are modified for convenience:

- `h` 🄽 - Collapse current directory. `C` is removed for close node.
- `l` 🄽 - Expand directory or open file. `w` is removed for open node with window picker. `<Space>` is removed for (toggle current directory).
- `<C-s>` 🄽 - Open in a split window. `S` is removed for open in split.
- `<C-v>` 🄽 - Open in a vsplit window. `s` is removed for open in vsplit.
- `<C-t>` 🄽 - Open in a new tab window. `t` is removed for open in tabnew.
- `]c` 🄽 - Navigate to next(👇) git item. `]g` is removed for navigate to next.
- `[c` 🄽 - Navigate to previous(👆) git item. `[g` is removed for navigate to previous.

Resize explorer width:

- `<Leader>>` 🄽 - Resize explorer width bigger.
- `<Leader><` 🄽 - Resize explorer width smaller.

### Tabline

Supported by [bufferline.nvim](https://github.com/akinsho/bufferline.nvim) and [vim-bbye](https://github.com/moll/vim-bbye).

1. Navigation:
   - `]b` 🄽 - Go to next(👉) buffer.
   - `[b` 🄽 - Go to previous(👈) buffer.
   - `<Leader>bd` 🄽 - Close current buffer without closing vim window by command `:Bdelete`.
   - `<Leader>bD` 🄽 - Forcibly close current buffer without closing vim window by command `:Bdelete!`.
   - `<Leader>1` 🄽 - Go to buffer-1.
   - `<Leader>2` 🄽 - Go to buffer-2.
   - `<Leader>3` 🄽 - Go to buffer-3.
   - `<Leader>4` 🄽 - Go to buffer-4.
   - `<Leader>5` 🄽 - Go to buffer-5.
   - `<Leader>6` 🄽 - Go to buffer-6.
   - `<Leader>7` 🄽 - Go to buffer-7.
   - `<Leader>8` 🄽 - Go to buffer-8.
   - `<Leader>9` 🄽 - Go to buffer-9.
   - `<Leader>0` 🄽 - Go to the last buffer.
2. Re-order:
   - `<Leader>>` 🄽 - Move(re-order) current buffer to next(👉) position.
   - `<Leader><` 🄽 - Move(re-order) current buffer to previous(👈) position.
3. Mouse:
   - `<LeftMouse>` 🄽 - Go to target buffer.
   - `<RightMouse>` 🄽 - Close target buffer.

### Highlight Words

Highlight words with different colors, supported by [vim-mark](https://github.com/inkarkat/vim-mark).

All keys are mapped with prefix `<Leader>k` to avoid key conflicts with other plugins:

- `<Leader>km` 🄽 🅅 - Mark/unmark word under cursor.
- `<Leader>kM` 🄽 - Clear all words.
- `<Leader>kn` 🄽 - Navigate to next(👇) marked word.
- `<Leader>kN` 🄽 - Navigate to previous(👆) marked word.

### GUI Font

Patched-fonts [Hack Nerd Font Mono](https://github.com/ryanoasis/nerd-fonts/releases) is enabled by default.

{: .note}

> Configure GUI font in _~/.nvim/settings.vim_.

---

## IDE Features

Supported by [nvim-cmp](https://github.com/hrsh7th/nvim-cmp), [null-ls.nvim](https://github.com/jose-elias-alvarez/null-ls.nvim) and many other plugins, please see [Manage LSP Servers](/lin.nvim.dev/docs/manage-lsp-servers) for more details.

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

Navigate with a floating window to preview and edit, supported by [glance.nvim](https://github.com/DNLHC/glance.nvim).

A few keys are modified for better user experience:

List window keys:

- `<C-s>` 🄽 - Open preview window in split. `s` is removed for open split.
- `<C-v>` 🄽 - Open preview window in vsplit. `v` is removed for open vsplit.
- `<C-t>` 🄽 - Open preview window in new tab. `t` is removed for open new tab.
- `<Leader>p` 🄽 - Go to preview window. `<Leader>l` is removed for go to preview window.
- `<C-c>`/`<C-[>` 🄽 - Close navigation window. `Q` is removed for close list window.

Preview window keys:

- `<Tab>`/`<S-Tab>` are removed for jump to next/previous navigation location.
- `<Leader>l` 🄽 - Go to list window. `<Leader>p` is removed for go to list window.
- `<C-c>`/`<C-[>` 🄽 - Close preview window. `Q` is removed for close preview window.

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

### Git

- `]c` 🄽 - Go to next(👇) git chunk in current buffer.
- `[c` 🄽 - Go to previous(👆) git chunk in current buffer.
- `<Leader>gb` 🄽 - Toggle git blame info on current line.

{: .note}

> Configure these key mappings in _~/.nvim/lua/conf/lsp.lua_.

---

## Search

Supported by [fzf.vim](https://github.com/junegunn/fzf.vim) and [nvim-lspfuzzy](https://github.com/ojroques/nvim-lspfuzzy). All fzf commands are renamed with the prefix `Fzf`, for example `:Files` are renamed to `:FzfFiles`, `:Rg` are renamed to `:FzfRg`.

### Text Search

- `<Space>r` 🄽 - Live grep by `FzfRg`, by default this command will filter ignored and hidden files.
  - `<Space>ur` 🄽 - Unrestricted(--no-ignore --hidden) live grep by extend command `FzfUnrestrictedRg`.
  - `<Space>pr` 🄽 - Precise(no fuzzy) live grep by extend command `FzfPrecisedRg`.
  - `<Space>upr` 🄽 - Unrestricted(--no-ignore --hidden) precise(no fuzzy) live grep by self-defined `FzfUnrestrictedPrecisedRg`.
  - `<Space>wr` 🄽 - Search word under cursor by `FzfCWordRg`, by default this command will filter ignored and hidden files.
  - `<Space>uwr` 🄽 - Unrestricted(--no-ignore --hidden) search word under cursor by extend command `FzfUnrestrictedCWordRg`.
- `<Space>ln` 🄽 - Search lines in current buffer by `FzfLines`.
- `<Space>tg` 🄽 - Search tags by `FzfTags`.

### File Search

- `<Space>f` 🄽 - Search files by `FzfFiles`, by default this command will filter ignored and hidden files.
  - `<Space>uf` 🄽 - Unrestricted(--no-ignore --hidden) search files by extend command `FzfUnrestrictedFiles`.
  - `<Space>wf` 🄽 - Search files by word under cursor by extend command `FzfCWordFiles`.
  - `<Space>uwf` 🄽 - Unrestricted(--no-ignore --hidden) search files by word under cursor by extend command `FzfUnrestrictedCWordFiles`.
- `<Space>b` 🄽 - Search opened buffers by `FzfBuffers`.
- `<Space>hf` 🄽 - Search history files (v:oldfiles) and opened buffers by `FzfHistory`.

### History Search

- `<Space>hs` 🄽 - Search searching history by `FzfHistory/`.
- `<Space>hc` 🄽 - Search vim command history by `FzfHistory:`.

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

### Key Mappings

Supported by [which-key.nvim](https://github.com/folke/which-key.nvim).

### Cursor Motion

Supported by [leap.nvim](https://github.com/ggandor/leap.nvim) and [hop.nvim](https://github.com/phaazon/hop.nvim).

Leap keeps its default key mappings(s/S, x/X), and keys for hop are mapped following its predecessor [vim-easymotion](https://github.com/easymotion/vim-easymotion):

- `<Leader><Leader>f{char}` 🄽 🅇 - Move forward by a single {char}.
- `<Leader><Leader>F{char}` 🄽 🅇 - Move backward by a single {char}.
- `<Leader><Leader>s{char}{char}` 🄽 🅇 - Move forward by two consequent {char}{char}.
- `<Leader><Leader>S{char}{char}` 🄽 🅇 - Move backward by two consequent {char}{char}.
- `<Leader><Leader>w` 🄽 🅇 - Move forward by word.
- `<Leader><Leader>W` 🄽 🅇 - Move backward by word.
- `<Leader><Leader>l` 🄽 🅇 - Move forward by line.
- `<Leader><Leader>L` 🄽 🅇 - Move backward by line.

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

_init.vim_ will load below components in _~/.nvim_ directory:

- _conf/\*.vim_ and _lua/conf/\*.lua_ - Basic vim and lua settings.
- _lua/plugins.lua_ - Plugins managed by [lazy.nvim](https://github.com/folke/lazy.nvim), see [Plugins](/lin.nvim.dev/appendix/#plugins) for the complete list.
- _repo/{org}/{repo}/\*.vim_ and _lua/repo/{org}/{repo}/\*.lua_ - Settings for related plugin.
- _colorschemes.vim_ - Color schemes.
- _lua/lspservers.lua_ - LSP servers.
- _settings.vim_ - Other settings.

{: .note}

> Configure plugins in _lua/plugins.lua_ and related settings in _repo/{org}/{repo}/\*.vim_ or _lua/repo/{org}/{repo}/\*.lua_.

---

## Next

- See [complete list of installed colorschemes/plugins/lsps](/lin.nvim.dev/docs/appendix).
