if status is-interactive
    # Commands to run in interactive sessions can go here
end

set -U fish_greeting
# Bun
fish_add_path -g $HOME/.cache/.bun/bin
# Go
fish_add_path -g $HOME/.local/share/go/bin
thefuck --alias | source
starship init fish | source
source ~/.config/fish/aliases.fish
source ~/.config/fish/ffmpeg.fish
source ~/.config/fish/env.fish
zoxide init fish | source


function conda-on
    eval /home/adriano/.local/share/miniforge3/bin/conda "shell.fish" "hook" | source
end
