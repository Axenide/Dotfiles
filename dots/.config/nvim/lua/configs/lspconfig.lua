local lspconfig = require("lspconfig")

lspconfig.pyright.setup({
  on_attach,
  capabilities,
  filetypes = {"python"},
})
