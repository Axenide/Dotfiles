set -xg TERMINAL kitty
set -xg EDITOR nvim
xdg-user-dirs-update

set -xg XDG_DESKTOP_DIR (xdg-user-dir DESKTOP)
set -xg XDG_DOWNLOAD_DIR (xdg-user-dir DOWNLOAD)
set -xg XDG_TEMPLATES_DIR (xdg-user-dir TEMPLATES)
set -xg XDG_PUBLICSHARE_DIR (xdg-user-dir PUBLICSHARE)
set -xg XDG_DOCUMENTS_DIR (xdg-user-dir DOCUMENTS)
set -xg XDG_MUSIC_DIR (xdg-user-dir MUSIC)
set -xg XDG_PICTURES_DIR (xdg-user-dir PICTURES)
set -xg XDG_VIDEOS_DIR (xdg-user-dir VIDEOS)

if test -e ~/.config/fish/api.fish
  source ~/.config/fish/api.fish
end
