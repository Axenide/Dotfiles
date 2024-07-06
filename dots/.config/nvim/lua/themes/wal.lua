local M = {}

M.base_30 = {
  white = "#c5b4b9",
  darker_black = "#02131A",
  black = "#02131A", -- nvim bg
  black2 = "#02131A",
  one_bg = "#02131A",
  one_bg2 = "#3B444A",
  one_bg3 = "#5A535A",
  grey = "#623A44",
  grey_fg = "#623A44",
  grey_fg2 = "#623A44",
  light_grey = "#623A44",
  red = "#623A44",
  baby_pink = "#623A44",
  pink = "#3B444A",
  line = "#5A535A", -- for lines like vertsplit
  green = "#913749",
  vibrant_green = "#A35662",
  nord_blue = "#BA606C",
  blue = "#c5b4b9",
  yellow = "#897d81",
  sun = "#623A44",
  purple = "#3B444A",
  dark_purple = "#5A535A",
  teal = "#913749",
  orange = "#A35662",
  cyan = "#BA606C",
  statusline_bg = "#02131A",
  lightbg = "#02131A",
  pmenu_bg = "#897d81",
  folder_bg = "#BA606C",
}

M.base_16 = {
  base00 = "#02131A",
  base01 = "#623A44",
  base02 = "#3B444A",
  base03 = "#5A535A",
  base04 = "#913749",
  base05 = "#A35662",
  base06 = "#BA606C",
  base07 = "#c5b4b9",
  base08 = "#897d81",
  base09 = "#623A44",
  base0A = "#3B444A",
  base0B = "#5A535A",
  base0C = "#913749",
  base0D = "#A35662",
  base0E = "#BA606C",
  base0F = "#c5b4b9",
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
