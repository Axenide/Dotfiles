local M = {}

M.base_30 = {
  white = "#d2cddd",
  darker_black = "#100c12",
  black = "#100c12", -- nvim bg
  black2 = "#100c12",
  one_bg = "#100c12",
  one_bg2 = "#8A7497",
  one_bg3 = "#8A5FE2",
  grey = "#6A4AA5",
  grey_fg = "#6A4AA5",
  grey_fg2 = "#6A4AA5",
  light_grey = "#6A4AA5",
  red = "#6A4AA5",
  baby_pink = "#6A4AA5",
  pink = "#8A7497",
  line = "#8A5FE2", -- for lines like vertsplit
  green = "#8F63E7",
  vibrant_green = "#7897AE",
  nord_blue = "#67CC82",
  blue = "#d2cddd",
  yellow = "#938f9a",
  sun = "#6A4AA5",
  purple = "#8A7497",
  dark_purple = "#8A5FE2",
  teal = "#8F63E7",
  orange = "#7897AE",
  cyan = "#67CC82",
  statusline_bg = "#100c12",
  lightbg = "#100c12",
  pmenu_bg = "#938f9a",
  folder_bg = "#67CC82",
}

M.base_16 = {
  base00 = "#100c12",
  base01 = "#6A4AA5",
  base02 = "#8A7497",
  base03 = "#8A5FE2",
  base04 = "#8F63E7",
  base05 = "#7897AE",
  base06 = "#67CC82",
  base07 = "#d2cddd",
  base08 = "#938f9a",
  base09 = "#6A4AA5",
  base0A = "#8A7497",
  base0B = "#8A5FE2",
  base0C = "#8F63E7",
  base0D = "#7897AE",
  base0E = "#67CC82",
  base0F = "#d2cddd",
}

M.type = "dark"

M.polish_hl = {
  Operator = {
    fg = M.base_30.nord_blue,
  },

  ["@operator"] = {
    fg = M.base_30.nord_blue,
  },
}

return M
