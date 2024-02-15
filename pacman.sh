#!/bin/bash

clear

title() {
  clear
  echo -e "\e[91m   ___                _    __   _    "
  echo -e "  / _ |__ _____ ___  (_)__/ /__( )___"
  echo -e " / __ |\ \ / -_) _ \/ / _  / -_)/(_-<"
  echo -e "/_/_|_/_\_\\__/_//_/_/\_,_/\__/ /___/"
  echo -e "  / _ \___  / /_/ _(_) /__ ___       "
  echo -e " / // / _ \/ __/ _/ / / -_|_-<       "
  echo -e "/____/\___/\__/_//_/_/\__/___/  \e[0m" 
  echo "≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣"
}

title

echo "For this installation you need git and an AUR helper (yay). Do you want to install them? (y/n)"
read install_git_yay

if [ $install_git_yay = "y" ]; then
  sudo pacman -S --needed git
  git clone https://aur.archlinux.org/yay-bin.git
  cd yay-bin
  makepkg -si
  cd ..
  rm -rf yay-bin
  title
else
  clear
  echo "Please install git and yay before running this script."
  exit 1
fi

title

echo "Do you want to install Chaotic AUR and custom pacman.conf? (y/n)"
read pacman_conf

if [ $pacman_conf = "y" ]; then
  sudo pacman-key --recv-key 3056513887B78AEB --keyserver keyserver.ubuntu.com
  sudo pacman-key --lsign-key 3056513887B78AEB
  sudo pacman -U 'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-keyring.pkg.tar.zst'
  sudo pacman -U 'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-mirrorlist.pkg.tar.zst'
  sudo cp ./pacman/pacman.conf /etc/pacman.conf
  title
  echo "Chaotic AUR and custom pacman.conf installed."
else
  title
  echo "Chaotic AUR and custom pacman.conf not installed."
fi

title

echo "Do you want to install the packages for this dotfiles? (y/n)"
read install_packages

if [ $install_packages = "y" ]; then
  yay -S --needed - < ./pacman/packages.txt
  title
  echo "Packages installed."
else
  title
  echo "Packages not installed."
fi

sudo usermod -aG input $USER
sudo usermod -aG seat $USER
