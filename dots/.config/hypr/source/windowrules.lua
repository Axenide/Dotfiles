hl.window_rule({
	name = "windowrule-1",
	float = true,
	match = { class = "^(org.gnome.Calculator)$" },
})

hl.window_rule({
	name = "windowrule-2",
	float = true,
	move = { 1492, 839 },
	size = { 427, 240 },
	pin = true,
	match = { title = "^(Picture-in-Picture)$" },
})

hl.window_rule({
	name = "windowrule-3",
	no_blur = true,
	match = { class = "^(fl64.exe)$" },
})

hl.window_rule({
	name = "windowrule-4",
	no_screen_share = true,
	-- no_screen_share = false,
	match = { class = "^(librewolf)$" },
})

hl.layer_rule({
	name = "layerrule-1",
	no_anim = true,
	match = { namespace = "selection" },
})

hl.window_rule({
	name = "windowrule-5",
	idle_inhibit = "always",
	fullscreen = true,
	match = { fullscreen = 1 },
})

hl.window_rule({
	name = "windowrule-6",
	rounding = false,
	border_size = 0,
	no_shadow = true,
	match = { class = "^Audacious$" },
})

hl.layer_rule({
	name = "layerrule-2",
	blur = true,
	ignore_alpha = 0.4,
	match = { namespace = "fabric" },
})

hl.layer_rule({
	name = "ambxst",
	blur = true,
	blur_popups = true,
	ignore_alpha = 0.5,
	no_anim = true,
	match = { namespace = "ambxst" },
})

hl.layer_rule({
	name = "ambxst-2",
	blur = true,
	blur_popups = true,
	no_anim = true,
	match = { namespace = "^ambxst:(overview|presets)$" },
})
