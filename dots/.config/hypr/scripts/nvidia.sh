#!/bin/bash

# Comprobar si se está utilizando una tarjeta gráfica NVIDIA
if lspci | grep -i NVIDIA &> /dev/null; then
    echo "Detectado hardware NVIDIA."

    # Exportar las variables de entorno
    export XCURSOR_SIZE=24
    export LIBVA_DRIVER_NAME=nvidia
    export GBM_BACKEND=nvidia-drm
    export __GLX_VENDOR_LIBRARY_NAME=nvidia
    export WLR_NO_HARDWARE_CURSORS=1
    export WLR_DRM_NO_ATOMIC=1

    echo "Variables de entorno exportadas:"
    echo "XCURSOR_SIZE=24"
    echo "LIBVA_DRIVER_NAME=nvidia"
    echo "GBM_BACKEND=nvidia-drm"
    echo "__GLX_VENDOR_LIBRARY_NAME=nvidia"
    echo "WLR_NO_HARDWARE_CURSORS=1"
    echo "WLR_DRM_NO_ATOMIC=1"
else
    echo "No se detectó hardware NVIDIA."
fi
