import os
import inquirer
import subprocess
import sys

title_text:str = """
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
"""

done_text:str = """
┌────────────────────────────┐
│                            │
│     ░█▀▄░█▀█░█▀█░█▀▀░█     │
│     ░█░█░█░█░█░█░█▀▀░▀     │
│     ░▀▀░░▀▀▀░▀░▀░▀▀▀░▀     │
│                            │
└────────────────────────────┘
> https://github.com/Axenide <
"""

def clear():
    os.system('clear')

def title():
    clear()
    print(f"\033[91m{title_text}\033[0m") 

def main():
    test_mode = '--test' in sys.argv
    term_mode = '--term' in sys.argv
    title()

    questions = [
        inquirer.List(
            'graphics',
            message="Graphics?",
            choices=['NVIDIA', 'Open Source (AMD/Intel/Nouveau)'],
        ),
        inquirer.List(
            'keyboard',
            message="Keyboard layout?",
            choices=['US', 'LATAM'],
        )
    ]

    answers = inquirer.prompt(questions)

    graphics_option = answers['graphics']
    keyboard_option = answers['keyboard']

    title()
    print("Stowing dotfiles...\n")

    if graphics_option == 'NVIDIA':
        if test_mode:
            print("Would copy ./options/nvidia.conf to ./dots/.config/hypr/source/nvidia.conf")
        else:
            with open('./options/nvidia.conf', 'r') as src, open('./dots/.config/hypr/source/nvidia.conf', 'w') as dst:
                dst.write(src.read())

    if keyboard_option == 'US':
        if test_mode:
            print("Would copy ./options/us.conf to ./dots/.config/hypr/source/keyboard.conf")
        else:
            with open('./options/us.conf', 'r') as src, open('./dots/.config/hypr/source/keyboard.conf', 'w') as dst:
                dst.write(src.read())
    else:
        if test_mode:
            print("Would copy ./options/latam.conf to ./dots/.config/hypr/source/keyboard.conf")
        else:
            with open('./options/latam.conf', 'r') as src, open('./dots/.config/hypr/source/keyboard.conf', 'w') as dst:
                dst.write(src.read())

    stow_target = 'term' if term_mode else 'dots'
    if test_mode:
        print(f"Would run 'stow {stow_target}'")
    else:
        os.system(f'stow {stow_target}')

    title()
    answer = inquirer.prompt([inquirer.Confirm('install_packages', message="Install needed packages?", default=True)])

    if answer['install_packages']:
        pacman_script = 'term.sh' if term_mode else 'pacman.sh'
        if test_mode:
            print(f"Would run 'bash {pacman_script}'")
        else:
            subprocess.run(['bash', pacman_script])
    else:
        print("Skipping package installation.")

    title()
    answer = inquirer.prompt([inquirer.Confirm('install_tpm', message="Install TPM plugins?", default=True)])

    if answer['install_tpm']:
        if test_mode:
            print("Would remove ~/.tmux, create ~/.tmux/plugins, and clone TPM")
            print("Would run ~/.tmux/plugins/tpm/scripts/install_plugins.sh")
        else:
            os.system('rm -rf ~/.tmux')
            os.makedirs('~/.tmux/plugins', exist_ok=True)
            subprocess.run(['git', 'clone', 'https://github.com/tmux-plugins/tpm', '~/.tmux/plugins/tpm'])
            subprocess.run(['~/.tmux/plugins/tpm/scripts/install_plugins.sh'])
    else:
        print("Skipping TPM plugins installation.")

    title()
    answer = inquirer.prompt([inquirer.Confirm('install_firefox', message="Install Firefox custom CSS and user.js?", default=True)])

    if answer['install_firefox']:
        if test_mode:
            print("Would run 'bash firefox.sh'")
        else:
            subprocess.run(['bash', 'firefox.sh'])
    else:
        print("Skipping Firefox config.")

    if test_mode:
        print("Would symlink ./example_wallpaper.png to ~/.current.wall")
    else:
        os.symlink('./example_wallpaper.png', os.path.expanduser('~/.current.wall'))

    if test_mode:
        print("Would run 'wal --theme base16-gruvbox-hard'")
        print("Would run 'python ./dots/.config/wal/set.py'")
    else:
        subprocess.run(['wal', '--theme', 'base16-gruvbox-hard'])
        subprocess.run(['python', './dots/.config/wal/set.py'])

    clear()
    print(f"\033[32m{done_text}\033[0m")

if __name__ == "__main__":
    main()
