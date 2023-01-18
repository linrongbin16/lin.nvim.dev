---
title: Home
layout: home
nav_order: 1
<!-- has_children: true -->
---

# lin.nvim: Lin Rongbin's Neovim Distribution

> Leave vim behind, this is the next generation of [lin.vim](https://github.com/linrongbin16/lin.vim).

A highly configured [neovim](https://neovim.io/) distribution integrated with tons of utilities for development, inspired by [spf13-vim](https://github.com/spf13/spf13-vim).

Aim to be out-of-box, with IDE features, performant, lightweight and friendly to most neovim users. Focus on and only on editing, no compiling/packaging/debugging.

{% include youtube.html id="zCfSekdZiIg" %}

---

## Philosophy

### No-Manual

All done by one-line command(not for windows now), plugins/configs/LSP everything all set.

{: .note-title}

> Note
>
> Besides git and neovim itself, there're still some third-party dependencies can't be given up:
>
> - Programming languages:
>   - C/C++ tool chain: as a pre-requirement for other things.
>   - Python3/pip: for vim plugins and LSP.
>   - Node/npm: for vim plugins and LSP.
>   - Rust/cargo: for rg/fd/bat, as greate enhancements for fzf.
> - Curl/wget: download tools for installer itself.
> - Unzip/gzip/7-zip: for LSP management.
> - Universal-ctags: tags.
> - Hack nerd font: patched-font with icons.

### IDE Features

Feed IDE features that are in a chronic of starvation:

- Modern UI(icons, file explorer, tabs, etc).
- More colors and highlights.
- Searching.
- Auto-complete.
- Code-format.
- Diagnostics.
- ...

{: .note-title}

> Note
>
> Most popurlar color schemes are picked from [vimcolorschemes.com/top](https://vimcolorschemes.com/top) and [awesome-neovim#colorscheme](https://www.trackawesomelist.com/rockerBOO/awesome-neovim/readme/#colorscheme), following below rules:
>
> 1. &gt; 500 stars.
> 2. Last commit in 1 year.
> 3. For duplicate ports/variants, keep the one has more stars, more active updates or newer features.

### Focus

Focus on and only on editing, no compiling/packaging/debugging:

- Trying to cover IDE features, but not be one.
- The installer should depend less and customize more.
- Performance should always be first priority, even integrated with tons of things.
- There're some flashy and wow plugins, but only pain-point-killer stays, not to mention ones that seriously drag cursor and typing.

### Compatibility

Both neovim and its community are under active development, the [latest stable version](https://github.com/neovim/neovim/wiki/Installing-Neovim) is always recommended.

No effort is spent on maintaining backward compatibility.

---

## Next

- See [demo](/lin.nvim.dev/demo) for more use cases.
