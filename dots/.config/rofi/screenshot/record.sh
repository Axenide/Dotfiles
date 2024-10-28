#!/bin/bash

theme="$HOME/.config/rofi/screenshot/style.rasi"

sink_device="$(pactl list sources | grep 'Name:' | grep "$(pactl info | grep 'Default Sink' | awk '{print $3}')" | awk '{print $2}')"
source_device="$(pactl list sources | grep 'Name:' | grep "$(pactl info | grep 'Default Source' | awk '{print $3}')" | awk '{print $2}')"

# Combine the two devices into one
pactl unload-module module-null-sink
pactl unload-module module-loopback
pactl load-module module-null-sink sink_name=Combined
pactl load-module module-null-sink sink_name=EmptySink
pactl load-module module-loopback sink=Combined source=$source_device
pactl load-module module-loopback sink=Combined source=$sink_device

# options to be displayed
record=""
gtk="󱕷"
goback="󱞴"

# Set parameters, --mic and --desktop.
mic="false"
desktop="true"

row=0

# Parse the command line arguments
while [[ $# -gt 0 ]]; do
    case "$1" in
        --mic)
            mic="$2"
            shift
            ;;
        --desktop)
            desktop="$2"
            shift
            ;;
        --row)
            row="$2"
            shift
            ;;
        *)
            echo "Unknown argument: $1"
            exit 1
            ;;
    esac
    shift
done

# If mic is true, then set the $device to $source_device
# If desktop is true, then set $device to $sink_device
# If both are true, then set $device to Combined.monitor
# If both are false, then set $device to none

if [ "$mic" = "true" ] && [ "$desktop" = "false" ]; then
    device=$source_device
    micon="󰍬"
    deskon="󰖁"
elif [ "$mic" = "false" ] && [ "$desktop" = "true" ]; then
    device=$sink_device
    micon="󰍭"
    deskon="󰕾"
elif [ "$mic" = "true" ] && [ "$desktop" = "true" ]; then
    device=Combined.monitor
    micon="󰍬"
    deskon="󰕾"
else
    device=EmptySink.monitor
    micon="󰍭"
    deskon="󰖁"
fi

# options to be displayed
options="$record\n$gtk\n$micon\n$deskon\n$goback"

# Función para mostrar la notificación con la cuenta regresiva
show_notification() {
    local remaining_time=$1
    local message=$2
    notify-send "$message" "Starting in $remaining_time..." -t "$remaining_time"000 -e -h string:x-canonical-private-synchronous:countdown -i ~/.config/rofi/screenshot/$remaining_time.svg
}

# Función para la cuenta regresiva
countdown() {
    local seconds=$1
    local message=$2
    while [ $seconds -gt 0 ]; do
        show_notification $seconds "$message"
        sleep 1
        ((seconds--))
    done
    # show_notification "¡Tiempo terminado!"
}

selected="$(echo -e "$options" | rofi -dmenu -mesg "  Recording" -theme ${theme} -selected-row $row )"
case $selected in
$record)
  gpu-screen-recorder -w portal -f 60 -q very_high -ac opus -cr full -a "$device" -o "$XDG_PICTURES_DIR/Screenshots/$(date +%Y-%m-%d-%H-%M-%S).mp4"
	;;
$gtk)
  gpu-screen-recorder-gtk
  ;;
$micon)
  if [ "$mic" = "true" ]; then
    ~/.config/rofi/screenshot/toggle.sh --mic "false" --desktop "$desktop" --row 2
  else
    ~/.config/rofi/screenshot/toggle.sh --mic "true" --desktop "$desktop" --row 2
  fi
  ;;
$deskon)
  if [ "$desktop" = "true" ]; then
    ~/.config/rofi/screenshot/toggle.sh --mic "$mic" --desktop "false" --row 3
  else
    ~/.config/rofi/screenshot/toggle.sh --mic "$mic" --desktop "true" --row 3
  fi
  ;;
$goback)
  ~/.config/rofi/screenshot/screenshot.sh
  ;;
esac
