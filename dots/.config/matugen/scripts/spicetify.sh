#!/bin/bash

if pgrep spotify; then
    spicetify watch -s & sleep 1 && pkill spicetify &
else
    spicetify apply
fi
