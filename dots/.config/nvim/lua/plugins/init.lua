return {
  {
    "serenevoid/kiwi.nvim",
    opts = {
      {
        name = "ax-wiki",
        path = "Dropbox/ax-wiki",
      },
    },
    keys = {
      { "<leader>ww", ':lua require("kiwi").open_wiki_index()<cr>', desc = "Open Wiki index" },
      {
        "<leader>aw",
        ':lua require("kiwi").open_wiki_index("ax-wiki")<cr>',
        desc = "Open index of [Ax]Wiki",
      },
      { "T", ':lua require("kiwi").todo.toggle()<cr>', desc = "Toggle Markdown Task" },
    },
    lazy = true,
  },
  { -- show images in nvim!
    "3rd/image.nvim",
    enabled = true,
    dev = false,
    ft = { "markdown", "quarto", "vimwiki", "html" },
    cond = function()
      -- Disable on Windows system
      return vim.fn.has "win32" ~= 1
    end,
    dependencies = {
      "leafo/magick", -- that's a lua rock
    },
    config = function()
      local image = require "image"
      image.setup {
        backend = "kitty",
        integrations = {
          markdown = {
            enabled = true,
            filetypes = { "markdown", "vimwiki", "quarto" },
          },
        },
        editor_only_render_when_focused = false,
        window_overlap_clear_enabled = true,
        tmux_show_only_in_active_window = true,
        max_width = nil,
        max_height = nil,
        max_width_window_percentage = nil,
        max_height_window_percentage = 30,
        kitty_method = "normal",
      }

      local function clear_all_images()
        local bufnr = vim.api.nvim_get_current_buf()
        local images = image.get_images { buffer = bufnr }
        for _, img in ipairs(images) do
          img:clear()
        end
      end

      local function get_image_at_cursor(buf)
        local images = image.get_images { buffer = buf }
        local row = vim.api.nvim_win_get_cursor(0)[1] - 1
        for _, img in ipairs(images) do
          if img.geometry ~= nil and img.geometry.y == row then
            local og_max_height = img.global_state.options.max_height_window_percentage
            img.global_state.options.max_height_window_percentage = nil
            return img, og_max_height
          end
        end
        return nil
      end

      local create_preview_window = function(img, og_max_height)
        local buf = vim.api.nvim_create_buf(false, true)
        local win_width = vim.api.nvim_get_option_value("columns", {})
        local win_height = vim.api.nvim_get_option_value("lines", {})
        local win = vim.api.nvim_open_win(buf, true, {
          relative = "editor",
          style = "minimal",
          width = win_width,
          height = win_height,
          row = 0,
          col = 0,
          zindex = 1000,
        })
        vim.keymap.set("n", "q", function()
          vim.api.nvim_win_close(win, true)
          img.global_state.options.max_height_window_percentage = og_max_height
        end, { buffer = buf })
        return { buf = buf, win = win }
      end

      local handle_zoom = function(bufnr)
        local img, og_max_height = get_image_at_cursor(bufnr)
        if img == nil then
          return
        end

        local preview = create_preview_window(img, og_max_height)
        image.hijack_buffer(img.path, preview.win, preview.buf)
      end

      vim.keymap.set("n", "<leader>io", function()
        local bufnr = vim.api.nvim_get_current_buf()
        handle_zoom(bufnr)
      end, { buffer = true, desc = "image [o]pen" })

      vim.keymap.set("n", "<leader>ic", clear_all_images, { desc = "image [c]lear" })
    end,
  },

  {
    "stevearc/conform.nvim",
    event = "BufWritePre",
    lazy = false,
    opts = require "configs.conform",
  },

  {
    "MeanderingProgrammer/render-markdown.nvim",
    ft = { "markdown", "quarto", "vimwiki" },
    dependencies = { "nvim-treesitter/nvim-treesitter", "nvim-tree/nvim-web-devicons" },
    ---@module 'render-markdown'
    ---@type render.md.UserConfig
    opts = {},
  },
  {
    "CopilotC-Nvim/CopilotChat.nvim",
    lazy = false,
    dependencies = {
      { "github/copilot.vim" },
      { "nvim-lua/plenary.nvim", branch = "master" },
    },
    build = "make tiktoken",
    opts = {},
  },

  {
    "danymat/neogen",
    config = true,
  },

  {
    "nvim-tree/nvim-tree.lua",
    opts = {
      git = { enable = true },
    },
  },

  {
    "TobinPalmer/pastify.nvim",
    cmd = { "Pastify" },
    config = function()
      require("pastify").setup {
        opts = {
          local_path = "/assets/img/",
        },
      }
    end,
  },

  { "ellisonleao/glow.nvim", config = true, cmd = "Glow" },

  {
    "iamcco/markdown-preview.nvim",
    ft = "markdown",
    cmd = { "MarkdownPreview", "MarkdownPreviewStop" },
    build = "cd app && yarn install && git reset --hard",
  },

  {
    "nvim-treesitter/nvim-treesitter",
    branch = "main",
    build = function()
      if vim.fn.executable "tree-sitter" == 1 then
        require("nvim-treesitter").install { "lua", "markdown", "markdown_inline", "python", "query", "vim", "vimdoc" }
      end
    end,
    config = function()
      if vim.fn.executable "tree-sitter" == 1 then
        require("nvim-treesitter").install { "lua", "markdown", "markdown_inline", "python", "query", "vim", "vimdoc" }
      end

      vim.api.nvim_create_autocmd("FileType", {
        group = vim.api.nvim_create_augroup("user_treesitter", { clear = true }),
        pattern = { "lua", "markdown", "python", "vim", "vimdoc" },
        callback = function(event)
          pcall(vim.treesitter.start, event.buf)
        end,
      })
    end,
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
    "mfussenegger/nvim-dap",
    config = function(_, opts) end,
  },

  {
    "mfussenegger/nvim-dap-python",
    ft = { "python" },
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
      local dap = require "dap"
      local dapui = require "dapui"
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

  {
    "neovim/nvim-lspconfig",
    config = function()
      require "configs.lspconfig"
    end,
  },
}
