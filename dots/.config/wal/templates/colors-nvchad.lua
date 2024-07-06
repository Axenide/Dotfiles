local M = {{}}

M.base_30 = {{
  white = "{color7}",
  darker_black = "{color0}",
  black = "{color0}", -- nvim bg
  black2 = "{color0}",
  one_bg = "{color0}",
  one_bg2 = "{color2}",
  one_bg3 = "{color3}",
  grey = "{color1}",
  grey_fg = "{color1}",
  grey_fg2 = "{color1}",
  light_grey = "{color1}",
  red = "{color1}",
  baby_pink = "{color9}",
  pink = "{color10}",
  line = "{color11}", -- for lines like vertsplit
  green = "{color12}",
  vibrant_green = "{color13}",
  nord_blue = "{color14}",
  blue = "{color15}",
  yellow = "{color8}",
  sun = "{color9}",
  purple = "{color10}",
  dark_purple = "{color11}",
  teal = "{color12}",
  orange = "{color13}",
  cyan = "{color14}",
  statusline_bg = "{color0}",
  lightbg = "{color0}",
  pmenu_bg = "{color8}",
  folder_bg = "{color14}",
}}

M.base_16 = {{
  base00 = "{color0}",
  base01 = "{color1}",
  base02 = "{color2}",
  base03 = "{color3}",
  base04 = "{color4}",
  base05 = "{color5}",
  base06 = "{color6}",
  base07 = "{color7}",
  base08 = "{color8}",
  base09 = "{color9}",
  base0A = "{color10}",
  base0B = "{color11}",
  base0C = "{color12}",
  base0D = "{color13}",
  base0E = "{color14}",
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
