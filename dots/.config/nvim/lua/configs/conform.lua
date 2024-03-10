local options = {
  lsp_fallback = true,

  formatters_by_ft = {
    lua = { "stylua" },
  },
}

require("conform").setup(options)
