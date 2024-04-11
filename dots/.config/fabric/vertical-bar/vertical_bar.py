import os
import fabric
import time
import psutil
import setproctitle
import signal
from fabric.widgets.box import Box
from fabric.widgets.image import Image
from fabric.widgets.label import Label
from fabric.widgets.button import Button
from fabric.widgets.wayland import Window
from fabric.widgets.date_time import DateTime
from fabric.widgets.centerbox import CenterBox
# from fabric.widgets.webview import WebView
# from fabric.utils.applications import Application
from fabric.system_tray.widgets import SystemTray
from fabric.utils.fabricator import Fabricate
from fabric.utils.string_formatter import FormattedString
from fabric.hyprland.widgets import WorkspaceButton, Workspaces
from fabric.widgets.circular_progress_bar import CircularProgressBar
from fabric.widgets.overlay import Overlay
from fabric.utils import (
    set_stylesheet_from_file,
    # bulk_replace,
    bulk_connect,
    exec_shell_command,
    get_relative_path,
)
import gi
# import json
from loguru import logger
from fabric.widgets.box import Box
from fabric.widgets.button import Button
# from fabric.widgets.eventbox import EventBox
from fabric.hyprland.service import Connection#, SignalEvent
from fabric.utils.string_formatter import FormattedString
from fabric.utils import bulk_connect

gi.require_version("Gtk", "3.0")
from gi.repository import (
    Gtk,
    Gdk,
    GLib,
)

from services.notifications import NotificationServer
from services.notifications import Notification

connection = Connection()

# Overrides
def scroll_handler(self, widget, event: Gdk.EventScroll):
        match event.direction:
            case Gdk.ScrollDirection.UP:
                connection.send_command(
                    "batch/dispatch workspace -1",
                )
                logger.info("[Workspaces] Moved to the next workspace")
            case Gdk.ScrollDirection.DOWN:
                connection.send_command(
                    "batch/dispatch workspace +1",
                )
                logger.info("[Workspaces] Moved to the previous workspace")
            case _:
                logger.info(
                    f"[Workspaces] Unknown scroll direction ({event.direction})"
                )
        return

Workspaces.scroll_handler = scroll_handler

PROFILE_PICTURE = os.path.expanduser("~/.face.icon")

class Circles(Box):
    def __init__(self):
        super().__init__(
            visible=False,
            all_visible=False,
        )
        self.cpu_circular_progress_bar = CircularProgressBar(
            size=(90, 90),
            line_style="none",
            percentage=0,
            name="cpu_circular-progress-bar",
        )
        self.memory_circular_progress_bar = CircularProgressBar(
            size=(90, 90),
            line_style="none",
            percentage=0,
            name="memory_circular-progress-bar",
        )
        self.battery_circular_progress_bar = CircularProgressBar(
            size=(90, 90),
            line_style="none",
            percentage=100,
            name="battery_circular-progress-bar",
        )
        self.update_status()
        GLib.timeout_add_seconds(1, self.update_status)
        self.add(
            Box(
                spacing=24,
                name="circles-container",
                h_expand=True,
                orientation="v",
                children=[
                    Box(
                        name="circular-progress-bar-container",
                        h_expand=True,
                        spacing=4,
                        children=[
                            Box(
                                children=[
                                    Overlay(
                                        children=self.cpu_circular_progress_bar,
                                        overlays=[
                                            Image(
                                                image_file=get_relative_path("assets/cpu.svg"),
                                            ),
                                        ],
                                    )
                                ],
                            ),
                            Box(
                                children=[
                                    Overlay(
                                        children=self.memory_circular_progress_bar,
                                        overlays=[
                                            Image(
                                                image_file=get_relative_path("assets/ram.svg"),
                                            ),
                                        ],
                                    )
                                ]
                            ),
                            Box(
                                children=[
                                    Overlay(
                                        children=self.battery_circular_progress_bar,
                                        overlays=[
                                            Image(
                                                image_file=get_relative_path("assets/bolt.svg"),
                                            ),
                                        ],
                                    ),
                                ]
                            ),
                        ],
                    ),
                ],
            ),
        )
        self.show_all()

    def update_status(self):
        self.cpu_circular_progress_bar.percentage = psutil.cpu_percent()
        self.memory_circular_progress_bar.percentage = psutil.virtual_memory().percent
        self.battery_circular_progress_bar.percentage = (
            psutil.sensors_battery().percent
            if psutil.sensors_battery() is not None
            else 100
        )
        return True

# class WebApp(Box):
#     def __init__(self):
#         super().__init__(
#             name="webapp",
#             visible=False,
#             all_visible=False,
#             h_expand=True,
#             v_expand=True,
#         )
#         self.webview = WebView(
#             name="calendar-webview",
#             h_expand=True,
#             v_expand=True,
#             # url="file://" + str(get_relative_path("calendar/index.html")),
#             url="https://www.google.com/",
#         )
#         self.add(self.webview)

