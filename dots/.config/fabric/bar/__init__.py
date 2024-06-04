import os
import signal
import time
import subprocess

from thefuzz import fuzz, process

import dbus
import fabric
from fabric.utils.fabricator import Fabricator
from fabric.utils import (
    Application,
    FormattedString,
    invoke_repeater,
    bulk_connect,
    exec_shell_command,
    exec_shell_command_async,
    get_relative_path,
    set_stylesheet_from_file,
    get_desktop_applications,
)

from fabric.widgets import (
    Box,
    Button,
    CenterBox,
    CircularProgressBar,
    DateTime,
    EventBox,
    Entry,
    Image,
    Label,
    Overlay,
    Revealer,
    Scale,
    ScrolledWindow,
    Stack,
    SystemTray,
    WaylandWindow as Window,
    WebView,
    HyprlandWorkspaceButton as WorkspaceButton,
    HyprlandWorkspaces as Workspaces,
)

import gi
from gi.repository import GLib, Gdk, GdkPixbuf, Gtk
from loguru import logger
import psutil
import psutil
import setproctitle

gi.require_version("Gtk", "3.0")

from fabric.hyprland.service import Hyprland
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
