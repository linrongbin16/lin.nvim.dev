---
layout: default
title: Installation
nav_order: 3
---

# Installation

{: .note }

> _[neovide](https://neovide.dev/) is highly recommended as a high-performance neovim GUI client._

- [Linux/macOS](#linuxmacos)
- [Windows](#windows)
- [More Options](#more-options)
- [Upgrade](#upgrade)

Both neovim and its community are under active development, the [latest neovim stable version](https://github.com/neovim/neovim/wiki/Installing-Neovim) is always recommended. No effort is spent on maintaining backward compatibility.

## Linux/macOS

```bash
git clone https://github.com/linrongbin16/lin.nvim ~/.vim && cd ~/.vim && ./install.sh
```

{: .note-title}

> Notice
>
> 1. _install.sh_ will detect and install below dependencies with system package manager if not exists:
>    - [Git](https://git-scm.com/).
>    - [Neovim](https://github.com/neovim/neovim/wiki/Installing-Neovim).
>    - C/C++ tool chain([clang](https://clang.llvm.org/)/[gcc](https://gcc.gnu.org/), [make](https://www.gnu.org/software/make/), [pkg-config](https://www.freedesktop.org/wiki/Software/pkg-config/), [autoconf](https://www.gnu.org/software/autoconf/), [automake](https://www.gnu.org/software/automake/) and [cmake](https://cmake.org/)).
>    - [Python3](https://www.python.org/)(Python2 is not supported) and some pip packages.
>    - [Node.js](https://nodejs.org/), [yarn](https://yarnpkg.com/) and some npm packages.
>    - [Go](https://go.dev/).
>    - [Rust](https://www.rust-lang.org/) and some modern commands: [fd](https://github.com/sharkdp/fd), [rg](https://github.com/BurntSushi/ripgrep), [bat](https://github.com/sharkdp/bat), etc.
>    - [Curl](https://curl.se/), [wget](https://www.gnu.org/software/wget/), [unzip](https://linux.die.net/man/1/unzip) and [gzip](https://www.gnu.org/software/gzip/).
>    - [Universal-ctags](https://github.com/universal-ctags/ctags).
>    - [Hack nerd font](https://github.com/ryanoasis/nerd-fonts/releases/download/v2.2.2/Hack.zip).
> 2. Supported platforms for now:
>    - Debian/ubuntu based Linux: use _apt_ and _snap_ as installer.
>    - Fedora/centos based Linux: use _dnf_ as installer.
>    - Archlinux based Linux: use _pacman_ as installer.
>    - MacOS: use _brew_ as package installer, please install [Xcode](https://guide.macports.org/chunked/installing.html) and [homebrew](https://brew.sh/) as pre-requirements.
>    - Other \*NIX systems such as Gentoo, BSD are not supported yet.

## Windows

1.  Install [Visual Studio](https://www.visualstudio.com/) with below 2 components:
    - .NET Desktop Development
    - Desktop development with C++

{% include image.html src="/assets/installations/install-windows-visual-studio2.png" alt="install-windows-visual-studio2.png" %}

## More Options

## Upgrade
