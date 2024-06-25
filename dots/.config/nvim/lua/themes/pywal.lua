
local M = {}

M.base_30 = {
  white = "#c7c7c7",
  darker_black = "#1f1f20",
  black = "#1f1f20", --  nvim bg
  black2 = "#1f1f20",
  one_bg = "#1f1f20",
  one_bg2 = "#575757",
  one_bg3 = "#1f1f20",
  grey = "#575757",
  grey_fg = "#575757",
  grey_fg2 = "#575757",
  light_grey = "#575757",
  red = "#9d9ea2",
  baby_pink = "#9d9ea2",
  pink = "#ab596b",
  line = "#575757", -- for lines like vertsplit
  green = "#4956a9",
  vibrant_green = "#4956a9",
  nord_blue = "#9550a6",
  blue = "#9550a6",
  yellow = "#6755aa",
  sun = "#6755aa",
  purple = "#ab596b",
  dark_purple = "#ab596b",
  teal = "#b70d31",
  orange = "#6755aa",
  cyan = "#b70d31",
  statusline_bg = "#1f1f20",
  lightbg = "#1f1f20",
  pmenu_bg = "#4956a9",
  folder_bg = "#9550a6",
}

M.base_16 = {
  base00 = "#1f1f20",
  base01 = "#1f1f20",
  base02 = "#575757",
  base03 = "#575757",
  base04 = "#c7c7c7",
  base05 = "#c7c7c7",
  base06 = "#c7c7c7",
  base07 = "#c7c7c7",
  base08 = "#9d9ea2",
  base09 = "#6755aa",
  base0A = "#6755aa",
  base0B = "#4956a9",
  base0C = "#b70d31",
  base0D = "#9550a6",
  base0E = "#ab596b",
  base0F = "#c7c7c7",
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
