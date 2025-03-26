local M = {}

local lighten = require("base46.colors").change_hex_lightness

M.base_30 = {
	white = "{{colors.on_background.default.hex}}",
	black = "{{colors.background.default.hex | set_lightness: -5.0}}",
	darker_black = lighten("{{colors.background.default.hex | set_lightness: -5.0}}", -3),
	black2 = lighten("{{colors.background.default.hex | set_lightness: -5.0}}", 6),
	one_bg = lighten("{{colors.background.default.hex | set_lightness: -5.0}}", 10),
	one_bg2 = lighten("{{colors.background.default.hex | set_lightness: -5.0}}", 16),
	one_bg3 = lighten("{{colors.background.default.hex | set_lightness: -5.0}}", 22),
	grey = "{{colors.surface_variant.default.hex}}",
	grey_fg = lighten("{{colors.surface_variant.default.hex}}", -10),
	grey_fg2 = lighten("{{colors.surface_variant.default.hex}}", -20),
	light_grey = "{{colors.outline.default.hex}}",
	red = "{{colors.error.default.hex}}",
	baby_pink = lighten("{{colors.error.default.hex}}", 10),
	pink = "{{colors.tertiary.default.hex}}",
	line = "{{colors.outline.default.hex}}",
	green = "{{colors.secondary.default.hex}}",
	vibrant_green = lighten("{{colors.secondary.default.hex}}", 10),
	blue = "{{colors.primary.default.hex}}",
	nord_blue = lighten("{{colors.primary.default.hex}}", 10),
	yellow = lighten("{{colors.tertiary.default.hex}}", 10),
	sun = lighten("{{colors.tertiary.default.hex}}", 20),
	purple = "{{colors.tertiary.default.hex}}",
	dark_purple = lighten("{{colors.tertiary.default.hex}}", -10),
	teal = "{{colors.secondary_container.default.hex}}",
	orange = "{{colors.error.default.hex}}",
	cyan = "{{colors.secondary.default.hex}}",
	statusline_bg = lighten("{{colors.background.default.hex | set_lightness: -5.0}}", 6),
	pmenu_bg = "{{colors.surface_variant.default.hex}}",
	folder_bg = lighten("{{colors.primary_fixed_dim.default.hex}}", 0),
	lightbg = lighten("{{colors.background.default.hex | set_lightness: -5.0}}", 10),
}

M.base_16 = {
	base00 = "{{colors.surface.default.hex | set_lightness: -5.0}}",
	base01 = lighten("{{colors.surface_variant.default.hex}}", 0),
	base02 = "{{colors.secondary_fixed_dim.default.hex}}",
	base03 = lighten("{{colors.outline.default.hex}}", 0),
	base04 = lighten("{{colors.on_surface_variant.default.hex}}", 0),
	base05 = "{{colors.on_surface.default.hex}}",
	base06 = lighten("{{colors.on_surface.default.hex}}", 0),
	base07 = "{{colors.surface.default.hex | set_lightness: -5.0}}",
	base08 = lighten("{{colors.error.default.hex}}", -10),
	base09 = "{{colors.tertiary.default.hex}}",
	base0A = "{{colors.primary.default.hex}}",
	base0B = "{{colors.tertiary_fixed.default.hex}}",
	base0C = "{{colors.primary_fixed_dim.default.hex}}",
	base0D = lighten("{{colors.primary_container.default.hex}}", 20),
	base0E = "{{colors.on_primary_container.default.hex}}",
	base0F = "{{colors.inverse_surface.default.hex}}",
}

M.type = "dark" -- or "light" depending on your theme

M.polish_hl = {
	defaults = {
		Comment = {
			italic = true,
			fg = M.base_16.base03,
		},
	},
	Syntax = {
		String = {
			fg = "{{colors.tertiary.default.hex}}",
		},
	},
	treesitter = {
		["@comment"] = {
			fg = M.base_16.base03,
		},
		["@string"] = {
			fg = "{{colors.tertiary.default.hex}}",
		},
	},
}

return M
