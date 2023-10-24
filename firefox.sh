#!/bin/bash

# Ruta de la carpeta original
original_folder="$(pwd)/dots/.config/firefox"

# Ruta de la carpeta .mozilla/firefox
firefox_folder="$HOME/.mozilla/firefox"

# Encuentra el directorio default-release
default_release_dir=$(find "$firefox_folder" -type d -name "*.default-release")

if [ -n "$default_release_dir" ]; then
    # Crea symlinks de todos los archivos y directorios en la carpeta original
    for item in "$original_folder"/*; do
        item_name=$(basename "$item")
        ln -sf "$item" "$default_release_dir/$item_name"
    done
    echo "Symlinks created in $default_release_dir."
else
    echo "No se encontró el directorio default-release de Firefox."
fi
