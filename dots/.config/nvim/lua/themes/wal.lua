local M = {}

M.base_30 = {
  white = "#d2cddd",
  darker_black = "#100c12",
  black = "#100c12",
  black2 = "#100c12",
  one_bg = "#100c12",
  one_bg2 = "#938f9a",
  one_bg3 = "#938f9a",
  grey = "#938f9a",
  grey_fg = "#938f9a",
  grey_fg2 = "#938f9a",
  light_grey = "#938f9a",
  red = "#6A4AA5",
  baby_pink = "#6A4AA5",
  pink = "#7897AE",
  line = "#938f9a",
  green = "#8A7497",
  vibrant_green = "#8A7497",
  nord_blue = "#8F63E7",
  blue = "#8F63E7",
  yellow = "#8A5FE2",
  sun = "#8A5FE2",
  purple = "#7897AE",
  dark_purple = "#7897AE",
  teal = "#8F63E7",
  orange = "#6A4AA5",
  cyan = "#8F63E7",
  statusline_bg = "#100c12",
  lightbg = "#100c12",
  pmenu_bg = "#938f9a",
  folder_bg = "#8F63E7",
}

M.base_16 = {
  base00 = "#100c12",
  base01 = "#100c12",
  base02 = "#938f9a",
  base03 = "#938f9a",
  base04 = "#d2cddd",
  base05 = "#d2cddd",
  base06 = "#d2cddd",
  base07 = "#d2cddd",
  base08 = "#6A4AA5",
  base09 = "#8A7497",
  base0A = "#8A5FE2",
  base0B = "#8F63E7",
  base0C = "#7897AE",
  base0D = "#67CC82",
  base0E = "#6A4AA5",
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
