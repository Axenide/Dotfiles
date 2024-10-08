local M = {{}}

local lighten = require("base46.colors").change_hex_lightness

M.base_30 = {{
  white = "{color7}",
  darker_black = lighten("{color0}", -3),
  black = "{color0}",
  black2 = lighten("{color0}", 6),
  one_bg = lighten("{color0}", 10),
  grey = lighten("{color0}", 40),
  light_grey = "{color8}",
  red = "{color1}",
  baby_pink = "{color9}",
  pink = "{color13}",
  line = "{color8}",
  green = "{color2}",
  vibrant_green = "{color2}",
  nord_blue = "{color4}",
  blue = "{color4}",
  yellow = "{color3}",
  sun = lighten("{color3}", 6),
  purple = "{color13}",
  dark_purple = "{color13}",
  teal = "{color4}",
  orange = "{color1}",
  cyan = "{color4}",
  pmenu_bg = "{color8}",
  folder_bg = "{color4}",
}}

M.base_30.statusline_bg = M.base_30.black2
M.base_30.lightbg = M.base_30.one_bg
M.base_30.one_bg2 = lighten(M.base_30.one_bg, 6)
M.base_30.one_bg3 = lighten(M.base_30.one_bg2, 6)
M.base_30.grey_fg = lighten(M.base_30.grey, 10)
M.base_30.grey_fg2 = lighten(M.base_30.grey, 5)

M.base_16 = {{
  base00 = "{color0}",
  base01 = "{color0}",
  base02 = "{color8}",
  base03 = "{color8}",
  base04 = "{color7}",
  base05 = "{color7}",
  base06 = "{color15}",
  base07 = "{color15}",
  base08 = "{color1}",
  base09 = "{color2}",
  base0A = "{color3}",
  base0B = "{color4}",
  base0C = "{color5}",
  base0D = "{color6}",
  base0E = "{color1}",
  base0F = "{color15}",
}}

M.type = "dark"

M.polish_hl = {{
  Operator = {{
    fg = M.base_30.nord_blue,
  }},

  ["@operator"] = {{
    fg = M.base_30.nord_blue,
  }},
}}

return M
