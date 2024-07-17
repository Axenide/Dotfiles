local M = {}

M.base_30 = {
  white = "#e1e0e0",
  darker_black = "#000000",
  black = "#000000",
  black2 = "#000000",
  one_bg = "#000000",
  one_bg2 = "#9d9c9c",
  one_bg3 = "#9d9c9c",
  grey = "#9d9c9c",
  grey_fg = "#9d9c9c",
  grey_fg2 = "#9d9c9c",
  light_grey = "#9d9c9c",
  red = "#D84231",
  baby_pink = "#D84231",
  pink = "#9FA0A1",
  line = "#9d9c9c",
  green = "#EF4630",
  vibrant_green = "#EF4630",
  nord_blue = "#BB847E",
  blue = "#BB847E",
  yellow = "#CB685C",
  sun = "#CB685C",
  purple = "#9FA0A1",
  dark_purple = "#9FA0A1",
  teal = "#BB847E",
  orange = "#D84231",
  cyan = "#BB847E",
  statusline_bg = "#000000",
  lightbg = "#000000",
  pmenu_bg = "#9d9c9c",
  folder_bg = "#BB847E",
}

M.base_16 = {
  base00 = "#000000",
  base01 = "#000000",
  base02 = "#9d9c9c",
  base03 = "#9d9c9c",
  base04 = "#e1e0e0",
  base05 = "#e1e0e0",
  base06 = "#e1e0e0",
  base07 = "#e1e0e0",
  base08 = "#D84231",
  base09 = "#EF4630",
  base0A = "#CB685C",
  base0B = "#BB847E",
  base0C = "#9FA0A1",
  base0D = "#E5ABA5",
  base0E = "#D84231",
  base0F = "#e1e0e0",
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
