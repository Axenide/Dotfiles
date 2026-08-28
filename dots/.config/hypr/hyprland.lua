-- ┌────────────────────────────────────────────┐
-- │                                            │
-- │     ░█▀█░█░█░█▀▀░█▀█░▀█▀░█▀▄░█▀▀░▀░█▀▀     │
-- │     ░█▀█░▄▀▄░█▀▀░█░█░░█░░█░█░█▀▀░░░▀▀█     │
-- │     ░▀░▀░▀░▀░▀▀▀░▀░▀░▀▀▀░▀▀░░▀▀▀░░░▀▀▀     │
-- │     ░█░█░█░█░█▀█░█▀▄░█░░░█▀█░█▀█░█▀▄       │
-- │     ░█▀█░░█░░█▀▀░█▀▄░█░░░█▀█░█░█░█░█       │
-- │     ░▀░▀░░▀░░▀░░░▀░▀░▀▀▀░▀░▀░▀░▀░▀▀░       │
-- │                                            │
-- └────────────────────────────────────────────┘

-- https://github.com/Axenide/Dotfiles

-- Monitor configuration
hl.monitor({ output = "", mode = "preferred", position = "auto", scale = "auto" })
hl.monitor({ output = "TABMOON", mode = "1920x1200@60", position = "auto-center-down", scale = 1.5 })

-- Source Lua config modules
dofile(os.getenv("HOME") .. "/.config/hypr/source/environment.lua")
dofile(os.getenv("HOME") .. "/.config/hypr/source/appearance.lua")
dofile(os.getenv("HOME") .. "/.config/hypr/source/input.lua")
dofile(os.getenv("HOME") .. "/.config/hypr/source/misc.lua")
dofile(os.getenv("HOME") .. "/.config/hypr/source/windowrules.lua")
dofile(os.getenv("HOME") .. "/.config/hypr/source/binds.lua")
dofile(os.getenv("HOME") .. "/.config/hypr/source/autostart.lua")

-- Layer rules (Hyprland 0.55 Lua API)
dofile(os.getenv("HOME") .. "/.config/hypr/source/colors.lua")

-- Ambxst
loadfile(os.getenv("HOME") .. "/.local/share/ambxst/hyprland.lua")()

-- OVERRIDES
-- Down here you can write or source anything that you want to override from Ambxst's settings.

