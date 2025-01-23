import os
from fabric import Application
from fabric.widgets.box import Box
from fabric.widgets.label import Label
from fabric.widgets.datetime import DateTime
from fabric.widgets.centerbox import CenterBox
from fabric.widgets.button import Button
from fabric.widgets.stack import Stack
from fabric.widgets.wayland import WaylandWindow as Window
from fabric.hyprland.widgets import Workspaces, WorkspaceButton
from fabric.utils import get_relative_path
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Vte', '2.91')
from gi.repository import GLib, Gtk, Gdk, Vte, Pango
import modules.icons as icons
from modules.calendar import Calendar

class Buttons(Box):
    def __init__(self, **kwargs):
        super().__init__(
            name="buttons",
            spacing=4,
            h_align="center",
            v_align="start",
            h_expand=True,
            v_expand=True,
            visible=True,
            all_visible=True,
        )

        self.network_status_button = Button(
            name="network-status-button",
            h_expand=True,
            child=Box(
                h_align="start",
                v_align="center",
                spacing=10,
                children=[
                    Label(
                        name="network-icon",
                        markup=icons.wifi,
                    ),
                    Box(
                        name="network-text",
                        orientation="v",
                        h_align="start",
                        v_align="center",
                        children=[
                            Box(
                                children=[
                                    Label(
                                        name="network-label",
                                        label="Wi-Fi",
                                        justification="left",
                                    ),
                                    Box(h_expand=True),
                                ]
                            ),
                            Box(
                                children=[
                                    Label(
                                        name="network-ssid",
                                        label="ARGOS_5GHz",
                                        justification="left",
                                    ),
                                    Box(h_expand=True),
                                ]
                            ),
                        ]
                    ),
                ],
            )
        )

        self.network_menu_button = Button(
            name="network-menu-button",
            child=Label(
                name="network-menu-label",
                markup=icons.chevron_right,
            ),
        )

        self.network_button = Box(
            name="network-button",
            orientation="h",
            h_align="fill",
            v_align="center",
            h_expand=True,
            v_expand=True,
            children=[
                self.network_status_button,
                self.network_menu_button,
            ],
        )

        self.bluetooth_status_button = Button(
            name="bluetooth-status-button",
            h_expand=True,
            child=Box(
                h_align="start",
                v_align="center",
                spacing=10,
                children=[
                    Label(
                        name="bluetooth-icon",
                        markup=icons.bluetooth,
                    ),
                    Box(
                        name="bluetooth-text",
                        orientation="v",
                        h_align="start",
                        v_align="center",
                        children=[
                            Box(
                                children=[
                                    Label(
                                        name="bluetooth-label",
                                        label="Bluetooth",
                                        justification="left",
                                    ),
                                    Box(h_expand=True),
                                ]
                            ),
                            Box(
                                children=[
                                    Label(
                                        name="bluetooth-status",
                                        label="Connected",
                                        justification="left",
                                    ),
                                    Box(h_expand=True),
                                ]
                            ),
                        ]
                    ),
                ],
            )
        )

        self.bluetooth_menu_button = Button(
            name="bluetooth-menu-button",
            child=Label(
                name="bluetooth-menu-label",
                markup=icons.chevron_right,
            ),
        )

        self.bluetooth_button = Box(
            name="bluetooth-button",
            orientation="h",
            h_align="fill",
            v_align="center",
            h_expand=True,
            v_expand=True,
            children=[
                self.bluetooth_status_button,
                self.bluetooth_menu_button,
            ],
        )

        self.night_mode_button = Button(
            name="night-mode-button",
            child=Box(
                h_align="start",
                v_align="center",
                spacing=10,
                children=[
                    Label(
                        name="night-mode-icon",
                        markup=icons.night,
                    ),
                    Box(
                        name="night-mode-text",
                        orientation="v",
                        h_align="start",
                        v_align="center",
                        children=[
                            Box(
                                children=[
                                    Label(
                                        name="night-mode-label",
                                        label="Night Mode",
                                        justification="left",
                                    ),
                                    Box(h_expand=True),
                                ]
                            ),
                            Box(
                                children=[
                                    Label(
                                        name="night-mode-status",
                                        label="Enabled",
                                        justification="left",
                                    ),
                                    Box(h_expand=True),
                                ]
                            ),
                        ]
                    )
                ],
            )
        )

        self.caffeine_button = Button(
            name="caffeine-button",
            child=Box(
 h_align="start",
                v_align="center",
                spacing=10,
                children=[
                    Label(
                        name="caffeine-icon",
                        markup=icons.coffee,
                    ),
                    Box(
                        name="caffeine-text",
                        orientation="v",
                        h_align="start",
                        v_align="center",
                        children=[
                            Box(
                                children=[
                                    Label(
                                        name="caffeine-label",
                                        label="Caffeine",
                                        justification="left",
                                    ),
                                    Box(h_expand=True),
                                ]
                            ),
                            Box(
                                children=[
                                    Label(
                                        name="caffeine-status",
                                        label="Enabled",
                                        justification="left",
                                    ),
                                    Box(h_expand=True),
                                ]
                            ),
                        ]
                    )
                ],
            )
        )

        self.add(self.network_button)
        self.add(self.bluetooth_button)
        self.add(self.night_mode_button)
        self.add(self.caffeine_button)

        self.show_all()