class User(Box):
    def __init__(self):
        super().__init__(
            name="user",
            visible=False,
            all_visible=False,
            h_expand=True,
        )
        self.user_label = Label(
            name="user-label",
            h_align="left",
            label=str(exec_shell_command('whoami')).rstrip().capitalize(),
        )
        self.host_label = Label(
            name="host-label",
            h_align="left",
            label=str(exec_shell_command('hostname')).rstrip().capitalize(),
        )
        self.user_box = Box(
            name="user-box",
            orientation="v",
            v_align="center",
            children=[
                self.user_label,
                self.host_label,
            ]
        )
        self.user_image = Box(
            name="user-image",
            style="background-image: url(\"" + PROFILE_PICTURE + "\");",
        )
        self.add(
            Box(
                name="user-container",
                h_expand=True,
                orientation="h",
                children=[
                    self.user_image,
                    self.user_box,
                ]
            )
        )

class VerticalBar(Window):
    def __init__(self):
        super().__init__(
            layer="top",
            anchor="left top bottom",
            margin="0px -10px 0px 0px",
            visible=False,
            all_visible=False,
            exclusive=True,
            # keyboard_mode="on-demand",
        )
        self.wifi_off = False
        self.bluetooth_off = False
        self.night_off = True
        self.dnd_off = True
        self.system_tray = SystemTray(name="system-tray", orientation="v", spacing=8, icon_size=18)
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
        self.content_box = Gtk.Revealer(
            # name="content-box",
            transition_duration=500,
            transition_type="slide-right",
        )
        self.center_box = CenterBox(name="main-window", orientation="v")
        self.run_button = Button(
            name="run-button",
            tooltip_text="Show Applications Menu",
            child=Image(
                image_file=get_relative_path("assets/applications.svg"),
            ),
        )
        self.power_image = Image(
            name="power-image",
            image_file=get_relative_path("assets/power.svg"),
        )
        self.power_button = Button(
            name="power-button",
            tooltip_text="Show Power Menu",
            child=Box(
                orientation="v",
                children=[
                    self.power_image,
                ]
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
                image_file=get_relative_path("assets/media.svg")
            )
        )
        self.time_button = Button(
            name="time-button",
            child=DateTime(['%H\n%M']),
        )
        self.wifi_icon = Image(
            name="wifi-icon",
            image_file=get_relative_path("assets/wifi.svg"),
        )

        self.wifi_revealer = Gtk.Revealer(
            name="wifi-revealer",
            transition_duration=500,
            transition_type="slide-down",
        )

        self.wifi_revealer.add(
            Box(
                name="wifi-box",
                orientation="v",
                children=[
                ]
            )
        )

        self.bluetooth_icon = Image(
            name="bluetooth-icon",
            image_file=get_relative_path("assets/bluetooth.svg"),
        )

        self.bluetooth_revealer = Gtk.Revealer(
            name="bluetooth-revealer",
            transition_duration=500,
            transition_type="slide-down",
        )

        self.bluetooth_revealer.add(
            Box(
                name="bluetooth-box",
                orientation="v",
                children=[
                ]
            )
        )

        self.night_icon = Image(
            name="night-icon",
            image_file=get_relative_path("assets/night-off.svg"),
        )

        self.dnd_icon = Image(
            name="dnd-icon",
            image_file=get_relative_path("assets/bell.svg"),
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
        for btn in [self.run_button, self.power_button, self.colorpicker, self.media_button, self.time_button, self.wifi_button, self.bluetooth_button, self.night_button, self.dnd_button]:
            bulk_connect(
                btn,
                {
                    "button-press-event": self.on_button_press,
                    "enter-notify-event": self.on_button_hover,
                    "leave-notify-event": self.on_button_unhover,
                },
            )
        self.center_box.add_start(
            Box(
                orientation="v",
                spacing=4,
                children=[
                    self.run_button,
                    Box(name="module-separator"),
                    self.system_tray,
                    Box(name="module-separator"),
                    self.media_button,
                ],
            )
        )
        self.center_box.add_center(
            Box(
                orientation="v",
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
        self.center_box.add_end(
            Box(
                orientation="v",
                spacing=4,
                children=[
                    self.colorpicker,
                    Box(name="module-separator"),
                    self.time_button,
                    Box(name="module-separator"),
                    self.power_button,
                ],
            )
        )

        self.test_object = Label(label="Placeholder")

        self.applets = Box(
            name="applets",
            orientation="h",
            spacing=4,
            children=[
                self.wifi_button,
                self.bluetooth_button,
                self.night_button,
                self.dnd_button,
            ]
        )

        self.ext = Box(v_expand=True, h_expand=True, name="ext")

        self.user = User()

        self.circles = Circles()

        self.calendar = Gtk.Calendar(name="calendar")

        self.content_box.add(
            Box(
                name="content-box",
                spacing=4,
                orientation="v",
                children=[
                    self.user,
                    self.applets,
                    # self.wifi_revealer,
                    # self.bluetooth_revealer,
                    self.ext,
                    # WebApp(),
                    self.calendar,
                    self.circles,
                ]
            )
        )

        self.full_box = Box(
            name="full-box",
            orientation="h",
            children=[self.content_box, self.center_box],
        )

        # self.add(self.center_box)
        self.add(self.full_box)
        self.show_all()

    def on_button_press(self, button: Button, event):
        home_dir = os.getenv('HOME')

        if button == self.run_button:
            commands = {
                1: f'{home_dir}/.config/rofi/launcher/launcher.sh',
                2: 'swaync-client -t -sw',
                3: 'toggle'
            }
            command = commands.get(event.button)
            if command != 'toggle':
                return exec_shell_command(command)
            else:
                self.content_box.set_reveal_child(not self.content_box.get_reveal_child())
        
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

        elif button == self.time_button:
            commands = {
                1: f'{home_dir}/.config/rofi/calendar/calendar.sh',
            }
            command = commands.get(event.button)
            if command:
                return exec_shell_command(command)
        
        elif button == self.wifi_button:
            commands = {
                1: 'toggle',
                3: 'reveal'
            }
            command = commands.get(event.button)
            if command == 'toggle':
                self.wifi_off = not self.wifi_off
                if self.wifi_off == True:
                    self.wifi_icon.set_from_file(get_relative_path('assets/wifi-off.svg'))
                    self.wifi_button.set_name('wifi-button-off')
                else:
                    self.wifi_icon.set_from_file(get_relative_path('assets/wifi.svg'))
                    self.wifi_button.set_name('wifi-button')
            elif command == 'reveal':
                self.wifi_revealer.set_reveal_child(not self.wifi_revealer.get_reveal_child())
                self.bluetooth_revealer.set_reveal_child(False)

        elif button == self.bluetooth_button:
            commands = {
                1: 'toggle',
                3: 'reveal'
            }
            command = commands.get(event.button)
            if command == 'toggle':
                self.bluetooth_off = not self.bluetooth_off
                if self.bluetooth_off == True:
                    self.bluetooth_icon.set_from_file(get_relative_path('assets/bluetooth-off.svg'))
                    self.bluetooth_button.set_name('bluetooth-button-off')
                else:
                    self.bluetooth_icon.set_from_file(get_relative_path('assets/bluetooth.svg'))
                    self.bluetooth_button.set_name('bluetooth-button')
            elif command == 'reveal':
                self.bluetooth_revealer.set_reveal_child(not self.bluetooth_revealer.get_reveal_child())
                self.wifi_revealer.set_reveal_child(False)

        elif button == self.night_button:
            commands = {
                1: 'toggle',
            }
            command = commands.get(event.button)
            if command == 'toggle':
                self.night_off = not self.night_off
                if self.night_off == True:
                    self.night_icon.set_from_file(get_relative_path('assets/night-off.svg'))
                    self.night_button.set_name('night-button-off')
                    exec_shell_command('hyprshade off')
                else:
                    self.night_icon.set_from_file(get_relative_path('assets/night.svg'))
                    self.night_button.set_name('night-button')
                    exec_shell_command('hyprshade on redshift')

        elif button == self.dnd_button:
            commands = {
                1: 'toggle',
            }
            command = commands.get(event.button)
            if command == 'toggle':
                self.dnd_off = not self.dnd_off
                if self.dnd_off == True:
                    self.dnd_icon.set_from_file(get_relative_path('assets/bell.svg'))
                    self.dnd_button.set_name('dnd-button')
                else:
                    self.dnd_icon.set_from_file(get_relative_path('assets/bell-off.svg'))
                    self.dnd_button.set_name('dnd-button-off')

    def on_button_hover(self, button: Button, event):
        self.media_button.set_tooltip_text(str(exec_shell_command('playerctl metadata artist -f "{{ artist }} - {{ title }}"')).rstrip())
        return self.change_cursor("pointer")

    def on_button_unhover(self, button: Button, event):
        return self.change_cursor("default")
    
    def signals(self, sig, frame):
        if sig == signal.SIGUSR1:
            self.content_box.set_reveal_child(not self.content_box.get_reveal_child())

signal.signal(signal.SIGUSR1, VerticalBar().signals)

if __name__ == "__main__":
    # bar = VerticalBar()  # entery point
    setproctitle.setproctitle("axbar")
    NotificationServer()

    set_stylesheet_from_file(get_relative_path("vertical_bar.css"))
    fabric.start()
