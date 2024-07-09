#!/bin/bash

source ~/.config/kitty/colors.sh

# execute slurp with -f "%x %y %w %h" and set variables
read -r X Y W H < <(slurp -f "%x %y %w %h" -b 00000080 -c 8C3D45)
# execute kitty with override and disown
hyprctl dispatch -- exec "[move $X $Y]kitty -o initial_window_width="$W" -o initial_window_height="$H" --class kitty-floating"

exit
