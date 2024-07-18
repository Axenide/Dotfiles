import os
import shutil
import toml
import subprocess

home_dir = os.path.expanduser("~")
config_file = f"{home_dir}/.config/wal/targets.toml"

def copy_files_from_config(config_file):
    try:
        with open(config_file, "r") as f:
            config = toml.load(f)

        for section, values in config.items():
            src = os.path.join(home_dir, ".cache/wal", values.get("source", ""))
            dst = os.path.expanduser(values.get("target", ""))

            if src and dst:
                try:
                    if os.path.islink(dst):
                        real_path = os.path.realpath(dst)
                        os.makedirs(os.path.dirname(real_path), exist_ok=True)
                        shutil.copy(src, real_path)  # Cambiado de copyfile a copy
                        print(f"File successfully copied from {src} to {real_path} (symlink).")
                    else:
                        os.makedirs(os.path.dirname(dst), exist_ok=True)
                        shutil.copy(src, dst)  # Cambiado de copyfile a copy
                        print(f"File successfully copied from {src} to {dst}.")

                except FileNotFoundError:
                    print(f"File not found: {src}")
                except PermissionError:
                    print(f"Permission denied to copy from {src} to {dst}")
                except Exception as e:
                    print(f"An error occurred while copying from {src} to {dst}: {e}")

            if "command" in values:
                command = values["command"]
                try:
                    print(f"Executing command: {command}")
                    subprocess.run(command, shell=True, check=True)
                except subprocess.CalledProcessError as e:
                    print(f"Error executing command {command}: {e}")
                except Exception as e:
                    print(f"An error occurred while executing command {command}: {e}")

    except FileNotFoundError:
        print(f"Config file not found: {config_file}")
    except Exception as e:
        print(f"An error occurred while reading config file: {e}")

copy_files_from_config(config_file)
