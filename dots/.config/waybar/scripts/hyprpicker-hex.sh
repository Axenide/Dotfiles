#!/bin/bash

# Execute hyprpicker and save the output to a variable
hyprpicker -a -n -f hex && sleep 0.1

# Create a temporal 64x64 PNG file with the color in /tmp using convert
convert -size 64x64 xc:"$(wl-paste)" /tmp/color.png

# Send a notification using the file as an icon
notify-send "Color picked" "$(wl-paste)" -i /tmp/color.png

# Remove the temporal file
rm /tmp/color.png

# Exit
exit 0
