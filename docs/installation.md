---
layout: default
title: Installation
nav_order: 3
has_toc: false
---

<!-- markdownlint-disable MD013 MD025 -->

# Installation

---

- [Basic Mode](#basic-mode)
- [Linux/macOS](#linuxmacos)
- [Windows](#windows)
  - [Windows Developer Mode](#windows-developer-mode)
  - [Visual Studio](#visual-studio)
  - [Git](#git)
  - [Third-Party Dependencies](#third-party-dependencies)
  - [Patched GUI Font](#patched-gui-font)
  - [PowerShell Command](#powershell-command)
- [Options](#options)
  - [Auto-Detect Available Languages](#auto-detect-available-languages)
- [Upgrade](#upgrade)
- [Uninstall](#uninstall)
- [Optimization](#optimization)
  - [Git Performance](#git-performance)

---

## Basic Mode

If you want a basic installation, without any third-party dependencies or plugins(just like [sensible.vim](https://github.com/tpope/vim-sensible)). Just copy [cfg/basic.vim](https://github.com/linrongbin16/lin.nvim/blob/main/cfg/basic.vim) to your _~/.config/nvim/init.vim_, and that's all.

If you want a fully installation, go on with below steps.

---

## Linux/macOS

```bash
git clone https://github.com/linrongbin16/lin.nvim ~/.nvim && cd ~/.nvim && ./install.sh
```

{: .note}

> _install.sh_ will install [third-party dependencies](/lin.nvim.dev/appendix/#dependencies) with system package manager if not exists. Supported platforms are:
>
> - Debian/ubuntu based Linux: use _apt_ and _snap_ as installer.
> - Fedora/centos based Linux: use _dnf_ as installer.
> - Archlinux based Linux: use _pacman_ as installer.
> - MacOS: use _brew_ as package installer, please install [Xcode](https://guide.macports.org/chunked/installing.html) and [homebrew](https://brew.sh/) as pre-requirements.
> - Other \*NIX systems such as Gentoo, BSD are not supported yet.

{: .note-title}

---

## Windows

{: .important-title}

> Notice
>
> Please use either x64(recommended) or x86 for all below dependencies.

### Windows Developer Mode

Please check: <https://learn.microsoft.com/en-us/windows/apps/get-started/enable-your-device-for-development#activate-developer-mode>.

### Visual Studio

Install [Visual Studio](https://www.visualstudio.com/) with below 2 components:

- .NET Desktop Development
- Desktop development with C++

{% include image.html src="/assets/installations/install-windows-visual-studio2.png" alt="install-windows-visual-studio2.png" width="95%" %}

### Git

Install [Git for Windows Setup](https://git-scm.com/downloads) with below 3 options:

- In **Select Components**, select **Associate .sh files to be run with Bash**.

{% include image.html src="/assets/installations/install-windows-git1.png" alt="install-windows-git1.png" width="70%" %}

- In **Adjusting your PATH environment**, select **Use Git and optional Unix tools from the Command Prompt**.

{% include image.html src="/assets/installations/install-windows-git2.png" alt="install-windows-git2.png" width="70%" %}

- In **Configuring the terminal emulator to use with Git Bash**, select **Use Windows's default console window**. After this step, _git.exe_ and Linux built-in commands(such as _bash.exe_, _cp.exe_, _mv.exe_, _ls.exe_) will be available in $env:PATH.

{% include image.html src="/assets/installations/install-windows-git3.png" alt="install-windows-git3.png" width="70%" %}

### Third-Party Dependencies

- [Neovim](https://github.com/neovim/neovim/releases/latest): add _nvim.exe_ to $env:PATH.
- [CMake](https://github.com/Kitware/CMake/releases/latest): add _cmake.exe_ to $env:PATH.
- [Python3](https://www.python.org/downloads/windows/): manually copy _python.exe_ as _python3.exe_, then add _python3.exe_ to $env:PATH (since windows python3 installer only provide _python.exe_).
- [Node.js](https://nodejs.org/en/download/): add _node.exe_, _npm.exe_ to $env:PATH.
- [7-zip](https://www.7-zip.org/): add _7z.exe_ to $env:PATH.
- [Universal-ctags](https://github.com/universal-ctags/ctags-win32/releases): add _ctags.exe_, _readtags.exe_ to $env:PATH.
- [Rust](https://www.rust-lang.org/)(or [rg](https://github.com/BurntSushi/ripgrep), [fd](https://github.com/sharkdp/fd), [bat](https://github.com/sharkdp/bat), [delta](https://github.com/dandavison/delta)): add _rustc.exe_ and _cargo.exe_(or _rg.exe_, _fd.exe_, _bat.exe_, _delta.exe_) to $env:PATH. Notice bat and delta are optional.

{: .note}

> Use a package manager([chocolatey](https://chocolatey.org/) or [scoop](https://scoop.sh/)) may be a better choice, just make sure they're available in $env:PATH.

### Patched GUI Font

- [Hack NFM](https://github.com/ryanoasis/nerd-fonts/releases/download/v2.2.2/Hack.zip) font.

### PowerShell Command

Run PowerShell command as Administrator:

```powershell
git clone https://github.com/linrongbin16/lin.nvim $env:USERPROFILE\.nvim
cd $env:USERPROFILE\.nvim
.\install.ps1
```

{: .important-title}

> Notice
>
> If you are using WSL, _C:\Windows\System32\bash.exe_ could lead you to WSL instead of the _bash.exe_ from [Git for Windows](https://git-scm.com/). Make sure the git path is ahead of _C:\Windows\System32_, so git bash will be first detected (_wsl.exe_ could connect to WSL as well so no need to worry about losing _C:\Windows\System32\bash.exe_).
> {% include nest-image.html src="/assets/installations/install-windows-git-path.png" alt="install-windows-git-path.png" width="70%" %}

{: .important-title}

> Notice
>
> Disable Windows App alias _python.exe_ and _python3.exe_, it could lead you to the wrong python from Windows Store.
> {% include nest-image.html src="/assets/installations/install-windows-app-alias.png" alt="install-windows-app-alias.png" width="70%" %}

---

## Options

### Auto-Detect Available Languages

There's a real powerful option to quickly install lsp servers:

- `--with-lsp`: detect any language installed(based on compiler/interpreter), and interactively provide candidates for you.

---

## Upgrade

For distribution, please re-install by:

```bash
cd ~/.nvim && git pull origin main && ./install.sh
```

For vim plugins, please update in neovim:

```vim
:Lazy! sync
```

## Uninstall

```bash
rm -rf ~/.nvim
rm -rf ~/.config/nvim
```

---

## Optimization

### Git Performance

Add below global configs to improve performance if git version &ge; 2.37.0:

```bash
git config --global core.fsmonitor true
git config --global core.untrackedcache  true
```

See [Improve Git monorepo performance with a file system monitor](https://github.blog/2022-06-29-improve-git-monorepo-performance-with-a-file-system-monitor/).

---

## Next

- Checkout [user guide](/lin.nvim.dev/docs/user-guide).
- Checkout [Available LSP Servers](/lin.nvim.dev/docs/appendix/#available-lsp-servers) to find out available lsp servers.
