---
layout: default
title: Philosophy
nav_order: 1
parent: Home
---

# Philosophy

## No-Manual

All done by one-line command(not for windows now):

- Plugins.
- Configs.
- LSP servers.
- ...

## IDE Features

Feed with IDE features that are in a chronic of starvation:

- Modern UI(icons, file explorer, tabs, etc).
- More colors and highlights.
- Searching.
- Auto-complete.
- Code-format.
- Diagnostics.
- ...

{: .note}

> Most popurlar color schemes are picked from [vimcolorschemes.com/top](https://vimcolorschemes.com/top) and [awesome-neovim#colorscheme](https://www.trackawesomelist.com/rockerBOO/awesome-neovim/readme/#colorscheme), following below rules:
>
> 1. &ge; 500 stars.
> 2. Last commit in 1 year.
> 3. For multiple ports/variants, keep more stars or updates, even lower standards to &ge; 100 stars if has below features:
>    - Modern features: LSP/treesitter/etc.
>    - Plugins integration: tabline/statusline/etc.

## Focus

Focus on and only on editing, no compiling/packaging/debugging:

- Trying to cover IDE features, but not be one.
- The installer should depend less and customize more.
- Performance should always be first priority, even integrated with tons of things.
- There're some wow plugins, but only pain-point-killer stays, not to mention ones that seriously drag cursor and typing.

## Compatibility

No effort is spent on maintaining backward compatibility.

- Neovim's [Latest stable version](https://github.com/neovim/neovim/wiki/Installing-Neovim) is always recommended.
- OS in last 2 years(latest Ubuntu-LTS) are supported.