class Widgets(Box):
    def __init__(self, **kwargs):
        super().__init__(
            name="dash-widgets",
            h_align="center",
            v_align="start",
            h_expand=True,
            v_expand=True,
            visible=True,
            all_visible=True,
        )

        self.buttons = Buttons()

        self.box_1 = Box(
            name="box-1",
        )

        self.box_2 = Box(
            name="box-2",
            h_expand=True,
        )

        self.box_3 = Box(
            name="box-3",
        )

        self.box_4 = Box(
            name="box-4",
            orientation="h",
            spacing=4,
            children=[
                Box(
                    name="box-x",
                    h_expand=True,
                ),
                Box(
                    name="box-x",
                    h_expand=True,
                ),
                Box(
                    name="box-x",
                    h_expand=True,
                ),
            ]
        )

        self.container_1 = Box(
            name="container-1",
            orientation="h",
            spacing=8,
            children=[
                self.box_2,
                self.box_3,
            ]
        )

        self.container_2 = Box(
            name="container-2",
            orientation="v",
            spacing=8,
            children=[
                self.buttons,
                self.box_4,
                self.container_1,
            ]
        )

        self.container_3 = Box(
            name="container-3",
            orientation="h",
            spacing=8,
            children=[
                self.box_1,
                self.container_2,
            ]
        )

        self.add(self.container_3)

        self.show_all()

class Dashboard(Box):
    def __init__(self, **kwargs):
        super().__init__(
            name="dashboard",
            orientation="v",
            spacing=8,
            h_align="center",
            v_align="start",
            h_expand=True,
            v_expand=True,
            visible=True,
            all_visible=True,
        )

        self.widgets = Widgets()

        self.calendar = Calendar()

        self.stack = Stack(
            name="stack",
            transition_type="slide-left-right",
            transition_duration=500,
        )

        self.switcher = Gtk.StackSwitcher(
            name="switcher",
            spacing=8,
        )

        self.label_1 = Label(
            name="label-1",
            label="Widgets",
        )

        self.label_2 = Label(
            name="label-2",
            label="Clipboard",
        )

        self.label_3 = Label(
            name="label-3",
            label="To-Do",
        )

        self.label_4 = Label(
            name="label-4",
            label="Calendar",
        )

        # Terminal integrada
        self.terminal = Vte.Terminal()
        self.terminal.spawn_async(
            Vte.PtyFlags.DEFAULT,        # Flags
            os.path.expanduser("~"),     # Working directory
            ["/bin/fish"],               # Comando
            None,                        # Variables de entorno
            GLib.SpawnFlags.DO_NOT_REAP_CHILD,  # Spawn flags
            None,                        # Función de configuración (opcional)
            None,                        # Datos adicionales para la función (opcional)
            -1,                          # Timeout
            None,                        # GLib.Cancellable
            None                         # Callback de finalización
        )
        self.terminal.set_font(Pango.FontDescription("ZedMono Nerd Font"))

        self.stack.add_titled(self.widgets, "widgets", "Widgets")
        self.stack.add_titled(self.label_2, "clipboard", "Clipboard")
        self.stack.add_titled(self.label_3, "to-do", "To-Do")
        self.stack.add_titled(self.calendar, "calendar", "Calendar")
        self.stack.add_titled(self.terminal, "terminal", "Terminal")

        self.switcher.set_stack(self.stack)
        self.switcher.set_hexpand(True)
        self.switcher.set_homogeneous(True)
        self.switcher.set_can_focus(True)

        self.add(self.switcher)
        self.add(self.stack)

        self.show_all()

    def go_to_next_child(self):
        children = self.stack.get_children()
        current_index = self.get_current_index(children)
        next_index = (current_index + 1) % len(children)
        self.stack.set_visible_child(children[next_index])

    def go_to_previous_child(self):
        children = self.stack.get_children()
        current_index = self.get_current_index(children)
        previous_index = (current_index - 1 + len(children)) % len(children)
        self.stack.set_visible_child(children[previous_index])

    def get_current_index(self, children):
        current_child = self.stack.get_visible_child()
        return children.index(current_child) if current_child in children else -1
