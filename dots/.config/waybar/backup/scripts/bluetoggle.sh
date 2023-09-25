#!/bin/bash

# Verificar el estado actual de Bluetooth
status=$(bluetoothctl show | grep "Powered" | awk '{print $2}')

# Función para encender o apagar Bluetooth
toggle_bluetooth() {
  if [[ $status == "yes" ]]; then
    bluetoothctl power off
    echo "Bluetooth apagado."
  else
    bluetoothctl power on
    echo "Bluetooth encendido."
  fi
}

# Llamar a la función para alternar el estado de Bluetooth
toggle_bluetooth

