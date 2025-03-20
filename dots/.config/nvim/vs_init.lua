vim.g.mapleader = " "

local vscode = require "vscode"

vim.keymap.set("n", "<leader>c", ":e ~/.config/nvim/vs_init.lua<CR>", { noremap = true, silent = true })

vim.keymap.set("n", "H", ":bprevious<CR>", { noremap = true, silent = true })
vim.keymap.set("n", "L", ":bnext<CR>", { noremap = true, silent = true })

vim.keymap.set("n", "<leader>v", ":vsplit<CR>", { noremap = true, silent = true })
vim.keymap.set("n", "<leader>s", ":split<CR>", { noremap = true, silent = true })

vim.keymap.set("n", "<leader>h", function()
  vscode.action "workbench.action.focusLeftGroup"
end, { noremap = true, silent = true })
vim.keymap.set("n", "<leader>j", function()
  vscode.action "workbench.action.focusBelowGroup"
end, { noremap = true, silent = true })
vim.keymap.set("n", "<leader>k", function()
  vscode.action "workbench.action.focusAboveGroup"
end, { noremap = true, silent = true })
vim.keymap.set("n", "<leader>l", function()
  vscode.action "workbench.action.focusRightGroup"
end, { noremap = true, silent = true })

vim.keymap.set("n", "<leader>w", ":w!<CR>", { noremap = true, silent = true })
vim.keymap.set("n", "<leader>x", function()
  vscode.action "workbench.action.closeActiveEditor"
end, { noremap = true, silent = true })

vim.keymap.set("n", "[d", function()
  vscode.action "editor.action.marker.prev"
end, { noremap = true, silent = true })
vim.keymap.set("n", "]d", function()
  vscode.action "editor.action.marker.next"
end, { noremap = true, silent = true })

vim.keymap.set("n", "<leader>ca", function()
  vscode.action "editor.action.quickFix"
end, { noremap = true, silent = true })
vim.keymap.set("n", "<leader>ff", function()
  vscode.action "workbench.action.quickOpen"
end, { noremap = true, silent = true })
vim.keymap.set("n", "<leader>fw", function()
  vscode.action "workbench.action.findInFiles"
end, { noremap = true, silent = true })

vim.keymap.set("n", "<leader>p", function()
  vscode.action "editor.action.formatDocument"
end, { noremap = true, silent = true })

vim.keymap.set("n", "gh", function()
  vscode.action "editor.action.showDefinitionPreviewHover"
end, { noremap = true, silent = true })

vim.keymap.set("n", "J", function()
  vscode.action "editor.action.moveLinesDownAction"
end, { noremap = true, silent = true })
vim.keymap.set("n", "K", function()
  vscode.action "editor.action.moveLinesUpAction"
end, { noremap = true, silent = true })

vim.keymap.set("n", "<leader>/", function()
  vscode.action "editor.action.commentLine"
end, { noremap = true, silent = true })
vim.keymap.set("n", "<leader>e", function()
  vscode.action "workbench.view.explorer"
end, { noremap = true, silent = true })
vim.keymap.set("n", "<leader>th", function()
  vscode.action "workbench.action.selectTheme"
end, { noremap = true, silent = true })

vim.keymap.set("n", "<C-d>", function()
  vscode.action "editor.action.copyLinesDownAction"
end, { noremap = true, silent = true })

vim.keymap.set("v", "<", function()
  vscode.action "editor.action.outdentLines"
end, { noremap = true, silent = true })
vim.keymap.set("v", ">", function()
  vscode.action "editor.action.indentLines"
end, { noremap = true, silent = true })

vim.opt.clipboard = "unnamedplus"
