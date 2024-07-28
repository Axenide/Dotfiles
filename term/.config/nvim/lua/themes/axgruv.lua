local M = {}

M.base_30 = {
  white = "#D9C9A7",
  darker_black = "#0A0B0C",
  black = "#000000", --  nvim bg
  black2 = "#1B1D1D",
  one_bg = "#0A0B0C",
  one_bg2 = "#3C3D3E",
  one_bg3 = "#0A0B0C",
  grey = "#494B4B",
  grey_fg = "#525454",
  grey_fg2 = "#525354",
  light_grey = "#626464",
  red = "#F35A4C",
  baby_pink = "#CD5259",
  pink = "#FF75A0",
  line = "#343738", -- for lines like vertsplit
  green = "#A0B754",
  vibrant_green = "#A9B665",
  nord_blue = "#799AA3",
  blue = "#59899A",
  yellow = "#D6A74B",
  sun = "#E5B750",
  purple = "#A3A0BE",
  dark_purple = "#AD80A2",
  teal = "#749689",
  orange = "#E78A4E",
  cyan = "#82B3A8",
  statusline_bg = "#0A0B0C",
  lightbg = "#1B1D1D",
  pmenu_bg = "#86AC8D",
  folder_bg = "#70919B",
}

M.base_16 = {
  base00 = "#000000",
  base01 = "#343333",
  base02 = "#3C3B3B",
  base03 = "#444343",
  base04 = "#C8B695",
  base05 = "#CABA9B",
  base06 = "#D7C7A5",
  base07 = "#E1D4B2",
  base08 = "#F35A4C",
  base09 = "#F28533",
  base0A = "#EDBE57",
  base0B = "#B0B845",
  base0C = "#8AB87D",
  base0D = "#80A99D",
  base0E = "#D3869B",
  base0F = "#D65D0E",
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
