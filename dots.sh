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

# Función para mostrar el menú y obtener la respuesta del usuario
show_menu() {
  title
  echo -e "\e[1;3;32mGraphics?\e[0m"
  echo "1. NVIDIA"
  echo "2. Open Source (AMD/Intel/Nouveau)"
  read -p "> " graphics_option
  echo ""
  title
  echo -e "\e[1;3;32mKeyboard layout?\e[0m"
  echo "1. US"
  echo "2. LATAM"
  read -p "> " keyboard_option
  echo ""

  # Validar las opciones ingresadas
  if [[ "$graphics_option" != "1" && "$graphics_option" != "2" ]]; then
    echo "Invalid graphics option. Exiting."
    exit 1
  fi

  if [[ "$keyboard_option" != "1" && "$keyboard_option" != "2" ]]; then
    echo "Invalid keyboard layout option. Exiting."
    exit 1
  fi
}

# Ejecutar la función de menú
show_menu

# Ejecutar los comandos de stow según las respuestas del usuario
title
echo "Stowing dotfiles..."
echo ""

# Si la opción de gráficos es NVIDIA
if [[ "$graphics_option" == "1" ]]; then
  stow nvidia
else
  stow open-graphics
fi

# Si la opción de diseño de teclado es US
if [[ "$keyboard_option" == "1" ]]; then
  stow us
else
  stow latam
fi

# Siempre ejecutar 'stow dots'
stow dots

# Instalar paquetes
title
read -p "Install needed packages? (y/n) " answer
if [[ "$answer" == "y" ]]; then
  bash pacman.sh
else
  echo "Skipping package installation."
fi

title
# Instalar plugins TPM de Tmux
read -p "Install TPM plugins? (y/n) " answer
if [[ "$answer" == "y" ]]; then
  rm -rf ~/.tmux &&
  mkdir -p ~/.tmux/plugins &&
  git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm && ~/.tmux/plugins/tpm/scripts/install_plugins.sh
else
  echo "Skipping TPM plugins installation."
fi
echo ""

# Instalar Firefox userChrome.css
title
read -p "Install Firefox custom CSS and user.js? (y/n) " answer
if [[ "$answer" == "y" ]]; then
  bash firefox.sh
else
  echo "Skipping Firefox config."
fi

# Instalar Floorp userChrome.css
title
read -p "Install Floorp custom CSS and user.js? (y/n) " answer
if [[ "$answer" == "y" ]]; then
  bash floorp.sh
else
  echo "Skipping Floorp config."
fi

clear
echo -e "\e[32m   ___                __"
echo "  / _ \___  ___  ___ / /"
echo " / // / _ \/ _ \/ -_)_/"
echo "/____/\___/_//_/\__(_)"
echo ""
echo -e "\033[31;3m\nStay Determined! <3\033[0m"
echo -e "\033[31;3m           -Axenide\033[0m"
echo ""
echo -e "\033[33;3m\n>>> https://github.com/Axenide <<<\033[0m"
echo ""
exit 0
