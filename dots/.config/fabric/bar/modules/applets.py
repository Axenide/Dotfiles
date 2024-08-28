from __init__ import *

class Applets(Box):
    def __init__(self):
        super().__init__(name="applets", spacing=4, orientation="v")

        self.states = {
            "wifi": False,
            "bluetooth": False,
            "night": False,
            "dnd": False
        }

        self.icons = {
            "wifi": Label(name="wifi-icon", label=f"{icons.wifi}", markup=True),
            "bluetooth": Label(name="bluetooth-icon", label=f"{icons.bluetooth}", markup=True),
            "night": Label(name="night-icon", label=f"{icons.night_off}", markup=True),
            "dnd": Label(name="dnd-icon", label=f"{icons.dnd}", markup=True)
        }

        self.buttons = {
            "wifi": Button(name="wifi-button", h_expand=True, child=self.icons["wifi"]),
            "bluetooth": Button(name="bluetooth-button", h_expand=True, child=self.icons["bluetooth"]),
            "night": Button(name="night-button-off", h_expand=True, child=self.icons["night"]),
            "dnd": Button(name="dnd-button", h_expand=True, child=self.icons["dnd"]),
        }

        button_box = Box(v_expand=True, spacing=4, children=list(self.buttons.values()))
        self.add(button_box)

        for btn in self.buttons.values():
            bulk_connect(
                btn,
                {
                    "button-press-event": self.on_button_press,
                    "enter-notify-event": self.on_button_hover,
                    "leave-notify-event": self.on_button_unhover,
                },
            )

        self.check_button_states()

    def check_button_states(self):
        self.update_wifi_state('enabled' in exec_shell_command('nmcli radio wifi'))
        self.update_bluetooth_state('Powered: yes' in exec_shell_command('bluetoothctl show'))
        self.update_night_state('redshift' in exec_shell_command('hyprshade current'))
        self.update_dnd_state('true' in exec_shell_command('swaync-client -D'))

    def update_wifi_state(self, enabled):
        self.icons["wifi"].set_markup(f"{icons.wifi if enabled else icons.wifi_off}")
        self.buttons["wifi"].set_name('wifi-button' if enabled else 'wifi-button-off')
        self.states["wifi"] = enabled

    def update_bluetooth_state(self, enabled):
        self.icons["bluetooth"].set_markup(f"{icons.bluetooth if enabled else icons.bluetooth_off}")
        self.buttons["bluetooth"].set_name('bluetooth-button' if enabled else 'bluetooth-button-off')
        self.states["bluetooth"] = enabled

    def update_night_state(self, enabled):
        self.icons["night"].set_markup(f"{icons.night if enabled else icons.night_off}")
        self.buttons["night"].set_name('night-button' if enabled else 'night-button-off')
        self.states["night"] = enabled

    def update_dnd_state(self, enabled):
        self.icons["dnd"].set_markup(f"{icons.dnd_off if enabled else icons.dnd}")
        self.buttons["dnd"].set_name('dnd-button-off' if enabled else 'dnd-button')
        self.states["dnd"] = enabled

    def on_button_press(self, button: Button, event):
        if button == self.buttons["wifi"]:
            self.toggle_wifi(event)
        elif button == self.buttons["bluetooth"]:
            self.toggle_bluetooth(event)
        elif button == self.buttons["night"]:
            self.toggle_night(event)
        elif button == self.buttons["dnd"]:
            self.toggle_dnd(event)

    def toggle_wifi(self, event):
        command = {1: 'toggle', 3: 'reveal'}.get(event.button)
        if command == 'toggle':
            wifi_state = exec_shell_command('nmcli radio wifi')
            self.states["wifi"] = 'enabled' not in wifi_state
            self.update_wifi_state(self.states["wifi"])
            exec_shell_command(f'nmcli radio wifi {"on" if self.states["wifi"] else "off"}')
        elif command == 'reveal':
            self.toggle_revealer("wifi", "bluetooth")
            exec_shell_command('kitty --class kitty-floating -e nmtui')

    def toggle_bluetooth(self, event):
        command = {1: 'toggle', 3: 'reveal'}.get(event.button)
        if command == 'toggle':
            bluetooth_state = exec_shell_command('bluetoothctl show')
            self.states["bluetooth"] = 'Powered: yes' not in bluetooth_state
            self.update_bluetooth_state(self.states["bluetooth"])
            exec_shell_command(f'bluetoothctl power {"on" if self.states["bluetooth"] else "off"}')
        elif command == 'reveal':
            self.toggle_revealer("bluetooth", "wifi")
            exec_shell_command('kitty --class kitty-floating -e bluetuith')

    def toggle_night(self, event):
        if event.button == 1:
            night_state = exec_shell_command('hyprshade current')
            self.states["night"] = 'redshift' not in night_state
            self.update_night_state(self.states["night"])
            exec_shell_command(f'hyprshade {"on redshift" if self.states["night"] else "off"}')

    def toggle_dnd(self, event):
        command = {1: 'toggle', 3: 'open'}.get(event.button)
        if command == 'toggle':
            dnd_state = exec_shell_command('swaync-client -D')
            self.states["dnd"] = 'true' not in dnd_state
            self.update_dnd_state(self.states["dnd"])
            exec_shell_command(f'swaync-client -{"dn" if self.states["dnd"] else "df"}')
        elif command == 'open':
            exec_shell_command('swaync-client -t')

    def toggle_revealer(self, primary, secondary):
        getattr(self, f"{primary}_revealer").set_reveal_child(not getattr(self, f"{primary}_revealer").get_reveal_child())
        getattr(self, f"{secondary}_revealer").set_reveal_child(False)

    def on_button_hover(self, button: Button, event):
        return self.change_cursor("pointer")

    def on_button_unhover(self, button: Button, event):
        return self.change_cursor("default")
