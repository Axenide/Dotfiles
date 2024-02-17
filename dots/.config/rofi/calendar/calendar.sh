#!/usr/bin/env bash
DIR=$(dirname $PWD)

current_day=$(date +"%e")
current_month=$(date +"%m")
current_year=$(date +"%Y")

month=$(date +"%-m")
year=$(date +"%Y")
previous_month="◀"
next_month="▶"
last_selected_option=""

format_calendar () {
    echo "$1" \
    | sed -E 's/([[:alpha:]])__/\1\n/g' \
    | sed -E 's/___([[:digit:]])/.\n\1/g' \
    | sed -e 's/___/\n./g' \
    | sed -e 's/__/\n/g' \
    | sed -e 's/_/\n/g'
}

print_month() {
    calendar="$(cal -v -- $1 $2 | tail -n +2 | sed -e 's/ /_/g')"
    echo "$(format_calendar "$calendar")"
}

find_day_index() {
    index=0
    while IFS=' ' read -ra arr; do
        for i in "${arr[@]}"; do
            if [[ "$i" == "$2" ]]; then
                echo "$index"
                break
            fi
            ((index++))
        done
    done <<< "$1"
}

calendar_menu() {
    calendar_header=$(cal -v -- $month $year | head -n 1)

    month_page="$(print_month $month $year)"
    calendar_body="\n\n\n$previous_month\n\n\n\n$month_page\n\n\n\n$next_month\n\n\n"

    previous_month_index="3"
    next_month_index="59"
    calendar_body_column="7"
    urgent="-u $previous_month_index,$next_month_index"
    active=""
    selected_row=""

    if [[ "$(echo $current_month | bc) $current_year" == "$(echo $month | bc) $year" ]]; then
        current_day_index=$(($(find_day_index "$month_page" $current_day) + $calendar_body_column))
        active="-a $current_day_index"
        selected_row="-selected-row $current_day_index"
    fi

    if [[ $last_selected_option == $previous_month ]]; then
        selected_row="-selected-row $previous_month_index"
    fi

    if [[ $last_selected_option == $next_month ]]; then
        selected_row="-selected-row $next_month_index"
    fi

    echo -e "$calendar_body" | rofi -dmenu \
    -theme ~/.config/rofi/calendar/style.rasi \
    -p "$calendar_header" $urgent $active $selected_row
}

while [[ true ]]; do
    selected=$(calendar_menu)
    last_selected_option="$selected"
    case $selected in
        $previous_month)
            ((month--))
            if [[ $month -lt 1 ]]; then
                month=12
                ((year--))
            fi
            ;;
        $next_month)
            ((month++))
            if [[ $month -gt 12 ]]; then
                month=1
                ((year++))
            fi
            ;;
        *)
    		break
    	    ;;
    esac
done
