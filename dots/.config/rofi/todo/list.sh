#!/bin/bash
#
# https://github.com/claudiodangelis/rofi-todo
#
# this script manages a simple to-do list stored locally
# it allows adding and removing to-do entries
#
# dependencies: rofi

TODO_FILE="${TODO_FILE:-$HOME/.rofi_todos}"

if [[ ! -a "${TODO_FILE}" ]]; then
    touch "${TODO_FILE}"
fi

function add_todo() {
    echo -e "`date +"%b %d %H:%M"` | $*" >> "${TODO_FILE}"
}

function remove_todo() {
    if [[ ! -z "$DONE_FILE" ]]; then
    	echo "${*}" >> "${DONE_FILE}"
    fi
    sed -i "/^${*}$/d" "${TODO_FILE}"
}

function get_todos() {
    echo "Refresh List"
    echo "$(cat "${TODO_FILE}")"
}

if [ -z "$@" ]; then
    get_todos
else
    LINE=$(echo "${@}" | sed "s/\([^a-zA-Z0-9]\)/\\\\\\1/g")
    LINE_UNESCAPED=${@}
    if [[ $LINE_UNESCAPED == +* ]]; then
        LINE_UNESCAPED=$(echo $LINE_UNESCAPED | sed s/^+//g |sed s/^\s+//g )
        add_todo ${LINE_UNESCAPED}
    else
        MATCHING=$(grep "^${LINE_UNESCAPED}$" "${TODO_FILE}")
        if [[ -n "${MATCHING}" ]]; then
            remove_todo ${LINE_UNESCAPED}
        fi
    fi
    get_todos
fi
