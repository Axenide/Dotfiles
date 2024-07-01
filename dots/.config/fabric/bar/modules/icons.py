# Parameters
font_family = 'tabler-icons'
font_weight = 'normal'

span = f"<span font-family='{font_family}' font-weight='{font_weight}'>"

# Bar
run = "&#xec2c;"
colorpicker = "&#xebe6;"
media = "&#xf00d;"

# AIchat
reload = "&#xf3ae;"
detach = "&#xea99;"

# Power
lock = "&#xeae2;"
suspend = "&#xece7;"
logout = "&#xeba8;"
reboot = "&#xeb13;"
shutdown = "&#xeb0d;"

# Applets
wifi = "&#xeb52;"
bluetooth = "&#xea37;"
night = "&#xeaf8;"
dnd = "&#xea35;"

wifi_off = "&#xecfa;"
bluetooth_off = "&#xeceb;"
night_off = "&#xf162;"
dnd_off = "&#xece9;"

# Player
pause = "&#xed45;"
play = "&#xed46;"
stop = "&#xed4a;"
skip_back = "&#xed48;"
skip_forward = "&#xed49;"
prev = "&#xed4c;"
next = "&#xed4b;"
shuffle = "&#xf000;"
repeat = "&#xeb72;"
music = "&#xeafc;"

# Volume
vol_off = "&#xf1c3;"
vol_mute = "&#xeb50;"
vol_medium = "&#xeb4f;"
vol_high = "&#xeb51;"

exceptions = ['font_family', 'font_weight', 'span']

def apply_span():
    global_dict = globals()
    for key in global_dict:
        if key not in exceptions and not key.startswith('__'):
            global_dict[key] = f"{span}{global_dict[key]}</span>"

apply_span()
