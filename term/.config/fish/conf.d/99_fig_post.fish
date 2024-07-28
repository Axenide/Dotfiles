contains $HOME/.local/bin $PATH; or set -a PATH $HOME/.local/bin
command -qv fig; and eval (fig init fish post --rcfile 99_fig_post | string split0)