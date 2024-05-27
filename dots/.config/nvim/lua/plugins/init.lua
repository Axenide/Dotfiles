return {
  {
    "danymat/neogen",
    config = true,
  },
  {
    "stevearc/conform.nvim",
    config = function()
      require "configs.conform"
    end,
  },

  {
    "nvim-tree/nvim-tree.lua",
    opts = {
      git = { enable = true },
    },
  },
  {
    'Exafunction/codeium.vim',
    event = "BufEnter",
  },
  {
    "TobinPalmer/pastify.nvim",
    cmd = { 'Pastify' },
    config = function()
      require("pastify").setup({
        opts = {
          local_path = "/assets/img/",
        },
      })
    end,
  },

  {"ellisonleao/glow.nvim", config = true, cmd = "Glow"},

  {
    "iamcco/markdown-preview.nvim",
    ft = "markdown",
    cmd = {"MarkdownPreview", "MarkdownPreviewStop"},
    build = "cd app && yarn install && git reset --hard",
    config = function()
      local plugin_dir = vim.fn.stdpath("config") .. "/lua/plugins/"
      vim.g.mkdp_browser = plugin_dir .. "webview.py"
      vim.g.mkdp_auto_close = 0
    end,
  },
  {
    "nvim-treesitter/nvim-treesitter",
    opts = {
      auto_install = true,
    },
  },
  {
    "christoomey/vim-tmux-navigator",
    lazy = false,
  },
  {
    "tpope/vim-fugitive",
    lazy = false,
  },

  {
    "williamboman/mason.nvim",
    opts = {
      ensure_installed = {
        "pyright",
        "debugpy",
      },
    },
  },

  {
    "neovim/nvim-lspconfig",
    config = function()
      require "configs.lspconfig"
      require "configs.lspconfig"
    end,
  },

  {
    "mfussenegger/nvim-dap",
    config = function(_, opts)
    end
  },
  {
    "mfussenegger/nvim-dap-python",
    ft = {"python"},
    dependencies = {
      "nvim-neotest/nvim-nio",
      "mfussenegger/nvim-dap",
      "rcarriga/nvim-dap-ui",
    },
    config = function(_, opts)
      local path = "~/.local/share/nvim/mason/packages/debugpy/venv/bin/python"
      require("dap-python").setup(path)
    end,
  },

  {
    "rcarriga/nvim-dap-ui",
    dependencies = "mfussenegger/nvim-dap",
    config = function()
      local dap = require("dap")
      local dapui = require("dapui")
      dapui.setup()
      dap.listeners.after.event_initialized["dapui_config"] = function()
        dapui.open()
      end
      dap.listeners.before.event_terminated["dapui_config"] = function()
        dapui.close()
      end
      dap.listeners.before.event_exited["dapui_config"] = function()
        dapui.close()
      end
    end,
  },
}
