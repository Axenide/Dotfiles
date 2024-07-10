local M = {}

M.base_30 = {
  white = "#cbcfe2",
  darker_black = "#0a0a0f",
  black = "#0a0a0f",
  black2 = "#0a0a0f",
  one_bg = "#0a0a0f",
  one_bg2 = "#8e909e",
  one_bg3 = "#8e909e",
  grey = "#8e909e",
  grey_fg = "#8e909e",
  grey_fg2 = "#8e909e",
  light_grey = "#8e909e",
  red = "#5E637C",
  baby_pink = "#5E637C",
  pink = "#979EC1",
  line = "#8e909e",
  green = "#6D738E",
  vibrant_green = "#6D738E",
  nord_blue = "#8C93B4",
  blue = "#8C93B4",
  yellow = "#7D83A1",
  sun = "#7D83A1",
  purple = "#979EC1",
  dark_purple = "#979EC1",
  teal = "#8C93B4",
  orange = "#5E637C",
  cyan = "#8C93B4",
  statusline_bg = "#0a0a0f",
  lightbg = "#0a0a0f",
  pmenu_bg = "#8e909e",
  folder_bg = "#8C93B4",
}

M.base_16 = {
  base00 = "#0a0a0f",
  base01 = "#0a0a0f",
  base02 = "#8e909e",
  base03 = "#8e909e",
  base04 = "#cbcfe2",
  base05 = "#cbcfe2",
  base06 = "#cbcfe2",
  base07 = "#cbcfe2",
  base08 = "#5E637C",
  base09 = "#6D738E",
  base0A = "#7D83A1",
  base0B = "#8C93B4",
  base0C = "#979EC1",
  base0D = "#9CA4C8",
  base0E = "#5E637C",
  base0F = "#cbcfe2",
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
