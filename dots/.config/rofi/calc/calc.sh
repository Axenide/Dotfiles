#! /usr/bin/env bash

theme=~/.config/rofi/calc/style.rasi

rofi -show calc -modi calc -no-show-match -no-sort -theme $theme -calc-command "echo -n '{result}' | wl-copy"
