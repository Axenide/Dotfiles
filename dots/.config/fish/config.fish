if status is-interactive
    # Commands to run in interactive sessions can go here
end

set -U fish_greeting
thefuck --alias | source
starship init fish | source
source ~/.config/fish/aliases.fish
source ~/.config/fish/ffmpeg.fish
source ~/.config/fish/env.fish
zoxide init fish | source
[ -f ~/.inshellisense/key-bindings.fish ] && source ~/.inshellisense/key-bindings.fish
