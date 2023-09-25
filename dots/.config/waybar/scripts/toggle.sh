#!/bin/bash

# Verificar si se proporcionó un nombre de proceso como argumento
if [ $# -ne 1 ]; then
    echo "Uso: $0 <nombre_del_proceso>"
    exit 1
fi

proceso="$1"

if pgrep -x "$proceso" > /dev/null; then
    pkill "$proceso"
else
    "$proceso" &
fi
