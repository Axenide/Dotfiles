#!/bin/bash

# Establecer los valores predeterminados para los parámetros
mic="false"
desktop="false"
row=0

# Parsear los argumentos de línea de comandos
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
            echo "Argumento desconocido: $1"
            exit 1
            ;;
    esac
    shift
done

~/.config/rofi/screenshot/record.sh --mic "$mic" --desktop "$desktop" --row "$row"
