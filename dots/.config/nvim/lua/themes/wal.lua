local M = {}

M.base_30 = {
  white = "#eac094",
  darker_black = "#0f1013",
  black = "#0f1013",
  black2 = "#0f1013",
  one_bg = "#0f1013",
  one_bg2 = "#a38667",
  one_bg3 = "#a38667",
  grey = "#a38667",
  grey_fg = "#a38667",
  grey_fg2 = "#a38667",
  light_grey = "#a38667",
  red = "#8C3D45",
  baby_pink = "#8C3D45",
  pink = "#E45C58",
  line = "#a38667",
  green = "#91444B",
  vibrant_green = "#91444B",
  nord_blue = "#D05156",
  blue = "#D05156",
  yellow = "#B04A4F",
  sun = "#B04A4F",
  purple = "#E45C58",
  dark_purple = "#E45C58",
  teal = "#D05156",
  orange = "#8C3D45",
  cyan = "#D05156",
  statusline_bg = "#0f1013",
  lightbg = "#0f1013",
  pmenu_bg = "#a38667",
  folder_bg = "#D05156",
}

M.base_16 = {
  base00 = "#0f1013",
  base01 = "#0f1013",
  base02 = "#a38667",
  base03 = "#a38667",
  base04 = "#eac094",
  base05 = "#eac094",
  base06 = "#eac094",
  base07 = "#eac094",
  base08 = "#8C3D45",
  base09 = "#91444B",
  base0A = "#B04A4F",
  base0B = "#D05156",
  base0C = "#E45C58",
  base0D = "#E86E52",
  base0E = "#8C3D45",
  base0F = "#eac094",
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
