#!/bin/bash

# Función para mostrar el menú y obtener la respuesta del usuario
show_menu() {
  echo "Axenide's dotfiles installer"
  echo "----------------------------"
  echo "Graphics?"
  echo "1. NVIDIA"
  echo "2. Open Source (AMD/Intel/Nouveau)"
  read -p "> " graphics_option

  echo "Keyboard layout?"
  echo "1. US"
  echo "2. LATAM"
  read -p "> " keyboard_option

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
echo "Stowing dotfiles..."

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

# Instalar plugins TPM de Tmux
read -p "Install TPM plugins? (y/n) " answer
if [[ "$answer" == "y" ]]; then
  rm -rf ~/.tmux &&
  mkdir -p ~/.tmux/plugins &&
  git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm && ~/.tmux/plugins/tpm/scripts/install_plugins.sh
else
  echo "Skipping TPM plugins installation."
fi

# Instalar NvChad
read -p "Install NvChad? (y/n) " answer
if [[ "$answer" == "y" ]]; then
  rm -rf ~/.config/nvim &&
  git clone https://github.com/NvChad/NvChad ~/.config/nvim --depth 1 && nvim
  read -p "Install Axenide's custom NvChad config? (y/n) " custom_config
  if [[ "$custom_config" == "y" ]]; then
    rm -rf ~/.config/nvim/lua/custom && stow nvim && nvim
  fi
else
  echo "Skipping NvChad installation."
fi
clear
echo -e "\033[32;3mDone!\033[0m"
echo ""
echo -e "\033[31;3m\nStay Determined! <3\033[0m"
echo -e "\033[31;3m           -Axenide\033[0m"
echo ""
echo -e "\033[33;3m\n>>> https://github.com/Axenide <<<\033[0m"
echo ""
exit 0
