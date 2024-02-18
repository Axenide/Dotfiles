#!/bin/bash

theme="$HOME/.config/rofi/screenshot/style.rasi"

# options to be displayed
option0="area"
option1="cliparea"
option2="screen"
option3="window"
option4="ocr-area"

# options to be displyed
options="$option0\n$option1\n$option2\n$option3\n$option4"

selected="$(echo -e "$options" | rofi -lines 4 -dmenu -p "󰹑 Screenshot" -theme ${theme} )"
case $selected in
$option0)
	grim -g "$(slurp)" $(xdg-user-dir)/Pictures/grim/$(date +'%s_grim.png')
	;;
$option1)
	grim -g "$(slurp)" - | wl-copy
	;;
$option2)
	sleep 0.5s && grim $(xdg-user-dir)/Pictures/grim/$(date +'%s_grim.png')
	;;
$option3)
	sleep 0.5s && grim -g "$(hyprctl activewindow | grep 'at:' | cut -d':' -f2 | tr -d ' ' | tail -n1) $(hyprctl activewindow | grep 'size:' | cut -d':' -f2 | tr -d ' ' | tail -n1 | sed s/,/x/g)" $(xdg-user-dir)/Pictures/grim/$(
		date +'%s_grim.png'
	)
	;;
$option4)
	grim -g "$(slurp)" - | tesseract - - | wl-copy
	;;
esac
