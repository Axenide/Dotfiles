local M = {}

M.base_30 = {
  white = "#b6b6c7",
  darker_black = "#0d0d11",
  black = "#0d0d11",
  black2 = "#0d0d11",
  one_bg = "#0d0d11",
  one_bg2 = "#7f7f8b",
  one_bg3 = "#7f7f8b",
  grey = "#7f7f8b",
  grey_fg = "#7f7f8b",
  grey_fg2 = "#7f7f8b",
  light_grey = "#7f7f8b",
  red = "#413E62",
  baby_pink = "#413E62",
  pink = "#5E5B8A",
  line = "#7f7f8b",
  green = "#3E415D",
  vibrant_green = "#3E415D",
  nord_blue = "#4B4A6F",
  blue = "#4B4A6F",
  yellow = "#4D4D64",
  sun = "#4D4D64",
  purple = "#5E5B8A",
  dark_purple = "#5E5B8A",
  teal = "#4B4A6F",
  orange = "#413E62",
  cyan = "#4B4A6F",
  statusline_bg = "#0d0d11",
  lightbg = "#0d0d11",
  pmenu_bg = "#7f7f8b",
  folder_bg = "#4B4A6F",
}

M.base_16 = {
  base00 = "#0d0d11",
  base01 = "#0d0d11",
  base02 = "#7f7f8b",
  base03 = "#7f7f8b",
  base04 = "#b6b6c7",
  base05 = "#b6b6c7",
  base06 = "#b6b6c7",
  base07 = "#b6b6c7",
  base08 = "#413E62",
  base09 = "#3E415D",
  base0A = "#4D4D64",
  base0B = "#4B4A6F",
  base0C = "#5E5B8A",
  base0D = "#6D6C8F",
  base0E = "#413E62",
  base0F = "#b6b6c7",
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
