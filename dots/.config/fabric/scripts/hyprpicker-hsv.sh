#!/bin/bash

# Copy the color to the clipboard
echo -n "$(hyprpicker -n -f hsv)" | wl-copy -n

# Create a temporal 64x64 PNG file with the color in /tmp using convert
magick -size 64x64 xc:"hsv($(wl-paste))" /tmp/color.png

# Send a notification using the file as an icon
notify-send "HSV color picked" "hsv($(wl-paste))" -i /tmp/color.png -a "Hyprpicker"

# Remove the temporal file
rm /tmp/color.png

# Exit
exit 0
