#!/usr/bin/env bash

# Definir una variable por defecto para la opción "--row"
row_value="0"

# Uso del script
usage() {
  echo "Uso: $0 [--row <valor>]"
  exit 1
}

# Procesar los argumentos y opciones utilizando getopt
OPTS=$(getopt -o r: --long row: -n "$0" -- "$@")
eval set -- "$OPTS"

# Manejar las opciones y argumentos
while true; do
  case "$1" in
    -r | --row)
      row_value="$2"
      shift 2 ;;
    --)
      shift
      break ;;
    *)
      echo "Opción inválida: $1"
      usage ;;
  esac
done

# Verificar si se proporcionó el valor de "--row"
if [ -z "$row_value" ]; then
  echo "Debe proporcionar un valor para la opción --row."
  usage
fi

# Aquí puedes usar la variable $row_value como desees en tu script
echo "El valor de --row es: $row_value"


## Author  : Aditya Shakya (adi1090x)
## Github  : @adi1090x
#
## Applets : Volume

# Import Current Theme
source "$HOME"/.config/rofi/applets/shared/theme.bash
theme="$type/$style"

# Volume Info
mixer="`amixer info Master | grep 'Mixer name' | cut -d':' -f2 | tr -d \',' '`"
speaker="`amixer get Master | tail -n1 | awk -F ' ' '{print $5}' | tr -d '[]'`"
mic="`amixer get Capture | tail -n1 | awk -F ' ' '{print $5}' | tr -d '[]'`"

active=""
urgent=""

# Speaker Info
amixer get Master | grep '\[on\]' &>/dev/null
if [[ "$?" == 0 ]]; then
	active="-a 1"
	stext='Unmuted'
	sicon='󰕾'
else
	urgent="-u 1"
	stext='Muted'
	sicon='󰖁'
fi

# Microphone Info
amixer get Capture | grep '\[on\]' &>/dev/null
if [[ "$?" == 0 ]]; then
    [ -n "$active" ] && active+=",5" || active="-a 5"
	mtext='Unmuted'
	micon='󰍬'
else
    [ -n "$urgent" ] && urgent+=",5" || urgent="-u 5"
	mtext='Muted'
	micon='󰍭'
fi

# Theme Elements
prompt="󰋋 $stext, 󰍬 $mtext"
mesg="$mixer - Speaker: $speaker, Mic: $mic"

if [[ "$theme" == *'type-1'* ]]; then
	list_col='1'
	list_row='5'
	win_width='400px'
elif [[ "$theme" == *'type-3'* ]]; then
	list_col='1'
	list_row='5'
	win_width='88px'
elif [[ "$theme" == *'type-5'* ]]; then
	list_col='1'
	list_row='5'
	win_width='520px'
elif [[ ( "$theme" == *'type-2'* ) || ( "$theme" == *'type-4'* ) ]]; then
	list_col='8'
	list_row='1'
	win_width='500px'
fi

# Options
layout=`cat ${theme} | grep 'USE_ICON' | cut -d'=' -f2`
if [[ "$layout" == 'NO' ]]; then
	option_1=" Increase"
	option_2="$sicon $stext"
	option_3=" Decrese"
	option_4="$micon $mtext"
	option_5=" Settings"
else
	option_1="󰝝"
	option_2="$sicon"
	option_3="󰝞"
  option_7="󰒓"
  option_4="󰢳"
	option_5="$micon"
  option_6="󰢴"
fi

# Rofi CMD
rofi_cmd() {
	rofi -theme-str "window {width: $win_width;}" \
		-theme-str "listview {columns: $list_col; lines: $list_row;}" \
		-theme-str 'textbox-prompt-colon {str: " ";}' \
		-dmenu \
		-p "$prompt" \
		-mesg "$mesg" \
		${active} ${urgent} \
		-markup-rows \
		-theme ${theme} \
    -selected-row $row_value
}

# Pass variables to rofi dmenu
run_rofi() {
	echo -e "$option_1\n$option_2\n$option_3\n$option_7\n$option_4\n$option_5\n$option_6" | rofi_cmd
}

# Execute Command
run_cmd() {
	if [[ "$1" == '--opt1' ]]; then
		amixer -Mq set Master,0 5%+ unmute
    ~/.config/rofi/applets/bin/volume.sh --row 0
	elif [[ "$1" == '--opt2' ]]; then
		amixer set Master toggle
    ~/.config/rofi/applets/bin/volume.sh --row 1
	elif [[ "$1" == '--opt3' ]]; then
		amixer -Mq set Master,0 5%- unmute
    ~/.config/rofi/applets/bin/volume.sh --row 2
	elif [[ "$1" == '--opt4' ]]; then
		amixer set Capture 5%-
    ~/.config/rofi/applets/bin/volume.sh --row 4
	elif [[ "$1" == '--opt5' ]]; then
		amixer set Capture toggle
    ~/.config/rofi/applets/bin/volume.sh --row 5
	elif [[ "$1" == '--opt6' ]]; then
		amixer set Capture 5%+
    ~/.config/rofi/applets/bin/volume.sh --row 6
	elif [[ "$1" == '--opt7' ]]; then
		pavucontrol
	fi
}

# Actions
chosen="$(run_rofi)"
case ${chosen} in
    $option_1)
		run_cmd --opt1
        ;;
    $option_2)
		run_cmd --opt2
        ;;
    $option_3)
		run_cmd --opt3
        ;;
    $option_4)
		run_cmd --opt4
        ;;
    $option_5)
		run_cmd --opt5
        ;;
    $option_6)
    run_cmd --opt6
    ;;
    $option_7)
    run_cmd --opt7
    ;;
esac

