local M = {}

M.base_30 = {
  white = "#b897a6",
  darker_black = "#120f0d",
  black = "#120f0d",
  black2 = "#120f0d",
  one_bg = "#120f0d",
  one_bg2 = "#806974",
  one_bg3 = "#806974",
  grey = "#806974",
  grey_fg = "#806974",
  grey_fg2 = "#806974",
  light_grey = "#806974",
  red = "#503146",
  baby_pink = "#503146",
  pink = "#813A5D",
  line = "#806974",
  green = "#6A3652",
  vibrant_green = "#6A3652",
  nord_blue = "#615D6B",
  blue = "#615D6B",
  yellow = "#4B4954",
  sun = "#4B4954",
  purple = "#813A5D",
  dark_purple = "#813A5D",
  teal = "#615D6B",
  orange = "#503146",
  cyan = "#615D6B",
  statusline_bg = "#120f0d",
  lightbg = "#120f0d",
  pmenu_bg = "#806974",
  folder_bg = "#615D6B",
}

M.base_16 = {
  base00 = "#120f0d",
  base01 = "#120f0d",
  base02 = "#806974",
  base03 = "#806974",
  base04 = "#b897a6",
  base05 = "#b897a6",
  base06 = "#b897a6",
  base07 = "#b897a6",
  base08 = "#503146",
  base09 = "#6A3652",
  base0A = "#4B4954",
  base0B = "#615D6B",
  base0C = "#813A5D",
  base0D = "#823D61",
  base0E = "#503146",
  base0F = "#b897a6",
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
