import os
import json

home = os.path.expanduser("~")

# Ruta al archivo colors.json generado por Pywal
wal_colors_path = f"{home}/.cache/wal/colors.json"

# Ruta donde quieres guardar el archivo template
output_template_path = f"{home}/.config/fabric/bar/styles/themes/wal.css"

# Lee los colores generados por Pywal
with open(wal_colors_path, 'r') as f:
    colors = json.load(f)

# Crea el template
template = f"""
@define-color background #000000;
@define-color white {colors['colors']['color7']};
@define-color red {colors['colors']['color1']};
@define-color yellow {colors['colors']['color3']};
@define-color green {colors['colors']['color2']};
@define-color blue {colors['colors']['color4']};
@define-color magenta {colors['colors']['color5']};
@define-color aqua {colors['colors']['color6']};
@define-color black {colors['colors']['color0']};
@define-color darkgray #111111;
@define-color gray {colors['colors']['color0']};
@define-color lightgray {colors['colors']['color8']};
"""

# Guarda el template en un archivo
with open(output_template_path, 'w') as f:
    f.write(template)

print("Template generado y guardado correctamente.")
