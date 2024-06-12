local M = {}

M.base_30 = {
  white = "#E8E3E3",
  darker_black = "#000000",
  black = "#000000", --  nvim bg
  black2 = "#111111",
  one_bg = "#111111",
  one_bg2 = "#2E2E2E",
  one_bg3 = "#111111",
  grey = "#424242",
  grey_fg = "#424242",
  grey_fg2 = "#424242",
  light_grey = "#424242",
  red = "#B66467",
  baby_pink = "#B66467",
  pink = "#A988B0",
  line = "#2E2E2E", -- for lines like vertsplit
  green = "#8C977D",
  vibrant_green = "#8C977D",
  nord_blue = "#8DA3B9",
  blue = "#8DA3B9",
  yellow = "#D9BC8C",
  sun = "#D9BC8C",
  purple = "#A988B0",
  dark_purple = "#A988B0",
  teal = "#8AA6A2",
  orange = "#D9BC8C",
  cyan = "#8AA6A2",
  statusline_bg = "#111111",
  lightbg = "#111111",
  pmenu_bg = "#8C977D",
  folder_bg = "#8DA3B9",
}

M.base_16 = {
  base00 = "#000000",
  base01 = "#111111",
  base02 = "#2E2E2E",
  base03 = "#424242",
  base04 = "#BBB6B6",
  base05 = "#E8E3E3",
  base06 = "#E8E3E3",
  base07 = "#E8E3E3",
  base08 = "#B66467",
  base09 = "#D9BC8C",
  base0A = "#D9BC8C",
  base0B = "#8C977D",
  base0C = "#8AA6A2",
  base0D = "#8DA3B9",
  base0E = "#A988B0",
  base0F = "#BBB6B6",
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
