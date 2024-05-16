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
from fabric.widgets.scrolled_window import ScrolledWindow
from fabric.widgets.date_time import DateTime
from fabric.widgets.centerbox import CenterBox
from fabric.widgets.revealer import Revealer
from fabric.widgets.stack import Stack
from fabric.widgets.scale import Scale
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
    GdkPixbuf,
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

home_dir = os.getenv('HOME')

from modules.aichat import AIchat
from modules.circles import Circles
from modules.player import Player
from modules.power import Power
from modules.user import User
from modules.workspaces import WorkspacesBox
from modules.applets import Applets
from modules.dashboard import Dashboard
from modules.wallpapers import Wallpapers
from modules.mainstack import MainStack
from scripts.listen import listen
from modules.bar import Bar # Should always be the last module
