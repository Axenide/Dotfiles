---@type ChadrcConfig 
 local M = {}
 M.ui = {
  theme = 'axgruv',
  hl_override = {
         [ "@variable" ] = { italic = true },
         ["@keyword"] = { italic = true },
         ["@keyword.function"] = { italic = true },
         ["@keyword.return"] = { bold = true },
         ["@function"] = { italic = false },
         ["@operator"] = { bold = true },
         ["@keyword.operator"] = { italic = true },
         ["@parameter"] = { italic = true },
     }
}
 M.plugins = 'custom.plugins'
 M.mappings = require "custom.mappings"
 M.init = require "custom.init"
 return M
