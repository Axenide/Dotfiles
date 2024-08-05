local M = {}

M.base_30 = {
  white = "#aeb8be",
  darker_black = "#0a0909",
  black = "#0a0909",
  black2 = "#0a0909",
  one_bg = "#0a0909",
  one_bg2 = "#798085",
  one_bg3 = "#798085",
  grey = "#798085",
  grey_fg = "#798085",
  grey_fg2 = "#798085",
  light_grey = "#798085",
  red = "#B36257",
  baby_pink = "#B36257",
  pink = "#847E82",
  line = "#798085",
  green = "#C6887A",
  vibrant_green = "#C6887A",
  nord_blue = "#6B7D88",
  blue = "#6B7D88",
  yellow = "#59778C",
  sun = "#59778C",
  purple = "#847E82",
  dark_purple = "#847E82",
  teal = "#6B7D88",
  orange = "#B36257",
  cyan = "#6B7D88",
  statusline_bg = "#0a0909",
  lightbg = "#0a0909",
  pmenu_bg = "#798085",
  folder_bg = "#6B7D88",
}

M.base_16 = {
  base00 = "#0a0909",
  base01 = "#0a0909",
  base02 = "#798085",
  base03 = "#798085",
  base04 = "#aeb8be",
  base05 = "#aeb8be",
  base06 = "#aeb8be",
  base07 = "#aeb8be",
  base08 = "#B36257",
  base09 = "#C6887A",
  base0A = "#59778C",
  base0B = "#6B7D88",
  base0C = "#847E82",
  base0D = "#5F8093",
  base0E = "#B36257",
  base0F = "#aeb8be",
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
