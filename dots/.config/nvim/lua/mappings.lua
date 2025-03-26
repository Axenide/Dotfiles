require "nvchad.mappings"

-- add yours here

local map = vim.keymap.set

map("n", ";", ":", { desc = "CMD enter command mode" })

map("n", "<leader>fm", function()
  require("conform").format()
end, { desc = "File Format with conform" })

map("i", "jk", "<ESC>", { desc = "Escape insert mode" })

map("n", "<leader>h", "", { desc = "window left" })
map("n", "<C-a>", "", { desc = "" })

map("n", "<C-h>", function()
  vim.cmd "TmuxNavigateLeft"
end, { desc = "window left" })

map("n", "<C-l>", function()
  vim.cmd "TmuxNavigateRight"
end, { desc = "window right" })

map("n", "<C-j>", function()
  vim.cmd "TmuxNavigateDown"
end, { desc = "window down" })

map("n", "<C-k>", function()
  vim.cmd "TmuxNavigateUp"
end, { desc = "window up" })

map("n", "<C-Left>", "b", { desc = "Move to the beginning of the previous word" })
map("n", "<C-Right>", "w", { desc = "Move to the beginning of the next word" })
map("n", "<C-d>", "yyp", { desc = "Duplicate line" })
map("n", "<A-j>", ":m .+1<CR>==", { desc = "Move line down" })
map("n", "<A-k>", ":m .-2<CR>==", { desc = "Move line up" })
map("n", "<C-A-j>", ":resize -2<CR>", { desc = "Resize height -2" })
map("n", "<C-A-k>", ":resize +2<CR>", { desc = "Resize height +2" })
map("n", "<C-A-h>", ":vertical resize -2<CR>", { desc = "Resize width -2" })
map("n", "<C-A-l>", ":vertical resize +2<CR>", { desc = "Resize width +2" })

-- Copilot
map("i", "<A-l>", "copilot#Accept('<CR>')", { noremap = true, silent = true, expr = true, replace_keycodes = false })

map("n", "<leader>zc", ":CopilotChatToggle<CR>", { desc = "Toggle Copilot Chat" })
map("v", "<leader>ze", ":CopilotChatExplain<CR>", { desc = "Explain Code" })
map("v", "<leader>zr", ":CopilotChatReview<CR>", { desc = "Review Code" })
map("v", "<leader>zf", ":CopilotChatFix<CR>", { desc = "Fix Code Issues" })
map("v", "<leader>zo", ":CopilotChatOptimize<CR>", { desc = "Optimize Code" })
map("v", "<leader>zd", ":CopilotChatDocs<CR>", { desc = "Generate Docs" })
map("v", "<leader>zt", ":CopilotChatTests<CR>", { desc = "Generate Tests" })
map("n", "<leader>zm", ":CopilotChatCommit<CR>", { desc = "Generate Commit Message" })
map("v", "<leader>zs", ":CopilotChatCommit<CR>", { desc = "Generate Commit for Selection" })

map("n", "<leader>db", "<cmd> DapToggleBreakpoint <CR>", { desc = "" })

map("n", "<leader>dpr", function()
  require("dap-python").test_method()
end, { desc = "" })

map("n", "<leader>dd", function()
  require("telescope.builtin").lsp_type_definitions()
end, { desc = "Telescope LSP Type Definition" })

-- CTRL + N runs `require('neogen').generate()`
map("n", "<A-n>", function()
  require("neogen").generate()
end, { desc = "Generate docstrings with Neogen" })
