hl.config({
  misc = {
    disable_hyprland_logo = true,
    disable_splash_rendering = true,
    focus_on_activate = true,
    allow_session_lock_restore = true,
    middle_click_paste = false,
    session_lock_xray = true
  },
  render = {
    direct_scanout = false
  },
  dwindle = {
    preserve_split = true
  },
  scrolling = {
    fullscreen_on_one_column = true,
    column_width = 0.5,
    explicit_column_widths = "0.5,1.0"
  },
  cursor = {
    no_hardware_cursors = 2,
    no_warps = true
  },
  opengl = {
    nvidia_anti_flicker = true
  }
})

-- permission is hyprlang-only (no Lua API yet)
-- permission = /usr/(bin|local/bin)/hyprpm, plugin, allow
