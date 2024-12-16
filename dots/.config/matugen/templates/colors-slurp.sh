#!/bin/bash

# execute slurp with -f "%x %y %w %h" and set variables
read -r X Y W H < <(slurp -f "%x %y %w %h" -b {{colors.shadow.default.hex_stripped}}bf -c {{colors.primary.default.hex_stripped}})
# execute kitty with override and disown
hyprctl dispatch -- exec "[move $X $Y]kitty -o initial_window_width="$W" -o initial_window_height="$H" --class kitty-floating -1"

exit
