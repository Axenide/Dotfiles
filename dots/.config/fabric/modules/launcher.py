import operator
from collections.abc import Iterator
from fabric import Application
from fabric.widgets.box import Box
from fabric.widgets.label import Label
from fabric.widgets.button import Button
from fabric.widgets.entry import Entry
from fabric.widgets.scrolledwindow import ScrolledWindow
from fabric.widgets.wayland import WaylandWindow as Window
from fabric.utils import DesktopApp, get_desktop_applications, idle_add, remove_handler
from fabric.utils import get_relative_path
from gi.repository import GLib
import modules.icons as icons

class AppLauncher(Box):
    def __init__(self, **kwargs):
        super().__init__(
            name="app-launcher",
            visible=False,
            all_visible=False,
            **kwargs,
        )
        self._arranger_handler: int = 0
        self._all_apps = get_desktop_applications()

        self.viewport = Box(name="viewport", spacing=4, orientation="v")
        self.search_entry = Entry(
            name="search-entry",
            placeholder="Search Applications...",
            h_expand=True,
            notify_text=lambda entry, *_: self.arrange_viewport(entry.get_text()),
            on_activate=lambda entry, *_: self.on_search_entry_activate(entry.get_text()),
            on_button_press_event=print,
        )
        self.search_entry.props.xalign = 0.5
        self.scrolled_window = ScrolledWindow(
            name="scrolled-window",
            spacing=10,
            min_content_size=(450, 105),
            max_content_size=(450, 105),
            child=self.viewport,
        )

        self.header_box = Box(
            name="header_box",
            spacing=10,
            orientation="h",
            children=[
                self.search_entry,
                Button(
                    name="close-button",
                    child=Label(name="close-label", markup=icons.cancel),
                    tooltip_text="Exit",
                    on_clicked=lambda *_: self.close_launcher()
                ),
            ],
        )
        
        self.launcher_box = Box(
            name="launcher-box",
            spacing=10,
            h_expand=True,
            orientation="v",
            children=[
                self.header_box,
                self.scrolled_window,
            ],
        )

        self.resize_viewport()

        self.add(self.launcher_box)
        self.connect("key-press-event", self.on_key_press_event)
        self.show_all()

    def close_launcher(self):
        # Elimina todos los slots de aplicaciones
        self.viewport.children = []
        GLib.spawn_command_line_async("fabric-cli exec ax-shell 'notch.close_notch()'")

    def open_launcher(self):
        # Vuelve a cargar la lista de aplicaciones
        self._all_apps = get_desktop_applications()
        self.arrange_viewport()

    def on_key_press_event(self, widget, event):
        if event.keyval == 65307:  # Escape key
            self.close_launcher()

    def arrange_viewport(self, query: str = ""):
        remove_handler(self._arranger_handler) if self._arranger_handler else None
        self.viewport.children = []

        filtered_apps_iter = iter(
            sorted(
                [
                    app
                    for app in self._all_apps
                    if query.casefold()
                    in (
                        (app.display_name or "")
                        + (" " + app.name + " ")
                        + (app.generic_name or "")
                    ).casefold()
                ],
                key=lambda app: (app.display_name or "").casefold(),
            )
        )
        should_resize = operator.length_hint(filtered_apps_iter) == len(self._all_apps)

        self._arranger_handler = idle_add(
            lambda *args: self.add_next_application(*args)
            or (self.resize_viewport() if should_resize else False),
            filtered_apps_iter,
            pin=True,
        )

        return False

    def add_next_application(self, apps_iter: Iterator[DesktopApp]):
        if not (app := next(apps_iter, None)):
            return False

        self.viewport.add(self.bake_application_slot(app))
        return True

    def resize_viewport(self):
        self.scrolled_window.set_min_content_width(
            self.viewport.get_allocation().width  # type: ignore
        )
        return False

    def bake_application_slot(self, app: DesktopApp, **kwargs) -> Button:
        return Button(
            name="app-slot-button",
            child=Box(
                name="app-slot-box",
                orientation="h",
                spacing=10,
                children=[
                    Label(
                        name="app-label",
                        label=app.display_name or "Unknown",
                        ellipsization="end",
                        v_align="center",
                        h_align="center",
                    ),
                ],
            ),
            tooltip_text=app.description,
            on_clicked=lambda *_: (app.launch(), self.close_launcher()),
            **kwargs,
        )

    def on_search_entry_activate(self, text):
        if text == ":wp":
            GLib.spawn_command_line_async("fabric-cli exec ax-shell 'notch.open_notch(\"wallpapers\")'")

