import os
import fabric
import time
import psutil
import setproctitle
import signal
import psutil
import dbus
from fabric.widgets.box import Box
from fabric.widgets.image import Image
from fabric.widgets.label import Label
from fabric.widgets.button import Button
from fabric.widgets.wayland import Window
from fabric.widgets.date_time import DateTime
from fabric.widgets.centerbox import CenterBox
from fabric.widgets.revealer import Revealer
from fabric.widgets.webview import WebView
# from fabric.utils.applications import Application
from fabric.system_tray.widgets import SystemTray
from fabric.utils.fabricator import Fabricator, invoke_repeater
from fabric.utils.string_formatter import FormattedString
from fabric.hyprland.widgets import WorkspaceButton, Workspaces
from fabric.widgets.circular_progress_bar import CircularProgressBar
from fabric.widgets.overlay import Overlay
from fabric.utils import (
    set_stylesheet_from_file,
    # bulk_replace,
    bulk_connect,
    exec_shell_command,
    exec_shell_command_async,
    get_relative_path,
)
import gi
# import json
from loguru import logger
from fabric.widgets.box import Box
from fabric.widgets.button import Button
from fabric.widgets.eventbox import EventBox
from fabric.hyprland.service import Hyprland #, SignalEvent
from fabric.utils.string_formatter import FormattedString
from fabric.utils import bulk_connect

gi.require_version("Gtk", "3.0")
from gi.repository import (
    Gtk,
    Gdk,
    GLib,
)

