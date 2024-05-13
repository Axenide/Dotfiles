from __init__ import *

class Applets(Box):
    def __init__(self):
        super().__init__(
            name="applets",
            spacing=4,
            orientation="v",
        )

        self.wifi = True
        self.bluetooth = True
        self.night = False
        self.dnd = False

        self.wifi_icon = Image(
            name="wifi-icon",
            image_file=get_relative_path("../assets/wifi.svg"),
        )

        self.bluetooth_icon = Image(
            name="bluetooth-icon",
            image_file=get_relative_path("../assets/bluetooth.svg"),
        )

        self.night_icon = Image(
            name="night-icon",
            image_file=get_relative_path("../assets/night-off.svg"),
        )

        self.dnd_icon = Image(
            name="dnd-icon",
            image_file=get_relative_path("../assets/bell.svg"),
        )

        self.wifi_button = Button(
            name="wifi-button",
            h_expand=True,
            child=self.wifi_icon,
        )

        self.bluetooth_button = Button(
            name="bluetooth-button",
            h_expand=True,
            child=self.bluetooth_icon,
        )

        self.night_button = Button(
            name="night-button-off",
            h_expand=True,
            child=self.night_icon,
        )


        self.dnd_button = Button(
            name="dnd-button",
            h_expand=True,
            child=self.dnd_icon,
        )

        self.buttons = [
            self.wifi_button,
            self.bluetooth_button,
            self.night_button,
            self.dnd_button,
        ]

        self.button_box = Box(
            v_expand=True,
            spacing=4,
            children=self.buttons,
        )

        self.add(self.button_box)

        for btn in self.buttons:
            bulk_connect(
                btn,
                {
                    "button-press-event": self.on_button_press,
                    "enter-notify-event": self.on_button_hover,
                    "leave-notify-event": self.on_button_unhover,
                },
            )
    
    def on_button_press(self, button: Button, event):
        if button == self.wifi_button:
            commands = {
                1: 'toggle',
                3: 'reveal'
            }
            command = commands.get(event.button)
            if command == 'toggle':
                self.wifi = not self.wifi
                if self.wifi == False:
                    self.wifi_icon.set_from_file(get_relative_path('../assets/wifi-off.svg'))
                    self.wifi_button.set_name('wifi-button-off')
                else:
                    self.wifi_icon.set_from_file(get_relative_path('../assets/wifi.svg'))
                    self.wifi_button.set_name('wifi-button')
            elif command == 'reveal':
                self.wifi_revealer.set_reveal_child(not self.wifi_revealer.get_reveal_child())
                self.bluetooth_revealer.set_reveal_child(False)
                exec_shell_command('kitty --class kitty-floating -e nmtui')

        elif button == self.bluetooth_button:
            commands = {
                1: 'toggle',
                3: 'reveal'
            }
            command = commands.get(event.button)
            if command == 'toggle':
                self.bluetooth = not self.bluetooth
                if self.bluetooth == False:
                    self.bluetooth_icon.set_from_file(get_relative_path('../assets/bluetooth-off.svg'))
                    self.bluetooth_button.set_name('bluetooth-button-off')
                else:
                    self.bluetooth_icon.set_from_file(get_relative_path('../assets/bluetooth.svg'))
                    self.bluetooth_button.set_name('bluetooth-button')
            elif command == 'reveal':
                self.bluetooth_revealer.set_reveal_child(not self.bluetooth_revealer.get_reveal_child())
                self.wifi_revealer.set_reveal_child(False)
                exec_shell_command('kitty --class kitty-floating -e bluetuith')

        elif button == self.night_button:
            commands = {
                1: 'toggle',
            }
            command = commands.get(event.button)
            if command == 'toggle':
                self.night = not self.night
                if self.night == False:
                    self.night_icon.set_from_file(get_relative_path('../assets/night-off.svg'))
                    self.night_button.set_name('night-button-off')
                    exec_shell_command('hyprshade off')
                else:
                    self.night_icon.set_from_file(get_relative_path('../assets/night.svg'))
                    self.night_button.set_name('night-button')
                    exec_shell_command('hyprshade on redshift')

        elif button == self.dnd_button:
            commands = {
                1: 'toggle',
                3: 'open'
            }
            command = commands.get(event.button)
            if command == 'toggle':
                self.dnd = not self.dnd
                if self.dnd == False:
                    self.dnd_icon.set_from_file(get_relative_path('../assets/bell.svg'))
                    self.dnd_button.set_name('dnd-button')
                    exec_shell_command('swaync-client -df')
                else:
                    self.dnd_icon.set_from_file(get_relative_path('../assets/bell-off.svg'))
                    self.dnd_button.set_name('dnd-button-off')
                    exec_shell_command('swaync-client -dn')
            if command == 'open':
                exec_shell_command('swaync-client -t')

    def on_button_hover(self, button: Button, event):
        return self.change_cursor("pointer")

    def on_button_unhover(self, button: Button, event):
        return self.change_cursor("default")
