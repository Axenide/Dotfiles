import os
import shutil

home_dir = os.path.expanduser("~")

def copy_files(file_list):
    for file in file_list:
        src, dst = file
        try:
            # Check if destination is a symlink
            if os.path.islink(dst):
                # Get the real path of the symlink
                real_path = os.path.realpath(dst)
                # Create directory if it doesn't exist
                os.makedirs(os.path.dirname(real_path), exist_ok=True)
                # Copy file to the real path
                shutil.copyfile(src, real_path)
                print(f"File successfully copied from {src} to {real_path} (symlink).")
            else:
                # Create directory if it doesn't exist
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                # Copy file to the destination
                shutil.copyfile(src, dst)
                print(f"File successfully copied from {src} to {dst}.")
        except FileNotFoundError:
            print(f"File not found: {src}")
        except PermissionError:
            print(f"Permission denied to copy from {src} to {dst}")
        except Exception as e:
            print(f"An error occurred while copying from {src} to {dst}: {e}")

# List of files to copy
file_list = [
    (f"{home_dir}/.cache/wal/colors-nvchad.lua", f"{home_dir}/.config/nvim/lua/themes/wal.lua"),
    (f"{home_dir}/.cache/wal/colors-discord.css", f"{home_dir}/.config/vesktop/themes/axwal.theme.css"),
]

# Call the function
copy_files(file_list)
