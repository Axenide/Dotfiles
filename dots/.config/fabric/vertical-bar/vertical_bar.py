import os
import fabric
import time
import psutil
import setproctitle
from fabric.widgets.box import Box
from fabric.widgets.image import Image
from fabric.widgets.label import Label
from fabric.widgets.button import Button
from fabric.widgets.wayland import Window
from fabric.widgets.date_time import DateTime
from fabric.widgets.centerbox import CenterBox
from fabric.system_tray import SystemTray
from fabric.utils.fabricator import Fabricate
from fabric.utils.string_formatter import FormattedString
from fabric.hyprland.widgets import WorkspaceButton, Workspaces
from fabric.utils import (
    set_stylesheet_from_file,
    bulk_replace,
    bulk_connect,
    exec_shell_command,
    get_relative_path,
)


class PowerMenu(Window):
    def __init__(self):
        super().__init__(
            layer="overlay",
            anchor="left bottom",
            margin="10px 10px 10px 10px",
            exclusive=False,
        )
        self.lock_button = Button(
            label="",
            name="lock-button",
        )
        self.suspend_button = Button(
            label="󰤄",
            name="suspend-button",
        )
        self.logout_button = Button(
            label="",
            name="logout-button",
        )
        self.reboot_button = Button(
            label="",
            name="reboot-button",
        )
        self.shut_down_button = Button(
            label="󰤁",
            name="shut-down-button",
        )
        self.add(
            Box(
                spacing=8,
                orientation="v",
                name="power-window",
                children=[
                    self.lock_button,
                    self.suspend_button,
                    self.logout_button,
                    self.reboot_button,
                    self.shut_down_button,
                ],
            )
        )
        for btn in [self.shut_down_button, self.reboot_button, self.logout_button]:
            bulk_connect(
                btn,
                {
                    "enter-notify-event": lambda *args: self.change_cursor("pointer"),
                    "leave-notify-event": lambda *args: self.change_cursor("default"),
                    "button-press-event": self.on_button_press,
                },
            )
        self.hide()

    def on_button_press(self, button: Button, event):
        if event.button == 1 and event.type == 5:
            # this block will be executed on double click
            if button.get_name() == "shut-down-button":
                exec_shell_command("notify-send Shutting down")
            elif button.get_name() == "reboot-button":
                exec_shell_command("notify-send Rebooting")
            elif button.get_name() == "logout-button":
                exec_shell_command("notify-send Logging out")
            self.toggle_window()

    def toggle_window(self):
        if not self.is_visible():
            self.show_all()
        else:
            self.hide()
        return self


