#!/bin/bash

# execute slurp with -f "%x %y %w %h" and set variables
read -r X Y W H < <(slurp -f "%x %y %w %h" -b {background.strip}BF -c {color1.strip})
# execute kitty with override and disown
hyprctl dispatch -- exec "[move $X $Y]kitty -o initial_window_width="$W" -o initial_window_height="$H" --class kitty-floating"

exit
