#!/bin/bash

# Función para mostrar el menú y obtener la respuesta del usuario
show_menu() {
  echo "Instalación de Dotfiles"
  echo "-----------------------"
  echo "Graphics?"
  echo "1. NVIDIA"
  echo "2. Open Source (AMD/Intel/Nouveau)"
  read -p "Elije una opción: " graphics_option

  echo "Keyboard layout?"
  echo "1. US"
  echo "2. LATAM"
  read -p "Elije una opción: " keyboard_option

  # Validar las opciones ingresadas
  if [[ "$graphics_option" != "1" && "$graphics_option" != "2" ]]; then
    echo "Opción de gráficos inválida. Saliendo."
    exit 1
  fi

  if [[ "$keyboard_option" != "1" && "$keyboard_option" != "2" ]]; then
    echo "Opción de diseño de teclado inválida. Saliendo."
    exit 1
  fi
}

# Ejecutar la función de menú
show_menu

# Ejecutar los comandos de stow según las respuestas del usuario
echo "Ejecutando comandos de stow..."

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

echo "Proceso completado. Saliendo."
exit 0
