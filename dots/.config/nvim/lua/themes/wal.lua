local M = {}

M.base_30 = {
  white = "#f3e4da",
  darker_black = "#0b0c10",
  black = "#0b0c10",
  black2 = "#0b0c10",
  one_bg = "#0b0c10",
  one_bg2 = "#aa9f98",
  one_bg3 = "#aa9f98",
  grey = "#aa9f98",
  grey_fg = "#aa9f98",
  grey_fg2 = "#aa9f98",
  light_grey = "#aa9f98",
  red = "#6D5759",
  baby_pink = "#6D5759",
  pink = "#CDA194",
  line = "#aa9f98",
  green = "#926D69",
  vibrant_green = "#926D69",
  nord_blue = "#CF8F73",
  blue = "#CF8F73",
  yellow = "#CA6A50",
  sun = "#CA6A50",
  purple = "#CDA194",
  dark_purple = "#CDA194",
  teal = "#CF8F73",
  orange = "#6D5759",
  cyan = "#CF8F73",
  statusline_bg = "#0b0c10",
  lightbg = "#0b0c10",
  pmenu_bg = "#aa9f98",
  folder_bg = "#CF8F73",
}

M.base_16 = {
  base00 = "#0b0c10",
  base01 = "#0b0c10",
  base02 = "#aa9f98",
  base03 = "#aa9f98",
  base04 = "#f3e4da",
  base05 = "#f3e4da",
  base06 = "#f3e4da",
  base07 = "#f3e4da",
  base08 = "#6D5759",
  base09 = "#926D69",
  base0A = "#CA6A50",
  base0B = "#CF8F73",
  base0C = "#CDA194",
  base0D = "#F1CFB6",
  base0E = "#6D5759",
  base0F = "#f3e4da",
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
