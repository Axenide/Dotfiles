import os
import re
import signal
import time
import subprocess
import shutil
import json
import calendar
from datetime import datetime, timedelta

import dbus
import psutil
import setproctitle

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
    # SystemTray,
    WaylandWindow as Window,
    WebView,
    HyprlandWorkspaceButton as WorkspaceButton,
    HyprlandWorkspaces as Workspaces,
)

from fabric.widgets.shapes import Corner, CornerOrientation

import gi
from gi.repository import (
        GLib,
        Gdk,
        GdkPixbuf,
        Gtk,
        Gray,
)

from loguru import logger

gi.require_version("Gtk", "3.0")

home_dir = os.path.expanduser("~")
user = f"{os.getenv('USER')}".rstrip()
host = f"{exec_shell_command('hostname')}".rstrip()

fabricSend = f'python {home_dir}/.config/fabric/bar/modules/scripts/send.py'

from modules.scripts.listen import listen
import modules.scripts.utils as utils

import modules.icons as icons
from modules.master import MasterWithHover, MasterWithButton
from modules.power import Power
from modules.panels import Panels
from modules.calendar import Calendar
from modules.systray import SystemTray
from modules.apps import Apps
from modules.aichat import AIchat
from modules.circles import Circles
from modules.player import Player
from modules.user import User
from modules.workspaces import WorkspacesBox
from modules.applets import Applets
from modules.dashboard import Dashboard
from modules.themes import Themes
from modules.wallpapers import Wallpapers
from modules.mainstack import MainStack
# from modules.osd import OSD
from modules.bar import Bar # Should always be the last module
