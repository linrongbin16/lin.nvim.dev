---
layout: default
title: Philosophy
nav_order: 1
parent: Home
---

# Philosophy

## Reduce Duplications

Installing neovim with plugins/configs/LSP becomes heavy manual work.

Taking different OS/machines into account, it would be a time killer.

{: .note-title}

> Note
>
> Besides git and neovim itself, third-party dependencies greately enhanced capabilities:
>
> - Below programming languages are installed as dependecies:
>   - C/C++ tool chain: as a pre-requirement for other programming languages.
>   - Python3/Pip: for vim plugins and LSP.
>   - Node/Npm: for vim plugins and LSP.
>   - Rust/Cargo: for rg/fd/bat, as greate enhancements for fzf.
> - Curl/wget: download tools for _install.sh_(_install.ps1_) itself.
> - Unzip/gzip/7-zip: for LSP management.
> - Universal-ctags: tags.
> - Hack nerd font: patched-font with icons.

## Performant

Performance and scalability are the biggest advantages of neovim(actually far more performant than vscode from subjective feeling, with the same function of plugins).

Performance should always be first priority, even integrated with tons of things.

## IDE Features

UI/file-explorer/highlights/auto-complete/code-format/diagnostics/etc, these IDE features are in a chronic of starvation.

{: .note-title}

> Note
>
> Most popurlar color schemes are picked from [vimcolorschemes.com/top](https://vimcolorschemes.com/top) and [awesome-neovim#colorscheme](https://www.trackawesomelist.com/rockerBOO/awesome-neovim/readme/#colorscheme), following below rules:
>
> 1. &gt; 500 stars.
> 2. Last commit in 1 year.
> 3. For duplicate ports/variants, keep the one has more active updates or more stars.

## Concise and Efficiency

Trying to cover IDE features, but not be one.

All is about editing itself, no compiling/packaging/debugging.

There're some flashy and wow plugins, but only pain-point-resolver stays, not to mention ones that seriously drag cursor and typing.
