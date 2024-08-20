#!/bin/bash

source "$HOME/.cache/wal/slurp-args.sh"

theme="$HOME/.config/rofi/screenshot/style.rasi"

# If gpu-screen-recorder is not running, make the variable "option4" be "  Start Recording 󰹑", else "  Stop Recording 󰹑".
if ! pgrep -x "gpu-screen-reco" > /dev/null
then
  option3=""
else
  option3=""
fi

# options to be displayed
option0="󰆞" # Area
option1="" # Fullscreen
option2="󱄺" # OCR
option4="" # Open Folder

# options to be displyed
options="$option0\n$option1\n$option2\n$option3\n$option4"

selected="$(echo -e "$options" | rofi -dmenu -mesg "󰹑  Screenshot" -theme ${theme} )"
case $selected in
$option0)
	grimblast --notify copysave area $XDG_PICTURES_DIR/Screenshots/$(date +%Y-%m-%d-%H-%M-%S).png
	;;
$option1)
  sleep 0.5
	grimblast --notify copysave screen $XDG_PICTURES_DIR/Screenshots/$(date +%Y-%m-%d-%H-%M-%S).png
	;;
$option2)
	grim -g "$(slurp)" - | tesseract -l spa - - | wl-copy
	;;
$option3)
  # If gpu-screen-recorder is not running, start recording, else stop recording.
  if ! pgrep -x "gpu-screen-reco" > /dev/null
  then
    ~/.config/rofi/screenshot/record.sh
  else
    killall -SIGINT gpu-screen-recorder
    notify-send "Recording stopped" "Video saved!" -e -i ~/.config/rofi/screenshot/disk.svg
  fi
  ;;
$option4)
  nautilus $XDG_PICTURES_DIR/Screenshots
  ;;
esac
