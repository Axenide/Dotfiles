
local M = {}

M.base_30 = {
  white = "#dbd2d2",
  darker_black = "#02131A",
  black = "#02131A", --  nvim bg
  black2 = "#02131A",
  one_bg = "#02131A",
  one_bg2 = "#999393",
  one_bg3 = "#02131A",
  grey = "#999393",
  grey_fg = "#999393",
  grey_fg2 = "#999393",
  light_grey = "#999393",
  red = "#575A60",
  baby_pink = "#575A60",
  pink = "#7A858B",
  line = "#999393", -- for lines like vertsplit
  green = "#995E63",
  vibrant_green = "#995E63",
  nord_blue = "#937D82",
  blue = "#937D82",
  yellow = "#727C83",
  sun = "#727C83",
  purple = "#7A858B",
  dark_purple = "#7A858B",
  teal = "#9E9DA1",
  orange = "#727C83",
  cyan = "#9E9DA1",
  statusline_bg = "#02131A",
  lightbg = "#02131A",
  pmenu_bg = "#995E63",
  folder_bg = "#937D82",
}

M.base_16 = {
  base00 = "#02131A",
  base01 = "#02131A",
  base02 = "#999393",
  base03 = "#999393",
  base04 = "#dbd2d2",
  base05 = "#dbd2d2",
  base06 = "#dbd2d2",
  base07 = "#dbd2d2",
  base08 = "#575A60",
  base09 = "#727C83",
  base0A = "#727C83",
  base0B = "#995E63",
  base0C = "#9E9DA1",
  base0D = "#937D82",
  base0E = "#7A858B",
  base0F = "#dbd2d2",
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