class VerticalBar(Window):
    def __init__(self):
        super().__init__(
            layer="top",
            anchor="left top bottom",
            margin="0px -10px 0px 0px",
            visible=False,
            all_visible=False,
            exclusive=True,
        )
        self.power_menu = PowerMenu()
        self.system_tray = SystemTray(name="system-tray", orientation="v", spacing=8)
        self.time_sep = Label(
            label="",
            name="time-separator",
        )
        self.time_sep_var = Fabricate(
            value="",
            poll_from=lambda _: [
                "",
                self.time_sep.set_style_classes(["day"]),
            ][0]
            if time.strftime("%p").lower() == "am"
            else [
                "",
                self.time_sep.set_style_classes(["night"]),
            ][0],
            interval=1000,
        )
        self.time_sep.bind_property(
            "label",
            self.time_sep_var,
            "value-str",
            # 1,
        )
        self.center_box = CenterBox(name="main-window", orientation="v")
        self.run_button = Button(
            name="run-button",
            tooltip_text="Show Applications Menu",
            child=Image(
                image_file=get_relative_path("assets/applications.svg"),
            ),
        )
        self.power_button = Button(
            name="power-button",
            tooltip_text="Show Power Menu",
            child=Image(
                image_file=get_relative_path("assets/power.svg")
            ),
        )
        self.colorpicker = Button(
            name="colorpicker",
            tooltip_text="Color Picker",
            child=Image(
                image_file=get_relative_path("assets/colorpicker.svg")
            ),
        )
        self.media_button = Button(
            name="media-button",
            tooltip_text=str(exec_shell_command('playerctl metadata artist -f "{{ artist }} - {{ title }}"')).rstrip(),
            child=Image(
                image_file=get_relative_path("assets/stop.svg")
            )
        )
        self.time_button = Button(
            name="time-button",
            child=DateTime(['%H\n%M']),
        )
        for btn in [self.run_button, self.power_button, self.colorpicker, self.media_button, self.time_button]:
            bulk_connect(
                btn,
                {
                    "button-press-event": self.on_button_press,  # run_button -> open wofi, power_button -> toggle the power menu
                    "enter-notify-event": self.on_button_hover,  # to change the cursor to a pointer
                    "leave-notify-event": self.on_button_unhover,  # resets the cursor
                },
            )
        self.center_box.add_left(
            Box(
                orientation="v",
                style="min-width: calc(40px - 4px); margin: 4px;",
                children=[
                    self.run_button,
                    Box(
                        name="module-separator",
                    ),
                    self.system_tray,
                    Box(
                        name="module-separator",
                    ),
                    self.media_button,
                ],
            )
        )
        self.center_box.add_center(
            Box(
                orientation="v",
                style="min-width: calc(40px - 4px); margin: 4px;",
                children=[
                    Workspaces(
                        spacing=8,
                        orientation="v",
                        name="workspaces",
                        buttons_list=[
                            WorkspaceButton(label=FormattedString("")),
                            WorkspaceButton(label=FormattedString("")),
                            WorkspaceButton(label=FormattedString("")),
                            WorkspaceButton(label=FormattedString("")),
                            WorkspaceButton(label=FormattedString("")),
                            WorkspaceButton(label=FormattedString("")),
                            WorkspaceButton(label=FormattedString("")),
                            WorkspaceButton(label=FormattedString("")),
                            WorkspaceButton(label=FormattedString("")),
                            WorkspaceButton(label=FormattedString("")),
                        ],
                    ),
                ],
            )
        )
        self.cpu_label = Label(label="0")
        self.memory_label = Label(label="0")
        self.battery_label = Label(label="0")
        self.system_info_var = Fabricate(
            value={"ram": 0, "cpu": 0},
            poll_from=lambda _: {
                "ram": str(int(psutil.virtual_memory().percent)),
                "cpu": str(int(psutil.cpu_percent())),
                "battery": str(
                    int(
                        psutil.sensors_battery().percent
                        if psutil.sensors_battery() is not None
                        else 100
                    )
                ),
            },
            interval=1000,
        )
        self.system_info_var.connect(
            "changed",
            lambda _, value: (
                self.cpu_label.set_label(value["cpu"]),
                self.memory_label.set_label(value["ram"]),
                self.battery_label.set_label(value["battery"]),
            ),
        )
        self.center_box.add_right(
            Box(
                orientation="v",
                style="min-width: calc(40px - 4px); margin: 4px;",
                children=[
                    self.colorpicker,
                    Box(name="module-separator"),
                    self.time_button,
                    Box(name="module-separator"),
                    self.power_button,
                ],
            )
        )
        self.add(self.center_box)
        self.show_all()

    def on_button_press(self, button: Button, event):
        home_dir = os.getenv('HOME')

        if button == self.run_button:
            commands = {
                1: f'{home_dir}/.config/rofi/launcher/launcher.sh',
                2: 'swaync-client -t -sw',
                3: 'notify-send "Showing overview"'
            }
            command = commands.get(event.button)
            if command:
                return exec_shell_command(command)
        
        elif button == self.power_button:
            commands = {
                1: f'{home_dir}/.config/rofi/powermenu/powermenu.sh',
                3: 'notify-send "Placeholder" "xDDDDD"'
            }
            command = commands.get(event.button)
            if command:
                return exec_shell_command(command)
        
        elif button == self.colorpicker:
            commands = {
                1: 'bash ' + get_relative_path('scripts/hyprpicker-hex.sh'),
                3: 'bash ' + get_relative_path('scripts/hyprpicker-rgb.sh'),
            }
            command = commands.get(event.button)
            if command:
                return exec_shell_command(command)
        
        elif button == self.media_button:
            commands = {
                1: 'playerctl previous',
                2: 'playerctl play-pause',
                3: 'playerctl next',
            }
            command = commands.get(event.button)
            if command:
                return exec_shell_command(command)

    def on_button_hover(self, button: Button, event):
        self.media_button.set_tooltip_text(str(exec_shell_command('playerctl metadata artist -f "{{ artist }} - {{ title }}"')).rstrip())
        return self.change_cursor("pointer")

    def on_button_unhover(self, button: Button, event):
        return self.change_cursor("default")


if __name__ == "__main__":
    bar = VerticalBar()  # entery point
    setproctitle.setproctitle("axbar")

    set_stylesheet_from_file(get_relative_path("vertical_bar.css"))
    fabric.start()
