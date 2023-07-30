#!/bin/bash
cd ~/Imágenes/Wallpapers
wallpaper=$(ls -p | grep -v / | tofi "$@" --prompt-text "Wallpaper: " | cut -d '' -f 1 | tr -d '\n')

swww img -t any --transition-bezier 0.0,0.0,1.0,1.0 --transition-duration .75 --transition-step 255 --transition-fps 60 "$wallpaper" && \
ln -sf ~/Imágenes/Wallpapers/"$wallpaper" ~/Imágenes/Wallpapers/current.wall
exit
