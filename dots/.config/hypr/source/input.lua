hl.config({
  input = {
    kb_layout = "us",
    kb_variant = "altgr-intl",
    follow_mouse = 1,
    sensitivity = 0,
    touchpad = {
      natural_scroll = true,
      scroll_factor = 0.25
    }
  }
})

hl.device({
  name = "wacom-intuos-s-pen",
  output = "HDMI-A-1"
})
