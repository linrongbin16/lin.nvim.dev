return {
    -- https://vimcolorschemes.com/
    {
        -- https://github.com/nlknguyen/papercolor-theme
        "nlknguyen/papercolor-theme",
        lazy = true,
        priority = 1000,
    },
    {
        -- https://github.com/cocopon/iceberg.vim
        "cocopon/iceberg.vim",
        lazy = true,
        priority = 1000,
    },
    {
        -- https://github.com/junegunn/seoul256.vim
        "junegunn/seoul256.vim",
        lazy = true,
        priority = 1000,
    },
    {
        -- https://github.com/jacoborus/tender.vim
        "jacoborus/tender.vim",
        lazy = true,
        priority = 1000,
    },
    {
        -- https://github.com/lifepillar/vim-solarized8
        "lifepillar/vim-solarized8",
        lazy = true,
        priority = 1000,
    },
    {
        -- https://github.com/jnurmine/zenburn
        "jnurmine/zenburn",
        lazy = true,
        priority = 1000,
    },
    {
        -- https://github.com/romainl/apprentice
        "romainl/apprentice",
        lazy = true,
        priority = 1000,
    },
    {
        -- https://github.com/raphamorim/lucario
        "raphamorim/lucario",
        lazy = true,
        priority = 1000,
    },
    {
        -- https://github.com/srcery-colors/srcery-vim
        "srcery-colors/srcery-vim",
        lazy = true,
        priority = 1000,
        name = "srcery",
    },
    {
        -- https://github.com/pineapplegiant/spaceduck
        "pineapplegiant/spaceduck",
        lazy = true,
        priority = 1000,
        branch = "main",
    },
    {
        -- https://github.com/ajmwagar/vim-deus
        "ajmwagar/vim-deus",
        lazy = true,
        priority = 1000,
    },
    {
        -- https://github.com/preservim/vim-colors-pencil
        "preservim/vim-colors-pencil",
        lazy = true,
        priority = 1000,
    },
    {
        -- https://github.com/challenger-deep-theme/vim
        "challenger-deep-theme/vim",
        lazy = true,
        priority = 1000,
        name = "challenger-deep-theme",
    },
    {
        -- https://github.com/rigellute/rigel
        "rigellute/rigel",
        lazy = true,
        priority = 1000,
    },
    {
        -- https://github.com/lifepillar/vim-gruvbox8
        "lifepillar/vim-gruvbox8",
        lazy = true,
        priority = 1000,
    },
    {
        -- https://github.com/crusoexia/vim-monokai (duplicated)
        "crusoexia/vim-monokai",
        lazy = true,
        priority = 1000,
    },
    {
        -- https://github.com/wadackel/vim-dogrun
        "wadackel/vim-dogrun",
        lazy = true,
        priority = 1000,
    },
    {
        -- https://github.com/jaredgorski/spacecamp
        "jaredgorski/spacecamp",
        lazy = true,
        priority = 1000,
    },
    {
        -- https://github.com/keitanakamura/neodark.vim
        "keitanakamura/neodark.vim",
        lazy = true,
        priority = 1000,
    },

    -- https://www.trackawesomelist.com/rockerBOO/awesome-neovim/readme/#colorscheme
    {
        -- https://github.com/catppuccin/nvim
        "catppuccin/nvim",
        lazy = true,
        priority = 1000,
        name = "catppuccin",
    },
    {
        -- https://github.com/rebelot/kanagawa.nvim
        "rebelot/kanagawa.nvim",
        lazy = true,
        priority = 1000,
    },
    {
        -- https://github.com/EdenEast/nightfox.nvim (duplicated)
        "EdenEast/nightfox.nvim",
        lazy = true,
        priority = 1000,
    },
    {
        -- https://github.com/sainnhe/everforest
        "sainnhe/everforest",
        lazy = true,
        priority = 1000,
    },
    {
        -- https://github.com/sainnhe/gruvbox-material
        "sainnhe/gruvbox-material",
        lazy = true,
        priority = 1000,
    },
    {
        -- https://github.com/projekt0n/github-nvim-theme
        "projekt0n/github-nvim-theme",
        lazy = true,
        priority = 1000,
        branch = "0.0.x",
    },
    {
        -- https://github.com/dracula/vim (duplicated)
        "dracula/vim",
        lazy = true,
        priority = 1000,
        name = "dracula",
    },
    {
        -- https://github.com/sainnhe/sonokai
        "sainnhe/sonokai",
        lazy = true,
        priority = 1000,
    },
    {
        -- https://github.com/mhartington/oceanic-next
        "mhartington/oceanic-next",
        lazy = true,
        priority = 1000,
    },
    {
        -- https://github.com/folke/tokyonight.nvim (duplicated)
        "folke/tokyonight.nvim",
        lazy = true,
        priority = 1000,
        branch = "main",
    },
    {
        -- https://github.com/ellisonleao/gruvbox.nvim
        "ellisonleao/gruvbox.nvim",
        lazy = true,
        priority = 1000,
    },
    {
        -- https://github.com/navarasu/onedark.nvim (duplicated)
        "navarasu/onedark.nvim",
        lazy = true,
        priority = 1000,
    },
    {
        -- https://github.com/tomasiser/vim-code-dark
        "tomasiser/vim-code-dark",
        lazy = true,
        priority = 1000,
    },
    {
        -- https://github.com/rose-pine/neovim
        "rose-pine/neovim",
        lazy = true,
        priority = 1000,
        name = "rose-pine",
        config = function()
            require("rose-pine").setup()
        end,
    },
    {
        -- https://github.com/marko-cerovac/material.nvim (duplicated)
        "marko-cerovac/material.nvim",
        lazy = true,
        priority = 1000,
    },
    {
        -- https://github.com/sainnhe/edge
        "sainnhe/edge",
        lazy = true,
        priority = 1000,
    },
    {
        -- https://github.com/fenetikm/falcon
        "fenetikm/falcon",
        lazy = true,
        priority = 1000,
    },
    {
        -- https://github.com/nyoom-engineering/oxocarbon.nvim
        "nyoom-engineering/oxocarbon.nvim",
        lazy = true,
        priority = 1000,
    },
    {
        -- https://github.com/bluz71/vim-nightfly-colors
        "bluz71/vim-nightfly-colors",
        lazy = true,
        priority = 1000,
        name = "nightfly",
    },
    {
        -- https://github.com/shaunsingh/nord.nvim (duplicated)
        "shaunsingh/nord.nvim",
        lazy = true,
        priority = 1000,
    },
    {
        -- https://github.com/bluz71/vim-moonfly-colors
        "bluz71/vim-moonfly-colors",
        lazy = true,
        priority = 1000,
        name = "moonfly",
    },
    {
        -- https://github.com/embark-theme/vim (duplicated)
        "embark-theme/vim",
        lazy = true,
        priority = 1000,
        name = "embark",
        branch = "main",
    },
}
