#!/bin/bash

yay -Syu --noconfirm --needed git stow python python-questionary python-rich
python ./dots.py
