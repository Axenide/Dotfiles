const WALLPAPERS_PATH = `/home/${Utils.exec("whoami")}/Imágenes/Wallpapers`
const THUMBNAILS_PATH = `/home/${Utils.exec("whoami")}/Imágenes/Wallpapers/.thumbnails`

function Wallpaper(wallpaper) {
  const filename = wallpaper.substring(wallpaper.lastIndexOf('/') + 1);

  return Widget.Button({
    className: 'wallpaper',
    cursor: 'pointer',
    onPrimaryClick: () => {
      Utils.exec(`ln -sf ${WALLPAPERS_PATH}/${filename} ${WALLPAPERS_PATH}/current.wall`)

      Utils.exec(`bash -c "${App.configDir}/shared/scripts/sidebar.sh close"`)
      Utils.exec(`bash -c "${App.configDir}/shared/scripts/sidebar.sh toggle-wallpapers"`)

      Utils.exec(`swww img -t any --transition-bezier 0.0,0.0,1.0,1.0 --transition-duration 1 --transition-step 255 --transition-fps 60 "${WALLPAPERS_PATH}/${filename}"`)
    },
    child: Widget.Box({
      className: 'img',
      css: `background-image: url("${THUMBNAILS_PATH}/${filename}")`
    })
  })
}

const command = `find ${WALLPAPERS_PATH}/ -iname '*.png' -or -iname '*.jpg' -or -iname '*.jpeg' -or -iname '*.webp' -or -iname '*.gif'`

function WallpaperList() {
  return Widget.Scrollable({
    vexpand: true,
    child: Widget.Box({
      className: 'list',
      vertical: true,
      spacing: 12,
      children: Utils.exec(command)
        .split('\n')
        .sort()
        .map(Wallpaper)
    })
  })
}

export default function() {
  return Widget.Box({
    className: 'wallpapers',
    vertical: true,
    children: [
      WallpaperList()
    ]
  })
}
