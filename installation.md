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

---

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

---

## Windows

{: .note-title }

> Notice
>
> Use a package manager (such as [chocolatey](https://chocolatey.org/) and [scoop](https://scoop.sh/)) could be a better choice, just make sure they're available in _$env:PATH_.

1. Install [Visual Studio](https://www.visualstudio.com/) with below 2 components:

   - .NET Desktop Development
   - Desktop development with C++
     {% include image.html src="/assets/installations/install-windows-visual-studio2.png" alt="install-windows-visual-studio2.png" %}

2. Install [64-bit Git for Windows Setup](https://git-scm.com/downloads) with below 3 options:

   - In **_Select Components_**, select **_Associate .sh files to be run with Bash_**.
     {% include image.html src="/assets/installations/install-windows-git1.png" alt="install-windows-git1.png" width="60%" %}
   - In **_Adjusting your PATH environment_**, select **_Use Git and optional Unix tools from the Command Prompt_**.
     {% include image.html src="/assets/installations/install-windows-git2.png" alt="install-windows-git2.png" width="60%" %}
   - In **_Configuring the terminal emulator to use with Git Bash_**, select **_Use Windows's default console window_**. After this step, _git.exe_ and Linux built-in commands(such as _bash.exe_, _cp.exe_, _mv.exe_, _ls.exe_) will be available in _$env:PATH_.
     {% include image.html src="/assets/installations/install-windows-git3.png" alt="install-windows-git3.png" width="60%" %}

3. Install other 64-bit dependencies:

   - [Neovim](https://github.com/neovim/neovim/releases/latest)(_nvim-win64.msi_): add _nvim.exe_ to _$env:PATH_.
   - [CMake](https://github.com/Kitware/CMake/releases/latest)(_cmake-{x.y.z}-windows-x86_64.msi_): add _cmake.exe_ to _$env:PATH_.
   - [Make-for-win32](https://sourceforge.net/projects/gnuwin32/files/make/3.81/make-3.81-bin.zip/download)(_make-{x.y}-bin.zip_): add _make.exe_ to _$env:PATH_.
   - [Python3](https://www.python.org/downloads/windows/)(_python-{x.y.z}-amd64.exe_): manually copy _python.exe_ as _python3.exe_, then add _python3.exe_ to _$env:PATH_ (since windows python3 installer only provide _python.exe_).
   - [Rust](https://www.rust-lang.org/tools/install) (_rustup-init.exe (64-bit)_): add _rustc.exe_, _cargo.exe_ to _$env:PATH_.
   - [Go](https://go.dev/dl/) (_go{x.y.z}.windows-amd64.msi_): add _go.exe_ to _$env:PATH_.
   - [Node.js](https://nodejs.org/en/download/) (_node-v{x.y.z}-x64.msi_): add _node.exe_, _npm.exe_ to _$env:PATH_.
   - [7-zip](https://www.7-zip.org/): add _7z.exe_ to _$env:PATH_.
   - [Universal-ctags](https://github.com/universal-ctags/ctags-win32/releases) (_ctags-p{x.y.d.z}-x64.zip_): add _ctags.exe_, _readtags.exe_ to _$env:PATH_.

4. Install [Hack NFM](https://github.com/ryanoasis/nerd-fonts/releases/download/v2.2.2/Hack.zip) font.

5. Run PowerShell command as Administrator:

```powershell
git clone https://github.com/linrongbin16/lin.nvim $env:USERPROFILE\.vim
cd $env:USERPROFILE\.vim
.\install.ps1
```

{: .note-title}

> Notice
>
> If you are using WSL, _C:\Windows\System32\bash.exe_ could lead you to WSL instead of the _bash.exe_ from [Git for Windows](https://git-scm.com/). Make sure the git path is ahead of _C:\Windows\System32_, so git bash will be first detected (_wsl.exe_ could connect to WSL as well so no need to worry about losing _C:\Windows\System32\bash.exe_).
> {% include image.html src="/assets/installations/install-windows-git-path.png" alt="install-windows-git-path.png" width="60%" %}

{: .note-title}

> Notice
>
> Disable Windows App alias _python.exe_ and _python3.exe_, it could lead you to the wrong python from Windows Store.
> {% include image.html src="/assets/installations/install-windows-app-alias.png" alt="install-windows-app-alias.png" width="60%" %}

---

## More Options

_install.sh_ (and _install.ps1_) provides 3 installation modes:

- Full mode: default mode, it installs all features for the best experience, which consumes unignorable CPU, memory, disk and graphics.
- Limit mode: for low-performance devices such as old PC. With `./install.sh --limit`, it disables extra highlights, color schemes, language support and other editing enhancements.
- Basic mode: for extremely restricted environment such as production environment, which has limited network access or lack of authentication. With `./install.sh --basic`, it disables everything except one basic vim setting file.

And more options:

- `--static-color=TEXT`: make color scheme static, instead of random selection on startup. For example: `--static-color=darkblue`.
- `--disable-color`: disable extra color schemes, and random selection on startup.
- `--disable-highlight`: disable extra highlights. Such as RGB and mark under cursor, etc.
- `--disable-language`: disable language support. Such as auto-complete and language servers, etc.
- `--disable-editing`: disable editing enhancements. Such as easy comments, cursor motion, etc.
- `--disable-plugin=TEXT`: disable specific vim plugin in format 'organization/repository', this is a multiple option. For example: `--disable-plugin=RRethy/vim-hexokinase --disable-plugin=alvan/vim-closetag`.

Notice:

- In full mode, you could use '--disable-xxx' options to disable some specific features.
- Option '--disable-highlight --disable-color --disable-language --disable-editing' is equivalent to '--limit'.

---

## Upgrade
