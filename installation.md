---
layout: default
title: Installation
nav_order: 3
---

# Installation

- [Linux/macOS](#linuxmacos)
- [Windows](#windows)
- [More Options](#more-options)
- [Upgrade](#upgrade)

---

## Linux/macOS

```bash
git clone https://github.com/linrongbin16/lin.nvim ~/.vim && cd ~/.vim && ./install.sh
```

{: .note-title}

> Notice
>
> 1. _install.sh_ will install [third-party dependencies](/lin.nvim.dev/appendix/#dependencies) with system package manager if not exists. For now supported platforms are:
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

0. [Enable Windows Developer Mode](https://learn.microsoft.com/en-us/windows/apps/get-started/enable-your-device-for-development#activate-developer-mode).

1. Install [Visual Studio](https://www.visualstudio.com/) with below 2 components:

   - .NET Desktop Development
   - Desktop development with C++
     {% include nest-image.html src="/assets/installations/install-windows-visual-studio2.png" alt="install-windows-visual-studio2.png" width="95%" %}

2. Install [64-bit Git for Windows Setup](https://git-scm.com/downloads) with below 3 options:

   - In **_Select Components_**, select **_Associate .sh files to be run with Bash_**.
     {% include nest-image.html src="/assets/installations/install-windows-git1.png" alt="install-windows-git1.png" width="70%" %}
   - In **_Adjusting your PATH environment_**, select **_Use Git and optional Unix tools from the Command Prompt_**.
     {% include nest-image.html src="/assets/installations/install-windows-git2.png" alt="install-windows-git2.png" width="70%" %}
   - In **_Configuring the terminal emulator to use with Git Bash_**, select **_Use Windows's default console window_**. After this step, _git.exe_ and Linux built-in commands(such as _bash.exe_, _cp.exe_, _mv.exe_, _ls.exe_) will be available in _$env:PATH_.
     {% include nest-image.html src="/assets/installations/install-windows-git3.png" alt="install-windows-git3.png" width="70%" %}

3. Install other 64-bit dependencies:

   - [Neovim - _nvim-win64.msi_](https://github.com/neovim/neovim/releases/latest): add _nvim.exe_ to _$env:PATH_.
   - [CMake - _cmake-{x.y.z}-windows-x86_64.msi_](https://github.com/Kitware/CMake/releases/latest): add _cmake.exe_ to _$env:PATH_.
   - [Make-for-win32 - _make-{x.y}-bin.zip_](https://sourceforge.net/projects/gnuwin32/files/make/3.81/make-3.81-bin.zip/download): add _make.exe_ to _$env:PATH_.
   - [Python3 - _python-{x.y.z}-amd64.exe_](https://www.python.org/downloads/windows/): manually copy _python.exe_ as _python3.exe_, then add _python3.exe_ to _$env:PATH_ (since windows python3 installer only provide _python.exe_).
   - [Rust - _rustup-init.exe (64-bit)_](https://www.rust-lang.org/tools/install): add _rustc.exe_, _cargo.exe_ to _$env:PATH_.
   - [Node.js - _node-v{x.y.z}-x64.msi_](https://nodejs.org/en/download/): add _node.exe_, _npm.exe_ to _$env:PATH_.
   - [7-zip - _7z{x}-x64.exe_](https://www.7-zip.org/): add _7z.exe_ to _$env:PATH_.
   - [Universal-ctags - _ctags-p{x.y.d.z}-x64.zip_](https://github.com/universal-ctags/ctags-win32/releases): add _ctags.exe_, _readtags.exe_ to _$env:PATH_.

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
> {% include nest-image.html src="/assets/installations/install-windows-git-path.png" alt="install-windows-git-path.png" width="70%" %}

{: .note-title}

> Notice
>
> Disable Windows App alias _python.exe_ and _python3.exe_, it could lead you to the wrong python from Windows Store.
> {% include nest-image.html src="/assets/installations/install-windows-app-alias.png" alt="install-windows-app-alias.png" width="70%" %}

---

## More Options

_install.sh_ (and _install.ps1_) provides 3 installation modes:

- Full mode: default mode, it installs all features for the best experience, while consuming unignorable CPU, memory, disk and graphics.
- Limit mode: for low-performance devices such as old PC. With `./install.sh --limit`, it disables extra highlights, color schemes, language support and other editing enhancements.
- Basic mode: for the extremely restricted environment such as a production server, which has limited network access or lacks authentication. With `./install.sh --basic`, it disables everything except one basic vim setting file.

And more options:

- `--static-color`: use static color scheme, instead of random selection on startup. For example: `--static-color=darkblue`.
- `--disable-color`: disable extra color schemes, and random selection on startup.
- `--disable-highlight`: disable extra highlights. Such as RGB color, cursor word, etc.
- `--disable-language`: disable language support. Such as auto-complete, code-format, lint, diagnostics, etc.
- `--disable-editing`: disable extra editing enhancements. Such as easy comments, cursor motion, etc.
- `--disable-plugin`: disable specific plugin in format _org/repo_, this is a multiple options. For example: `--disable-plugin=RRethy/vim-hexokinase --disable-plugin=alvan/vim-closetag`.

Please checkout [installed plugins](/lin.nvim.dev/appendix/#plugins) to find out whether a plugin will be installed or not.

{: .note-title}

> Notice
>
> - You could use `--disable-xxx` to disable some specific features.
> - Option `--limit` is equivalent to `--disable-highlight --disable-color --disable-language --disable-editing`.

---

## Upgrade

For distribution, please re-install by:

```bash
cd ~/.vim && git pull origin master && ./install.sh
```

For vim plugins, please update in neovim:

```vim
:PackerSync
```

---

## Next

- Checkout the [user guide](/lin.nvim.dev/user-guide).
