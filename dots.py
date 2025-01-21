#!/usr/bin/env python

import os
import subprocess
import questionary
from rich.console import Console
from rich.text import Text

console = Console()

def clear():
    os.system("clear")

def title():
    clear()
    console.print(Text("""
┌────────────────────────────────────────────┐
│                                            │
│     ░█▀█░█░█░█▀▀░█▀█░▀█▀░█▀▄░█▀▀░▀░█▀▀     │
│     ░█▀█░▄▀▄░█▀▀░█░█░░█░░█░█░█▀▀░░░▀▀█     │
│     ░▀░▀░▀░▀░▀▀▀░▀░▀░▀▀▀░▀▀░░▀▀▀░░░▀▀▀     │
│     ░█▀▄░█▀█░▀█▀░█▀▀░▀█▀░█░░░█▀▀░█▀▀       │
│     ░█░█░█░█░░█░░█▀▀░░█░░█░░░█▀▀░▀▀█       │
│     ░▀▀░░▀▀▀░░▀░░▀░░░▀▀▀░▀▀▀░▀▀▀░▀▀▀       │
│                                            │
└────────────────────────────────────────────┘
""", style="bold red"))

def show_menu():
    title()
    graphics_option = questionary.select(
        "Graphics?",
        choices=["NVIDIA", "Open Source (AMD/Intel/Nouveau)"]
    ).ask()

    keyboard_option = questionary.select(
        "Keyboard layout?",
        choices=["US", "LATAM"]
    ).ask()

    return graphics_option, keyboard_option

def copy_config(src, dest):
    with open(src, "r") as source:
        with open(dest, "w") as destination:
            destination.write(source.read())

def stow_files():
    title()
    console.print("Stowing dotfiles...", style="bold green")
    subprocess.run(["stow", "--adopt", "dots"], check=True)

def install_packages():
    title()
    package_choice = questionary.select(
        "Install needed packages?",
        choices=["Yes", "No"]
    ).ask()

    if package_choice == "Yes":
        subprocess.run(["bash", "pacman.sh"], check=True)
    else:
        console.print("Skipping package installation.", style="bold yellow")

def install_tpm_plugins():
    title()
    tpm_choice = questionary.select(
        "Install TPM plugins?",
        choices=["Yes", "No"]
    ).ask()

    if tpm_choice == "Yes":
        tpm_dir = os.path.expanduser("~/.tmux/plugins")
        subprocess.run(["rm", "-rf", tpm_dir], check=True)
        os.makedirs(tpm_dir, exist_ok=True)
        subprocess.run(["git", "clone", "https://github.com/tmux-plugins/tpm", os.path.join(tpm_dir, "tpm")], check=True)
        script_path = os.path.join(tpm_dir, "tpm/scripts/install_plugins.sh")
        if os.path.isfile(script_path):
            subprocess.run([script_path], check=True)
        else:
            console.print(f"Error: El script no existe en la ruta {script_path}", style="bold red")
    else:
        console.print("Skipping TPM plugins installation.", style="bold yellow")

def main():
    title()
    graphics_option, keyboard_option = show_menu()

    # Copy configuration files
    if graphics_option == "NVIDIA":
        copy_config("./options/nvidia.conf", "./dots/.config/hypr/source/nvidia.conf")
    else:
        copy_config("./options/nvidia-dummy.conf", "./dots/.config/hypr/source/nvidia.conf")

    keyboard_file = "us.conf" if keyboard_option == "US" else "latam.conf"
    copy_config(f"./options/{keyboard_file}", "./dots/.config/hypr/source/keyboard.conf")

    stow_files()
    install_packages()
    install_tpm_plugins()

    # Set wallpaper and theme
    subprocess.run(["matugen", "image", "./example_wallpaper.jpg"], check=True, stdout=subprocess.DEVNULL)

    clear()
    console.print("""
┌────────────────────────────┐
│                            │
│     ░█▀▄░█▀█░█▀█░█▀▀░█     │
│     ░█░█░█░█░█░█░█▀▀░▀     │
│     ░▀▀░░▀▀▀░▀░▀░▀▀▀░▀     │
│                            │
└────────────────────────────┘
> https://github.com/Axenide <
""", style="bold green")

if __name__ == "__main__":
    main()
