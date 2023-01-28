---
layout: default
title: Installation
nav_order: 3
---

# Installation

- [Linux/macOS](#linuxmacos)
- [Windows](#windows)
- [Options](#options)
- [Upgrade](#upgrade)
- [Optimization](#optimization)

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

{: .note-title}

---

## Windows

{: .note-title }

> Notice
>
> Use a package manager (such as [chocolatey](https://chocolatey.org/) and [scoop](https://scoop.sh/)) could be a better choice, just make sure they're available in $env:PATH.

0. [Enable Windows Developer Mode](https://learn.microsoft.com/en-us/windows/apps/get-started/enable-your-device-for-development#activate-developer-mode).

1. Install [Visual Studio](https://www.visualstudio.com/) with below 2 components:

   - .NET Desktop Development
   - Desktop development with C++
     {% include nest-image.html src="/assets/installations/install-windows-visual-studio2.png" alt="install-windows-visual-studio2.png" width="95%" %}

2. Install [64-bit Git for Windows Setup](https://git-scm.com/downloads) with below 3 options:

   - In **Select Components**, select **Associate .sh files to be run with Bash**.
     {% include nest-image.html src="/assets/installations/install-windows-git1.png" alt="install-windows-git1.png" width="70%" %}
   - In **Adjusting your PATH environment**, select **Use Git and optional Unix tools from the Command Prompt**.
     {% include nest-image.html src="/assets/installations/install-windows-git2.png" alt="install-windows-git2.png" width="70%" %}
   - In **Configuring the terminal emulator to use with Git Bash**, select **Use Windows's default console window**. After this step, _git.exe_ and Linux built-in commands(such as _bash.exe_, _cp.exe_, _mv.exe_, _ls.exe_) will be available in $env:PATH.
     {% include nest-image.html src="/assets/installations/install-windows-git3.png" alt="install-windows-git3.png" width="70%" %}

3. Install other 64-bit dependencies:

   - [Neovim](https://github.com/neovim/neovim/releases/latest): add _nvim.exe_ to $env:PATH.
   - [CMake](https://github.com/Kitware/CMake/releases/latest): add _cmake.exe_ to $env:PATH.
   - [Make-for-win32](https://sourceforge.net/projects/gnuwin32/files/make): add _make.exe_ to $env:PATH.
   - [Python3](https://www.python.org/downloads/windows/): manually copy _python.exe_ as _python3.exe_, then add _python3.exe_ to $env:PATH (since windows python3 installer only provide _python.exe_).
   - [Node.js](https://nodejs.org/en/download/): add _node.exe_, _npm.exe_ to $env:PATH.
   - [7-zip](https://www.7-zip.org/): add _7z.exe_ to $env:PATH.
   - [Universal-ctags](https://github.com/universal-ctags/ctags-win32/releases): add _ctags.exe_, _readtags.exe_ to $env:PATH.
   - [Ripgrep](https://github.com/BurntSushi/ripgrep): add _rg.exe_ to $env:PATH.
   - [fd](https://github.com/sharkdp/fd): add _fd.exe_ to $env:PATH.
   - (Optional) [bat](https://github.com/sharkdp/bat): add _bat.exe_ to $env:PATH.
   - (Optional) [delta](https://github.com/dandavison/delta): add _delta.exe_ to $env:PATH.

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

## Options

The installer provides 3 installation modes:

- Full mode: default mode, it installs all features for the best experience, while consuming unignorable CPU, memory, disk and graphics.
- Limit mode: use `--limit` for low-performance devices such as old PC, which disables most plugins and extensions.
- Basic mode: use `--basic` for restricted environments such as production servers, which only installs a pure basic vim setting file.

And more options:

- `--use-color`: use a static color scheme, instead of random selection on startup. For example: `--use-color=darkblue`.
- `--no-color`: disable color schemes, and random selection on startup.
- `--no-hilight`: disable highlights, such as RGB color, cursor word, etc.
- `--no-lang`: disable language support, such as auto-complete, code format, lint, diagnostics, etc.
- `--no-edit`: disable editing enhancements, such as easy comments, cursor movement, etc.
- `--no-plug`: disable specific plugin in format _org/repo_, this can be provided multiple times. For example: `--no-plug=RRethy/vim-hexokinase --no-plug=alvan/vim-closetag`.
- `--no-winctrl`: disable Windows ctrl+{c,v,s,x,a,...} keys behavior, include cmd+{c,v,s,x,a,...} keys on macOS.

Please checkout [Plugins](/lin.nvim.dev/appendix/#plugins) to find out whether a plugin will be installed or not.

{: .note-title}

> Notice
>
> - Option `--limit` is equivalent to `--no-hilight --no-color --no-lang --no-edit`.

---

## Upgrade

For distribution, please re-install by:

```bash
cd ~/.vim && git pull origin main && ./install.sh
```

For vim plugins, please update in neovim:

```vim
:Lazy! sync
```

---

## Optimization

### Git Performance

Add below global configs to improve performance if git version &ge; 2.37.0:

- `git config --global core.fsmonitor true`
- `git config --global core.untrackedcache  true`

See [Improve Git monorepo performance with a file system monitor](https://github.blog/2022-06-29-improve-git-monorepo-performance-with-a-file-system-monitor/).

---

## Next

- Checkout [user guide](/lin.nvim.dev/user-guide).
