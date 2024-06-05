import re
import os

def rgba_to_hex(rgba):
    r, g, b, a = rgba
    hex_color = "#{:02x}{:02x}{:02x}".format(r, g, b)
    if a < 1:
        return "alpha({}, {})".format(hex_color, a)
    return hex_color

def replace_rgba(match):
    rgba = match.group(1).split(',')
    rgba = [int(c) if i < 3 else float(c) for i, c in enumerate(rgba)]
    return rgba_to_hex(rgba)

def convert_css_rgba_to_hex(file_path):
    with open(file_path, 'r') as file:
        css_content = file.read()

    rgba_pattern = re.compile(r'rgba\(([^)]+)\)')
    new_css_content = rgba_pattern.sub(replace_rgba, css_content)

    with open(file_path, 'w') as file:
        file.write(new_css_content)

    print(f"Colores RGBA en {file_path} han sido convertidos a HEX.")

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.css'):
                file_path = os.path.join(root, file)
                convert_css_rgba_to_hex(file_path)

# Ruta del directorio a procesar
directory_path = '.'
process_directory(directory_path)
