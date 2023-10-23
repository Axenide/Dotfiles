---@type ChadrcConfig 
 local M = {}
 M.ui = {
  theme = 'axgruv',
  hl_override = {
         [ "@variable" ] = { italic = true }
     }
}
 M.plugins = 'custom.plugins'
 M.mappings = require "custom.mappings"
 M.init = require "custom.init"
 return M
