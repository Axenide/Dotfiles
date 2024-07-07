local M = {}

M.base_30 = {
  white = "#e19e9b",
  darker_black = "#03120B",
  black = "#03120B",
  black2 = "#03120B",
  one_bg = "#03120B",
  one_bg2 = "#9d6e6c",
  one_bg3 = "#9d6e6c",
  grey = "#9d6e6c",
  grey_fg = "#9d6e6c",
  grey_fg2 = "#9d6e6c",
  light_grey = "#9d6e6c",
  red = "#8F2835",
  baby_pink = "#8F2835",
  pink = "#9E3245",
  line = "#9d6e6c",
  green = "#AB2734",
  vibrant_green = "#AB2734",
  nord_blue = "#F82C38",
  blue = "#F82C38",
  yellow = "#D9222E",
  sun = "#D9222E",
  purple = "#9E3245",
  dark_purple = "#9E3245",
  teal = "#F82C38",
  orange = "#8F2835",
  cyan = "#F82C38",
  statusline_bg = "#03120B",
  lightbg = "#03120B",
  pmenu_bg = "#9d6e6c",
  folder_bg = "#F82C38",
}

M.base_16 = {
  base00 = "#03120B",
  base01 = "#03120B",
  base02 = "#9d6e6c",
  base03 = "#9d6e6c",
  base04 = "#e19e9b",
  base05 = "#e19e9b",
  base06 = "#e19e9b",
  base07 = "#e19e9b",
  base08 = "#8F2835",
  base09 = "#AB2734",
  base0A = "#D9222E",
  base0B = "#F82C38",
  base0C = "#9E3245",
  base0D = "#EB3044",
  base0E = "#8F2835",
  base0F = "#e19e9b",
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
