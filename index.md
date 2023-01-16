---
title: Home
layout: home
nav_order: 1
has_children: true
---

# lin.nvim: Lin Rongbin's Neovim Distribution

{: .note }

> _A highly configured [neovim](https://neovim.io/) distribution integrated with tons of utilities for development, inspired by [spf13-vim](https://github.com/spf13/spf13-vim)._

{% include youtube.html id="zCfSekdZiIg" %}

---

Aim to be out-of-box, IDE-like editing experience, performant, lightweight and friendly to most neovim users. Focus on and only on editing, no compiling/packaging/debugging.

Solved these issues:

- Time-cost configurations: all behaviors follow the community's best practices and most popular editors (just like [vscode](https://code.visualstudio.com/)).
- Lack of language support: language server protocol(LSP) is supported by [nvim-cmp](https://github.com/hrsh7th/nvim-cmp) and [null-ls.nvim](https://github.com/jose-elias-alvarez/null-ls.nvim), with [a bunch of language servers](/lin.nvim.dev/appendix/#lsp-servers) embedded.
- Difficulties on plugin: all [plugins](/lin.nvim.dev/appendix/#plugins) are carefully selected and configured for the best performance and editing experience, following most modern editors (again, just like vscode).
- Duplicate installations: one line command for different OS and machines (not on Windows for now), following the same behavior.
- Naive UI - Pretty color schemes, icons, file explorer, tabs and status are integrated.

Please see [Philosophy](/lin.nvim.dev/philosophy) for more thoughts.

---

## Next

- See [Demo](/lin.nvim.dev/demo) for more use cases.
