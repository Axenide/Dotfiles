local M = {}

-- In order to disable a default keymap, use
M.disabled = {
  n = {
      ["<leader>h"] = "",
      ["<C-a>"] = ""
  }
}

M.general = {
  n = {
    ["<C-h>"] = {"<cmd> TmuxNavigateLeft<CR>", "window left"},
    ["<C-l>"] = {"<cmd> TmuxNavigateRight<CR>", "window right"},
    ["<C-j>"] = {"<cmd> TmuxNavigateDown<CR>", "window down"},
    ["<C-k>"] = {"<cmd> TmuxNavigateUp<CR>", "window up"},
  }
}

-- Your custom mappings
M.abc = {
  n = {
    -- Undo with CTRL + z
     ["<C-z>"] = {":u <CR>", "Undo"},

    -- Redo with CTRL + y
     ["<C-y>"] = {":redo <CR>", "Redo"},

    -- Move sikipping the current word
     ["<C-Left>"] = {"b", "Move to the beginning of the previous word"},
     ["<C-Right>"] = {"w", "Move to the beginning of the next word"},

    -- Duplicate line with CTRL + d
     ["<C-d>"] = {"yyp", "Duplicate line"},

    -- Move line with ALT + j/k
     ["<A-j>"] = {":m .+1<CR>==", "Move line down"},
     ["<A-k>"] = {":m .-2<CR>==", "Move line up"},

    -- Resize with CTRL + ALT + j/k/h/l
     ["<C-A-j>"] = {":resize -2<CR>", "Resize height -2"},
     ["<C-A-k>"] = {":resize +2<CR>", "Resize height +2"},
     ["<C-A-h>"] = {":vertical resize -2<CR>", "Resize width -2"},
     ["<C-A-l>"] = {":vertical resize +2<CR>", "Resize width +2"},

  },

  i = {
     ["<C-BS>"] = { "<C-w>", "Delete word" , opts = { noremap = true, silent = true }},
    -- ...
  }
}

M.dap = {
  plugin = true,
  n = {
    ["<leader>db"] = {"<cmd> DapToggleBreakpoint <CR>"}
  }
}

M.dap_python = {
  plugin = true,
  n = {
    ["<leader>dpr"] = {
      function()
        require("dap-python").test_method()
      end
    }
  }
}

return M
