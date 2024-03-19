import Gdk from 'gi://Gdk'

import SideBar from './sidebar/SideBar.js'
import Menu from './menu/Menu.js'

import { sidebarShown } from '../../shared/vars.js'

const HyprlandService = await Service.import('hyprland')
const SystemTrayService = await Service.import('systemtray')

function Divider() {
  return Widget.Box({
    className: 'divider'
  })
}

function StartSection() {
  const SideBarButton = Widget.Button({
    className: 'sidebar_button',
    cursor: 'pointer',
    child: Widget.Box({
      css: `background-image: url("/home/${Utils.exec('whoami')}/.face.icon")`
    }),
    onPrimaryClick: () => Utils.exec(`bash -c "${App.configDir}/shared/scripts/sidebar.sh toggle"`)
  })

  const SearchButton = Widget.Button({
    className: 'search_button',
    cursor: 'pointer',
    child: Widget.Label(''),
    onPrimaryClick: () => Utils.exec(`bash -c "${App.configDir}/shared/scripts/sidebar.sh toggle-applauncher"`)
  })

  const WallpaperButton = Widget.Button({
    className: 'wallpaper_button',
    cursor: 'pointer',
    child: Widget.Label('󰸉'),
    onPrimaryClick: () => Utils.exec(`bash -c "${App.configDir}/shared/scripts/sidebar.sh toggle-wallpapers"`)
  })

  const revealSystray = Variable(false)
  const SysTray = Widget.Box({
    className: 'systray',
    hpack: 'center',
    vertical: true,
    children: [
      Widget.Revealer({
        revealChild: revealSystray.bind(),
        transition: 'slide_down',
        transitionDuration: 300,
        child: Widget.Box({
          vertical: true,
          spacing: 8,
          className: 'apps',
          children: SystemTrayService.bind('items').transform(apps => apps.map(app =>
            Widget.Button({
              className: 'app',
              child: Widget.Icon({
                icon: app.icon,
                size: 16
              }),
              onPrimaryClick: (_, event) => app.activate(event),
              onSecondaryClick: (self) => {
                app.menu.class_name = 'systray_menu'
                app.menu.popup_at_widget(self, Gdk.Gravity.EAST, Gdk.Gravity.WEST, null)
              }
            })
          ))
        })
      }),
      Widget.Button({
        className: 'systray_button',
        child: Widget.Label({
          label: revealSystray.bind().transform(v => v ? '󰅃' : '󰅀')
        }),
        onPrimaryClick: () => revealSystray.value = !revealSystray.value,
        setup: (self) => self.hook(revealSystray, () => {
          if (revealSystray.value)
            setTimeout(() => revealSystray.value = true, 5000)
        })
      })
    ]
  })

  return Widget.Box({
    className: 'start',
    vpack: 'start',
    vertical: true,
    spacing: 4,
    children: [
      SideBarButton,
      Divider(),
      SearchButton,
      WallpaperButton,
      SysTray
    ]
  })
}

function CenterSection() {
  const WorkspaceIndicator = Widget.Box({
    className: 'workspace_indicator',
    vertical: true,
    spacing: 10,
    children: Array.from({ length: 5 }).map((_, i) =>
      Widget.Button({
        className: 'workspace',
        hpack: 'center',
        cursor: 'pointer',
        onPrimaryClick: () => HyprlandService.message(`dispatch workspace ${i + 1}`)
      }).hook(HyprlandService.active.workspace, (self) => {
        const isActive = HyprlandService.active.workspace.id === i + 1;
        const isOccupied = (HyprlandService.getWorkspace(i + 1)?.windows || 0) > 0;
        const isEmpty = (HyprlandService.getWorkspace(i)?.windows || 0) === 0;

        self.toggleClassName('active', isActive);
        self.toggleClassName('occupied', isOccupied);
        self.toggleClassName('empty', isEmpty);
      }
      )
    )
  })

  return Widget.Box({
    className: 'center',
    vpack: 'center',
    vertical: true,
    children: [
      WorkspaceIndicator
    ]
  })
}

function EndSection() {
  const AudioControlButton = Widget.Button({
    attribute: { menu: Menu('audio') },
    className: 'audio_control_button',
    child: Widget.Label('󰋎'),
    onClicked: (self) => self.attribute.menu.toggle()
  })

  const SystemControlButton = Widget.Button({
    attribute: { menu: Menu('system') },
    className: 'system_control_button',
    child: Widget.Label(''),
    onClicked: (self) => self.attribute.menu.toggle()
  })

  const ScreenShotButton = Widget.Button({
    className: 'screenshot_button',
    child: Widget.Label('󰄄'),
    onPrimaryClick: () => Utils.subprocess(
      ['bash', '-c', '~/.config/rofi/screenshot/screenshot.sh'],
      (output) => print(output)
    )
  })

  const TimeIndicator = Widget.Button({
    attribute: { menu: Menu('calendar') },
    className: 'time_indicator',
    hpack: 'center',
    child: Widget.Label().poll(1000, (self) =>
      self.label = Utils.exec(`date +'%H\n%M'`)
    ),
    onClicked: (self) => self.attribute.menu.toggle()
  })

  return Widget.Box({
    className: 'end',
    vpack: 'end',
    vertical: true,
    spacing: 4,
    children: [
      Widget.Box({
        className: 'controls',
        hpack: 'center',
        vertical: true,
        children: [
          AudioControlButton,
          SystemControlButton,
          ScreenShotButton
        ]
      }),
      TimeIndicator
    ]
  })
}

function Bar() {
  return Widget.Box({
    children: [
      SideBar(),
      Widget.Box({
        className: 'bar',
        child: Widget.CenterBox({
          className: 'sections',
          vertical: true,
          startWidget: StartSection(),
          centerWidget: CenterSection(),
          endWidget: EndSection()
        })
      })
    ]
  })
}

export default Widget.Window({
  name: 'bar',
  layer: 'top',
  exclusivity: 'exclusive',
  keymode: sidebarShown.bind().transform(shown => shown === 'applauncher' ? 'exclusive' : 'none'),
  anchor: ['left', 'top', 'bottom'],
  child: Bar()
})
