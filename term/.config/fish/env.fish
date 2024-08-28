set -xg TERMINAL kitty
set -xg EDITOR nvim

# Debo intentar automatizar esto. Fish tiene sus mañas. >:(
#set -xg XDG_DESKTOP_DIR "$HOME/Escritorio"
#set -xg XDG_DOWNLOAD_DIR "$HOME/Descargas"
#set -xg XDG_TEMPLATES_DIR "$HOME/Plantillas"
#set -xg XDG_PUBLICSHARE_DIR "$HOME/Público"
#set -xg XDG_DOCUMENTS_DIR "$HOME/Documentos"
#set -xg XDG_MUSIC_DIR "$HOME/Música"
#set -xg XDG_PICTURES_DIR "$HOME/Imágenes"
#set -xg XDG_VIDEOS_DIR "$HOME/Vídeos"

# Actualiza los directorios de usuario de XDG
xdg-user-dirs-update

# Obtén las rutas de los directorios
set -xg XDG_DESKTOP_DIR (xdg-user-dir DESKTOP)
set -xg XDG_DOWNLOAD_DIR (xdg-user-dir DOWNLOAD)
set -xg XDG_TEMPLATES_DIR (xdg-user-dir TEMPLATES)
set -xg XDG_PUBLICSHARE_DIR (xdg-user-dir PUBLICSHARE)
set -xg XDG_DOCUMENTS_DIR (xdg-user-dir DOCUMENTS)
set -xg XDG_MUSIC_DIR (xdg-user-dir MUSIC)
set -xg XDG_PICTURES_DIR (xdg-user-dir PICTURES)
set -xg XDG_VIDEOS_DIR (xdg-user-dir VIDEOS)

source ~/.config/fish/api.fish