connection = Hyprland()

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
            size=(50, 50),
            line_style="none",
            percentage=0,
            name="cpu_circular-progress-bar",
        )
        self.memory_circular_progress_bar = CircularProgressBar(
            size=(50, 50),
            line_style="none",
            percentage=0,
            name="memory_circular-progress-bar",
        )
        self.battery_circular_progress_bar = CircularProgressBar(
            size=(50, 50),
            line_style="none",
            percentage=100,
            name="battery_circular-progress-bar",
        )
        # self.update_status()
        # invoke_repeater(1000, self.update_status)
        GLib.Thread.new(None, self.update_status)
        self.add(
            Box(
                spacing=24,
                name="circles-container",
                v_expand=True,
                orientation="v",
                children=[
                    Box(
                        name="circular-progress-bar-container",
                        v_expand=True,
                        v_align="fill",
                        spacing=4,
                        orientation="v",
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
        while True:
            self.cpu_circular_progress_bar.percentage = psutil.cpu_percent(interval=1)
            self.memory_circular_progress_bar.percentage = psutil.virtual_memory().percent
            self.battery_circular_progress_bar.percentage = (
                psutil.sensors_battery().percent
                if psutil.sensors_battery() is not None
                else 100
            )

class AIchat(WebView):
    def __init__(self):
        super().__init__(
            name="ai-chat",
            visible=False,
            all_visible=False,
            h_expand=True,
            v_expand=True,
            url="http://localhost:8501/",
        )

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

class Player(Box):
    def __init__(self):
        super().__init__(
            name="player",
            visible=False,
            all_visible=False,
            h_expand=True,
            orientation="h",
        )

        self.play_button = Button(
            name="play-button",
            icon_image=Image(
                image_file=get_relative_path("assets/stop.svg"),
            )
        )
        self.skip_back_button = Button(
            name="skip-back-button",
            icon_image=Image(
                image_file=get_relative_path("assets/skip-back.svg"),
            )
        )
        self.skip_forward_button = Button(
            name="skip-forward-button",
            icon_image=Image(
                image_file=get_relative_path("assets/skip-forward.svg"),
            )
        )
        self.prev_button = Button(
            name="prev-button",
            icon_image=Image(
                image_file=get_relative_path("assets/prev.svg"),
            )
        )
        self.next_button = Button(
            name="next-button",
            icon_image=Image(
                image_file=get_relative_path("assets/next.svg"),
            )
        )
        self.shuffle_button = Button(
            name="shuffle-button",
            icon_image=Image(
                image_file=get_relative_path("assets/shuffle-off.svg"),
            )
        )
        self.repeat_button = Button(
            name="repeat-button",
            icon_image=Image(
                image_file=get_relative_path("assets/repeat-off.svg"),
            )
        )

        self.cover_file = "file:///home/adriano/Imágenes/Wallpapers/current.wall"

        self.title = Label(
            name="title",
            # label=str(exec_shell_command('playerctl metadata title')).rstrip(),
            label="Title",
        )
        self.artist = Label(
            name="artist",
            # label=str(exec_shell_command('playerctl metadata artist')).rstrip(),
            label="Artist",
        )
        self.cover = Box(
            name="cover",
            style="background-image: url(\"" + self.cover_file + "\");",
            h_expand=True,
            v_align="end",
            orientation="v",
            children=[
                # self.title,
                # self.artist,
            ]
        )

        self.status = Label(
            name="status",
            label="",
        )
        
        # self.player_fabricator = Fabricator(stream=True, poll_from=r"""playerctl --follow metadata --format '{{status}}\n{{position}}\n{{mpris:length}}\n{{artist}}\n{{album}}\n{{title}}'""")
        self.player_fabricator = Fabricator(stream=True, poll_from=r"""playerctl --follow metadata --format '{{status}}\n{{artist}}\n{{mpris:artUrl}}\n{{title}}'""")

        def decode_player_data(_, data: str):
            data = data.split("\\n")
            playback: str = data[0] # "Playing" | "Paused"
            # position: str = data[1] # can be casted to a int if it's not empty
            # length: str = data[2] # can be casted to a int if it's not empty
            artist: str = data[1]
            album: str = data[2]
            title: str = data[3]
            # print(playback, position, length, artist, album, title)
            print(playback, artist, album, title)
            self.status.label = playback
            self.artist.set_label(artist)
            self.title.set_label(title)
            if album == "":
                self.cover.set_style("background-image: url(\"" + self.cover_file + "\");")
            else:
                self.cover.set_style("background-image: url(\"" + album + "\");")

            if playback == "Playing":
                self.play_button.set_image(
                    Image(
                        image_file=get_relative_path("assets/pause.svg"),
                    )
                )
            elif playback == "Paused":
                self.play_button.set_image(
                    Image(
                        image_file=get_relative_path("assets/play.svg"),
                    )
                )
            else:
                self.play_button.set_image(
                    Image(
                        image_file=get_relative_path("assets/stop.svg"),
                    )
                )
            # self.cover.style = "background-image: url(\"" + self.cover_file + "\");"

        self.player_fabricator.connect("changed", decode_player_data)

        self.player_box = Box(
            name="player-box",
            orientation="v",
            v_align="center",
            h_align="center",
            # spacing=8,
            children=[
                self.prev_button,
                # self.skip_back_button,
                self.play_button,
                # self.skip_forward_button,
                self.next_button,
            ]
        )

        for btn in [self.play_button, self.skip_back_button, self.skip_forward_button, self.prev_button, self.next_button, self.shuffle_button, self.repeat_button]:
            bulk_connect(
                btn,
                {
                    "button-press-event": self.on_button_press,
                    "enter-notify-event": self.on_button_hover,
                    "leave-notify-event": self.on_button_unhover,
                },
            )

        self.full_player = Box(
            name="full-player",
            orientation="h",
            h_expand=True,
            children=[
                self.cover,
                self.player_box,
                # self.title,
                # self.artist,
            ]
        )

        self.add(
            self.full_player,
        )
        
    # def update_status(self):
    #     def get_cover():
    #         if str(exec_shell_command('playerctl metadata mpris:artUrl')).rstrip() != "":
    #             return "file:///home/adriano/Imágenes/Wallpapers/current.wall"
    #         else:
    #             return str(exec_shell_command('playerctl metadata mpris:artUrl')).rstrip()
    #
    #     self.cover_file = get_cover()
    #     self.cover.style = "background-image: url(\"" + self.cover_file + "\");"
    #     self.title.label = str(exec_shell_command('playerctl metadata title')).rstrip()
    #     self.artist.label = str(exec_shell_command('playerctl metadata artist')).rstrip()
    #     print(self.cover_file)
    #     return True
    
    def on_button_hover(self, button: Button, event):
        if button == self.play_button:
            if self.status.label == "Playing":
                self.play_button.set_image(
                    Image(
                        image_file=get_relative_path("assets/pause-hover.svg"),
                    )
                )
            elif self.status.label == "Paused":
                self.play_button.set_image(
                    Image(
                        image_file=get_relative_path("assets/play-hover.svg"),
                    )
                )
            else:
                self.play_button.set_image(
                    Image(
                        image_file=get_relative_path("assets/stop-hover.svg"),
                    )
                )
        # elif button == self.skip_back_button:
        #     exec_shell_command("playerctl position 10-")
        # elif button == self.skip_forward_button:
        #     exec_shell_command("playerctl position 10+")
        elif button == self.prev_button:
            self.prev_button.set_image(
                Image(
                    image_file=get_relative_path("assets/prev-hover.svg"),
                )
            )
        elif button == self.next_button:
            self.next_button.set_image(
                Image(
                    image_file=get_relative_path("assets/next-hover.svg"),
                )
            )
        # elif button == self.shuffle_button:
        #     exec_shell_command("playerctl shuffle")
        # elif button == self.repeat_button:
        #     exec_shell_command("playerctl repeat")
        return self.change_cursor("pointer")

    def on_button_unhover(self, button: Button, event):
        if button == self.play_button:
            if self.status.label == "Playing":
                self.play_button.set_image(
                    Image(
                        image_file=get_relative_path("assets/pause.svg"),
                    )
                )
            elif self.status.label == "Paused":
                self.play_button.set_image(
                    Image(
                        image_file=get_relative_path("assets/play.svg"),
                    )
                )
            else:
                self.play_button.set_image(
                    Image(
                        image_file=get_relative_path("assets/stop.svg"),
                    )
                )
        elif button == self.prev_button:
            self.prev_button.set_image(
                Image(
                    image_file=get_relative_path("assets/prev.svg"),
                )
            )
        elif button == self.next_button:
            self.next_button.set_image(
                Image(
                    image_file=get_relative_path("assets/next.svg"),
                )
            )
        return self.change_cursor("default")

    def on_button_press(self, button: Button, event):
        if button == self.play_button:
            exec_shell_command('playerctl play-pause')
        elif button == self.skip_back_button:
            exec_shell_command("playerctl position 10-")
        elif button == self.skip_forward_button:
            exec_shell_command("playerctl position 10+")
        elif button == self.prev_button:
            exec_shell_command("playerctl previous")
        elif button == self.next_button:
            exec_shell_command("playerctl next")
        elif button == self.shuffle_button:
            exec_shell_command("playerctl shuffle")
        elif button == self.repeat_button:
            exec_shell_command("playerctl repeat")
        return True

class Power(EventBox):
    def __init__(self):
        super().__init__(
            name="power-event",
            # orientation="v",
        )
        self.lock = Button(
            name="lock",
            icon_image=Image(image_file=get_relative_path("assets/lock.svg"))
        )

        self.suspend = Button(
            name="suspend",
            icon_image=Image(image_file=get_relative_path("assets/suspend.svg"))
        )

        self.logout = Button(
            name="logout",
            icon_image=Image(image_file=get_relative_path("assets/logout.svg"))
        )

        self.reboot = Button(
            name="reboot",
            icon_image=Image(image_file=get_relative_path("assets/reboot.svg"))
        )

        self.shutdown = Button(
            name="shutdown",
            icon_image=Image(image_file=get_relative_path("assets/shutdown.svg"))
        )

        self.power_box = Box(
            name="power-box",
            orientation="v",
            # spacing=16,
            children=[
                self.lock,
                self.suspend,
                self.logout,
                self.reboot,
                # self.shutdown,
            ]
        )

        self.revealer = Revealer(
            name="power-revealer",
            transition_type="slide-up",
            transition_duration=500,
            child=self.power_box
        )

        self.full_power = Box(
            name="full-power",
            orientation="v",
            children=[
                self.revealer,
                self.shutdown,
            ]
        )

        self.add(self.full_power)

        for btn in [self.lock, self.suspend, self.logout, self.reboot, self.shutdown, self]:
            bulk_connect(
                btn,
                {
                    "button-press-event": self.on_button_press,
                    "enter-notify-event": self.on_button_hover,
                    "leave-notify-event": self.on_button_unhover,
                },
            )

    def on_button_hover(self, button: Button, event):
        if button == self:
            self.revealer.set_reveal_child(True)
            self.set_name("power-event-hover")
            print("hovering")
            print(self.name)
        return self.change_cursor("pointer")

    def on_button_unhover(self, button: Button, event):
        if button == self:
            self.revealer.set_reveal_child(False)
            self.set_name("power-event")
            print("unhovering")
            print(self.name)
        return self.change_cursor("default")

    def on_button_press(self, button: Button, event):
        if button == self.lock:
            exec_shell_command("swaylock")
            # exec_shell_command("notify-send 'Locking screen'")
        elif button == self.suspend:
            # exec_shell_command("systemctl suspend")
            exec_shell_command("notify-send 'Suspending system'")
        elif button == self.logout:
            # exec_shell_command("hyprctl dispatch exit")
            exec_shell_command("notify-send 'Logging out'")
        elif button == self.reboot:
            # exec_shell_command("systemctl reboot")
            exec_shell_command("notify-send 'Rebooting system'")
        elif button == self.shutdown:
            # exec_shell_command("systemctl poweroff")
            exec_shell_command("notify-send 'Shutting down system'")
        return True

class VerticalBar(Window):
    def __init__(self):
        super().__init__(
            layer="top",
            anchor="left top bottom",
            margin="0px -10px 0px 0px",
            visible=False,
            all_visible=False,
            exclusive=True,
            keyboard_mode="none",
        )
        self.wifi_off = False
        self.bluetooth_off = False
        self.ai_off = True
        self.night_off = True
        self.dnd_off = True
        self.system_tray = SystemTray(name="system-tray", orientation="v", spacing=8, icon_size=18)
        self.time_sep = Label(
            label="",
            name="time-separator",
        )

        self.content_box = Revealer(
            # name="content-box",
            transition_duration=500,
            transition_type="slide-right",
        )

        self.dashboard_box = Revealer(
            # name="content-box",
            transition_duration=500,
            transition_type="slide-left",
            # reveal_child=True,
            # h_expand=True,
            # v_expand=True,
        )

        self.chat_box = Revealer(
            # name="content-box",
            transition_duration=500,
            transition_type="slide-right",
            # reveal_child=True,
            h_expand=True,
            v_expand=True,
        )

        self.chat_expand = False

        self.chat_expand_button = Button(
            name="chat-expand",
            h_expand=False,
            child=Image(
                name="chat-expand-image",
                image_file=get_relative_path("assets/maximize.svg")
            )
        )

        self.chat_reload = Button(
            name="chat-reload",
            h_expand=False,
            child=Image(
                name="chat-reload-image",
                image_file=get_relative_path("assets/refresh.svg")
            )
        )

        self.chat_detach = Button(
            name="chat-detach",
            h_expand=False,
            child=Image(
                name="chat-detach-image",
                image_file=get_relative_path("assets/external.svg")
            )
        )

        self.center_box = CenterBox(name="main-window", orientation="v")

        self.run_button = Button(
            name="run-button",
            tooltip_text="Show Applications Menu",
            child=Image(
                name="run-button-image",
                image_file=get_relative_path("assets/applications.svg"),
            ),
        )

        self.power = Power()

        self.colorpicker = Button(
            name="colorpicker",
            tooltip_text="Color Picker",
            child=Image(
                name="colorpicker-image",
                image_file=get_relative_path("assets/colorpicker.svg")
            ),
        )
        self.media_button = Button(
            name="media-button",
            tooltip_text=str(exec_shell_command('playerctl metadata artist -f "{{ artist }} - {{ title }}"')).rstrip(),
            child=Image(
                name="media-button-image",
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

        self.wifi_revealer = Revealer(
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

        self.bluetooth_revealer = Revealer(
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

        self.buttons = [
            self.run_button,
            self.colorpicker,
            self.media_button,
            self.time_button,
            self.wifi_button,
            self.bluetooth_button,
            self.night_button,
            self.dnd_button,
            self.chat_expand_button,
            self.chat_reload,
            self.chat_detach
        ]

        for btn in self.buttons:
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

        self.center_box.add_end(
            Box(
                orientation="v",
                spacing=4,
                children=[
                    self.colorpicker,
                    Box(name="module-separator"),
                    self.time_button,
                    Box(name="module-separator"),
                    # self.power_button,
                    self.power,
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

        self.ext = Box(
            name="ext",
            v_expand=True,
            h_expand=True,
            orientation="v",
            spacing=8,
            children=[
                Box(
                    name="ext-box",
                    orientation="v",
                    v_expand=True, 
                    v_align="center",
                    spacing=8,
                    children=[
                        Label(name="ext-label", label="Work In Progress"),
                        Image(image_file=get_relative_path("assets/tool.svg")),
                    ]
                )
            ]
        )

        self.user = User()

        self.circles = Circles()

        self.player = Player()

        self.calendar = Gtk.Calendar(name="calendar", hexpand=True)

        self.dashboard_box.add(
            Box(
                name="dashboard-box",
                spacing=4,
                orientation="v",
                h_expand=True,
                v_expand=True,
                children=[
                    # self.user,
                    self.applets,
                    self.player,
                    # self.wifi_revealer,
                    # self.bluetooth_revealer,
                    self.ext,
                    # AIchat(),
                    # self.calendar,
                    # self.circles,
                    # self.bottom_box,
                    Box(name="bottom-box", orientation="h", h_expand=True, spacing=4, children=[self.calendar, self.circles]),
                ]
            )
        )

        self.chat = AIchat()

        self.chat_buttons = Box(
            name="chat-buttons",
            orientation="h",
            h_expand=True,
            spacing=4,
            children=[
                self.chat_expand_button,
                self.chat_reload,
                self.chat_detach,
            ]
        )

        self.chat_box_content = Box(
            name="chat-box",
            spacing=4,
            orientation="v",
            children=[
                self.chat_buttons,
                self.chat,
            ]
        )
        
        self.chat_box.add(
            self.chat_box_content,
        )

        self.revealers_box = Box(
            name="revealers-box",
            orientation="h",
            h_expand=True,
            v_expand=True,
            children=[
                self.chat_box,
                self.dashboard_box,
            ]
        )
        
        self.content_box.add(
            Box(
                name="content-box",
                spacing=4,
                orientation="v",
                h_expand=True,
                v_expand=True,
                children=[
                    self.user,
                    # self.applets,
                    # self.player,
                    # self.wifi_revealer,
                    # self.bluetooth_revealer,
                    # self.ext,
                    # AIchat(),
                    # self.calendar,
                    # self.circles,
                    # self.bottom_box,
                    # Box(name="bottom-box", orientation="h", h_expand=True, spacing=4, children=[self.calendar, self.circles]),
                    self.revealers_box,
                ]
            )
        )

        self.full_box = Box(
            name="full-box",
            orientation="h",
            children=[
                self.content_box,
                self.chat_box,
                self.center_box,
            ],
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
                self.dashboard_box.set_reveal_child(not self.dashboard_box.get_reveal_child())

                if self.content_box.get_reveal_child() == False:
                    self.dashboard_box.set_reveal_child(False)
                    self.chat_box.set_reveal_child(False)
                    self.set_keyboard_mode("none")
        
        elif button == self.colorpicker:
            commands = {
                1: get_relative_path('scripts/hyprpicker-hex.sh'),
                3: get_relative_path('scripts/hyprpicker-rgb.sh'),
            }
            command = commands.get(event.button)
            if command:
                return exec_shell_command_async(command, lambda *args: None)
        
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
                exec_shell_command('kitty --class kitty-floating -e nmtui')

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
                exec_shell_command('kitty --class kitty-floating -e bluetuith')

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
                3: 'open'
            }
            command = commands.get(event.button)
            if command == 'toggle':
                self.dnd_off = not self.dnd_off
                if self.dnd_off == True:
                    self.dnd_icon.set_from_file(get_relative_path('assets/bell.svg'))
                    self.dnd_button.set_name('dnd-button')
                    exec_shell_command('swaync-client -df')
                else:
                    self.dnd_icon.set_from_file(get_relative_path('assets/bell-off.svg'))
                    self.dnd_button.set_name('dnd-button-off')
                    exec_shell_command('swaync-client -dn')
            if command == 'open':
                exec_shell_command('swaync-client -t')

        elif button == self.chat_expand_button:
            self.chat_expand = not self.chat_expand
            if self.chat_expand:
                self.chat_box_content.set_style('min-width: 550px;')
                self.chat_expand_button.get_children()[0].set_from_file(get_relative_path('assets/minimize.svg'))
            else:
                self.chat_box_content.set_style('min-width: 300px;')
                self.chat_expand_button.get_children()[0].set_from_file(get_relative_path('assets/maximize.svg'))

        elif button == self.chat_reload:
            self.chat.reload()

        elif button == self.chat_detach:
            self.content_box.set_reveal_child(False)
            self.chat_box.set_reveal_child(False)
            return exec_shell_command_async(get_relative_path(f'scripts/webview.py http://localhost:8501/'), lambda *args: None)

    def on_button_hover(self, button: Button, event):
        self.media_button.set_tooltip_text(str(exec_shell_command('playerctl metadata artist -f "{{ artist }} - {{ title }}"')).rstrip())
        return self.change_cursor("pointer")

    def on_button_unhover(self, button: Button, event):
        return self.change_cursor("default")
    
    def signals(self, sig, frame):
        if sig == signal.SIGUSR1:
            self.dashboard_box.set_reveal_child(not self.dashboard_box.get_reveal_child())
            self.chat_box.set_reveal_child(False)

        if sig == signal.SIGUSR2:
            self.chat_box.set_reveal_child(not self.chat_box.get_reveal_child())
            self.dashboard_box.set_reveal_child(False)

        if self.chat_box.get_reveal_child() == True:
            self.set_keyboard_mode("on-demand")
        else:
            self.set_keyboard_mode("none")

        if self.dashboard_box.get_reveal_child() == False and self.chat_box.get_reveal_child() == False:
            self.content_box.set_reveal_child(False)
        else:
            self.content_box.set_reveal_child(True)

if __name__ == "__main__":
    bar = VerticalBar()  # entery point
    signal.signal(signal.SIGUSR1, bar.signals)
    signal.signal(signal.SIGUSR2, bar.signals)
    setproctitle.setproctitle("axbar")
    set_stylesheet_from_file(get_relative_path("bar.css"))
    fabric.start()
