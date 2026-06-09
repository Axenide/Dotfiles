require("nvchad.configs.lspconfig").defaults()

local servers = { "html", "cssls", "pyright", "qmlls" }
local nvlsp = require "nvchad.configs.lspconfig"

for _, lsp in ipairs(servers) do
  local opts = {
    on_attach = nvlsp.on_attach,
    on_init = nvlsp.on_init,
    capabilities = nvlsp.capabilities,
  }

  if lsp == "qmlls" then
    opts.cmd = { "qmlls6" }
  end

  if lsp == "pyright" then
    opts.settings = {
      python = {
        analysis = {
          autoSearchPaths = true,
          useLibraryCodeForTypes = true,
          diagnosticMode = "workspace",
        },
      },
    }
  end

  vim.lsp.config(lsp, opts)
end

vim.lsp.enable(servers)
