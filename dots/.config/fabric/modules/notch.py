from os import truncate
from fabric.widgets.box import Box
from fabric.widgets.label import Label
from fabric.widgets.centerbox import CenterBox
from fabric.widgets.button import Button
from fabric.widgets.stack import Stack
from fabric.widgets.wayland import WaylandWindow as Window
from fabric.hyprland.widgets import ActiveWindow
from fabric.utils.helpers import FormattedString, truncate, get_relative_path
from fabric.core.fabricator import Fabricator
from gi.repository import GLib, Gdk
from modules.launcher import AppLauncher
from modules.dashboard import Dashboard
from modules.wallpapers import WallpaperSelector
from modules.notification_popup import NotificationContainer
from modules.power import PowerMenu
from modules.corners import MyCorner
import modules.icons as icons
import modules.data as data

class Notch(Window):
    def __init__(self, **kwargs):
        super().__init__(
            name="notch",
            layer="top",
            anchor="top",
            margin="-40px 10px 10px 10px",
            keyboard_mode="none",
            exclusivity="normal",
            visible=True,
            all_visible=True,
        )

        self.dashboard = Dashboard()
        self.launcher = AppLauncher()
        self.wallpapers = WallpaperSelector(data.WALLPAPERS_DIR)
        self.notification = NotificationContainer()
        self.power = PowerMenu()

        self.active_window = ActiveWindow(
            name="hyprland-window",
            h_expand=True,
            formatter=FormattedString(
                f"{{'{data.USERNAME}@{data.HOSTNAME}' if not win_title else truncate(win_title, 30)}}",
                truncate=truncate,
            ),
        )

        # self.cava = Box(
        #     name="cava",
        #     spacing=1,
        #     children=[Box() for _ in range(28)]  # Usa "_" si no utilizas el índice
        # ).build(
        #     lambda box, _: Fabricator(
        #         poll_from=f"cava -p {get_relative_path('cava.ini')}",  # Ruta al archivo de configuración
        #         interval=0,  # Intervalo de actualización
        #         stream=True,  # Habilita el stream para datos en tiempo real
        #         on_changed=lambda f, line: [
        #             child.set_style(
        #                 f"* {{ margin-top: {26 - value}px; }}",  # Ajusta el margen superior dinámicamente
        #                 compile=False,
        #                 add_brackets=False,
        #             )
        #             for value, child in zip(
        #                 [
        #                     int(val)  # Convierte cada valor a entero
        #                     for val in line.strip(";").split(";")  # Elimina ";" al inicio y final, luego separa
        #                 ],
        #                 box.children,  # Empareja cada valor con un hijo
        #             )
        #         ],
        #     )
        # )

        self.compact = Button(
            name="notch-compact",
            h_expand=True,
            on_clicked=lambda *_: self.open_notch("dashboard"),
            child=self.active_window,
        )

        self.button_media = Button(
            name="button-bar",
            v_expand=False,
            on_clicked=self.on_button_clicked,
            child=Label(
                name="button-bar-label",
                markup=icons.media
            )
        )
        self.button_media.connect("enter-notify-event", self.on_button_enter)
        self.button_media.connect("leave-notify-event", self.on_button_leave)
        
        self.button_color = Button(
            name="button-bar",
            tooltip_text="Color Picker\nLeft Click: HEX\nMiddle Click: HSV\nRight Click: RGB",
            v_expand=False,
            child=Label(
                name="button-bar-label",
                markup=icons.colorpicker
            )
        )
        self.button_color.connect("enter-notify-event", self.on_button_enter)
        self.button_color.connect("leave-notify-event", self.on_button_leave)
        self.button_color.connect("button-press-event", self.colorpicker)

        self.stack = Stack(
            name="notch-content",
            v_expand=True,
            h_expand=True,
            transition_type="crossfade",
            transition_duration=250,
            children=[
                self.compact,
                self.launcher,
                self.dashboard,
                self.wallpapers,
                self.notification,
                self.power,
            ]
        )

        self.corner_left = Box(
            name="notch-corner-left",
            orientation="v",
            children=[
                MyCorner("top-right"),
                Box(),
            ]
        )

        self.corner_right = Box(
            name="notch-corner-right",
            orientation="v",
            children=[
                MyCorner("top-left"),
                Box(),
            ]
        )

        self.notch_box = CenterBox(
            name="notch-box",
            orientation="h",
            h_align="center",
            v_align="center",
            start_children=Box(
                children=[
                    Box(
                        name="button-media-box",
                        orientation="v",
                        v_expand=True,
                        children=[
                            self.button_media,
                            Box(v_expand=True),
                        ],
                    ),
                    self.corner_left,
                ],
            ),
            center_children=self.stack,
            end_children=Box(
                children=[
                    self.corner_right,
                    Box(
                        name="button-color-box",
                        orientation="v",
                        v_expand=True,
                        children=[
                            self.button_color,
                            Box(v_expand=True),
                        ],
                    )
                ]
            )
        )

        self.hidden = False

        self.add(self.notch_box)
        self.show_all()
        self.wallpapers.viewport.hide()

        self.add_keybinding("Escape", lambda *_: self.close_notch())
        self.add_keybinding("Ctrl Tab", lambda *_: self.dashboard.go_to_next_child())
        self.add_keybinding("Ctrl Shift ISO_Left_Tab", lambda *_: self.dashboard.go_to_previous_child())

    def on_button_enter(self, widget, event):
        window = widget.get_window()
        if window:
            window.set_cursor(Gdk.Cursor(Gdk.CursorType.HAND2))

    def on_button_leave(self, widget, event):
        window = widget.get_window()
        if window:
            window.set_cursor(None)

    def close_notch(self):
        self.set_keyboard_mode("none")

        if self.hidden:
            self.notch_box.remove_style_class("hideshow")
            self.notch_box.add_style_class("hidden")

        for widget in [self.launcher, self.dashboard, self.wallpapers, self.notification, self.power]:
            widget.remove_style_class("open")
            if widget == self.wallpapers:
                self.wallpapers.viewport.hide()
                self.wallpapers.viewport.set_property("name", None)
        for style in ["launcher", "dashboard", "wallpapers", "notification", "power"]:
            self.stack.remove_style_class(style)
        self.stack.set_visible_child(self.compact)

    def open_notch(self, widget):
        self.set_keyboard_mode("exclusive")

        if self.hidden:
            self.notch_box.remove_style_class("hidden")
            self.notch_box.add_style_class("hideshow")

        widgets = {
            "launcher": self.launcher,
            "dashboard": self.dashboard,
            "wallpapers": self.wallpapers,
            "notification": self.notification,
            "power": self.power
        }

        # Limpiar clases y estados previos
        for style in widgets.keys():
            self.stack.remove_style_class(style)
        for w in widgets.values():
            w.remove_style_class("open")
        
        # Configurar según el widget solicitado
        if widget in widgets:
            self.stack.add_style_class(widget)
            self.stack.set_visible_child(widgets[widget])
            widgets[widget].add_style_class("open")
            
            # Acciones específicas para el launcher
            if widget == "launcher":
                self.launcher.open_launcher()
                self.launcher.search_entry.set_text("")
                self.launcher.search_entry.grab_focus()

            if widget == "notification":
                self.set_keyboard_mode("none")

            if widget == "wallpapers":
                self.wallpapers.search_entry.set_text("")
                self.wallpapers.search_entry.grab_focus()
                GLib.timeout_add(
                    500, 
                    lambda: (
                        self.wallpapers.viewport.show(), 
                        self.wallpapers.viewport.set_property("name", "wallpaper-icons")
                    )
                )

            if widget != "wallpapers":
                self.wallpapers.viewport.hide()
                self.wallpapers.viewport.set_property("name", None)

        else:
            self.stack.set_visible_child(self.dashboard)

    def colorpicker(self, button, event):
        if event.button == 1:
            GLib.spawn_command_line_async(f"bash {get_relative_path('../scripts/hyprpicker-hex.sh')}")
        elif event.button == 2:
            GLib.spawn_command_line_async(f"bash {get_relative_path('../scripts/hyprpicker-hsv.sh')}")
        elif event.button == 3:
            GLib.spawn_command_line_async(f"bash {get_relative_path('../scripts/hyprpicker-rgb.sh')}")

    def on_button_clicked(self, *args):
        # Ejecuta notify-send cuando se hace clic en el botón
        GLib.spawn_command_line_async("notify-send 'Botón presionado' '¡Funciona!'")

    def toggle_hidden(self):
        self.hidden = not self.hidden
        if self.hidden:
            self.notch_box.add_style_class("hidden")
        else:
            self.notch_box.remove_style_class("hidden")
