-- Hyprland 0.55 Lua Keybindings

local mainMod = "SUPER"
local browser = "zen-browser"

-- Close active window
hl.bind(mainMod .. " + C", hl.dsp.window.close())

-- Exit Hyprland
hl.bind(mainMod .. " + SHIFT + escape", hl.dsp.exit())

-- File manager
hl.bind(mainMod .. " + E", hl.dsp.exec_cmd("uwsm app -- nautilus"))
hl.bind(mainMod .. " + SHIFT + E", hl.dsp.exec_cmd("uwsm app -- kitty -1 -e yazi"))

-- Browser
hl.bind(mainMod .. " + W", hl.dsp.exec_cmd("uwsm-app " .. browser))
hl.bind(mainMod .. " + SHIFT + W", hl.dsp.exec_cmd("uwsm-app " .. browser .. " --private-window"))

-- Toggle floating
hl.bind(mainMod .. " + space", hl.dsp.window.float({ action = "toggle" }))

-- Pseudo mode (dwindle)
hl.bind(mainMod .. " + P", hl.dsp.window.pseudo())

-- Rotate split
hl.bind(mainMod .. " + SHIFT + D", function() if hl.get_active_workspace().tiled_layout == "dwindle" then hl.dsp.layout("rotatesplit") end end)

-- Fullscreen screenshot
hl.bind("Print", hl.dsp.exec_cmd("hyprshot -z -m output -f Screenshots/$(date +%Y-%m-%d-%H-%M-%S).png"))
hl.bind("SHIFT + Print", hl.dsp.exec_cmd("hyprshot -z -m output --clipboard-only"))

-- Fullscreen toggle
hl.bind(mainMod .. " + F", hl.dsp.window.fullscreen())
hl.bind(mainMod .. " + CTRL + F", hl.dsp.window.fullscreen({ mode = 0 }))
hl.bind(mainMod .. " + SHIFT + F", hl.dsp.window.fullscreen({ mode = 1 }))

-- Start Kitty terminal
hl.bind(mainMod .. " + RETURN", hl.dsp.exec_cmd("uwsm-app $(kitty -1)"))
hl.bind(mainMod .. " + SHIFT + RETURN", hl.dsp.exec_cmd("[float] uwsm-app $(kitty -1)"))
hl.bind(mainMod .. " + ALT + RETURN", hl.dsp.exec_cmd("uwsm-app $(bash ~/.config/kitty/slurp.sh)"))

-- Pin a window
hl.bind(mainMod .. " + Y", hl.dsp.window.pin({ action = "toggle" }))

-- Center window
hl.bind(mainMod .. " + G", hl.dsp.window.center())

-- Move floating window (fine-grained)
hl.bind(mainMod .. " + SHIFT + ALT + Left", hl.dsp.window.move({ x = -4, y = 0 }))
hl.bind(mainMod .. " + SHIFT + ALT + Right", hl.dsp.window.move({ x = 4, y = 0 }))
hl.bind(mainMod .. " + SHIFT + ALT + Up", hl.dsp.window.move({ x = 0, y = -4 }))
hl.bind(mainMod .. " + SHIFT + ALT + Down", hl.dsp.window.move({ x = 0, y = 4 }))

-- VIM-LIKE fine move
hl.bind(mainMod .. " + SHIFT + ALT + H", hl.dsp.window.move({ x = -10, y = 0 }))
hl.bind(mainMod .. " + SHIFT + ALT + L", hl.dsp.window.move({ x = 10, y = 0 }))
hl.bind(mainMod .. " + SHIFT + ALT + K", hl.dsp.window.move({ x = 0, y = -10 }))
hl.bind(mainMod .. " + SHIFT + ALT + J", hl.dsp.window.move({ x = 0, y = 10 }))