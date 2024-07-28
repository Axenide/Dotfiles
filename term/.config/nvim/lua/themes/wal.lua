local M = {}

M.base_30 = {
  white = "#c5c8c8",
  darker_black = "#03030D",
  black = "#03030D",
  black2 = "#03030D",
  one_bg = "#03030D",
  one_bg2 = "#898c8c",
  one_bg3 = "#898c8c",
  grey = "#898c8c",
  grey_fg = "#898c8c",
  grey_fg2 = "#898c8c",
  light_grey = "#898c8c",
  red = "#474C58",
  baby_pink = "#474C58",
  pink = "#7D8288",
  line = "#898c8c",
  green = "#575C67",
  vibrant_green = "#575C67",
  nord_blue = "#777C83",
  blue = "#777C83",
  yellow = "#696F77",
  sun = "#696F77",
  purple = "#7D8288",
  dark_purple = "#7D8288",
  teal = "#777C83",
  orange = "#474C58",
  cyan = "#777C83",
  statusline_bg = "#03030D",
  lightbg = "#03030D",
  pmenu_bg = "#898c8c",
  folder_bg = "#777C83",
}

M.base_16 = {
  base00 = "#03030D",
  base01 = "#03030D",
  base02 = "#898c8c",
  base03 = "#898c8c",
  base04 = "#c5c8c8",
  base05 = "#c5c8c8",
  base06 = "#c5c8c8",
  base07 = "#c5c8c8",
  base08 = "#474C58",
  base09 = "#575C67",
  base0A = "#696F77",
  base0B = "#777C83",
  base0C = "#7D8288",
  base0D = "#8C9295",
  base0E = "#474C58",
  base0F = "#c5c8c8",
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
