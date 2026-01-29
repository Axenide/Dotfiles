local options = {
  formatters_by_ft = {
    python = { "isort", "black" },
    lua = { "stylua" },
    css = { "prettier" },
    scss = { "prettier" },
    sass = { "prettier" },
    html = { "prettier" },
    json = { "prettier" },
    html = { "prettier" },
    nix = { "alejandra" },
    bash = { "shfmt" },
    zsh = { "shfmt" },
    sh = { "shfmt" },
  },

  format_on_save = {
    -- These options will be passed to conform.format()
    timeout_ms = 5000,
    lsp_fallback = true,
  },
}

return options
