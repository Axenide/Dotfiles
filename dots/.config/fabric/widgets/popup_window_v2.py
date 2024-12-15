from typing import Literal

from utils.hyprland_monitor import HyprlandWithMonitors
from gi.repository import GLib

from fabric.widgets.box import Box
from fabric.widgets.eventbox import EventBox
from fabric.widgets.revealer import Revealer
from fabric.widgets.wayland import WaylandWindow
from fabric.widgets.widget import Widget


# Greatly inspired by:
#   CREDIT TO AYLUR: https://github.com/Aylur/dotfiles/blob/main/ags/widget/PopupWindow.ts

class Padding(EventBox):
    def __init__(self, name: str | None = None, style: str = "", **kwargs):
        super().__init__(
            name=name,
            h_expand=True,
            v_expand=True,
            child=Box(style=style, h_expand=True, v_expand=True),
            events=["button-press"],
            **kwargs,
        )
        self.set_can_focus(False)


class PopupRevealer(Box):
    def __init__(
        self,
        popup_window: WaylandWindow,
        decorations: str = "padding: 1px;",
        name: str | None = None,
        child: Widget | None = None,
        transition_type: Literal[
            "none",
            "crossfade",
            "slide-right",
            "slide-left",
            "slide-up",
            "slide-down",
        ] = "slide-down",
        transition_duration: int = 400,
    ):
        self.revealer: Revealer = Revealer(
            name=name,
            child=child,
            transition_type=transition_type,
            transition_duration=transition_duration,
            notify_child_revealed=lambda revealer, _: [
                revealer.hide(),
                popup_window.set_visible(False),
            ]
            if not revealer.fully_revealed
            else None,
            notify_reveal_child=lambda revealer, _: [
                popup_window.set_visible(True),
            ]
            if revealer.child_revealed
            else None,
        )
        super().__init__(
            style=decorations,
            children=self.revealer,
        )


def make_layout(anchor: str, name: str, popup: PopupRevealer, **kwargs) -> Box:
    match anchor:
        case "center-left":
            return Box(
                children=[
                    Box(
                        orientation="vertical",
                        children=[
                            Padding(name=name, **kwargs),
                            popup,
                            Padding(name=name, **kwargs),
                        ],
                    ),
                    Padding(name=name, **kwargs),
                ]
            )

        case "center":
            return Box(
                children=[
                    Padding(name=name, **kwargs),
                    Box(
                        orientation="vertical",
                        children=[
                            Padding(name=name, **kwargs),
                            popup,
                            Padding(name=name, **kwargs),
                        ],
                    ),
                    Padding(name=name, **kwargs),
                ]
            )
        case "center-right":
            return Box(
                children=[
                    Padding(name=name, **kwargs),
                    Box(
                        orientation="vertical",
                        children=[
                            Padding(name=name, **kwargs),
                            popup,
                            Padding(name=name, **kwargs),
                        ],
                    ),
                ]
            )
        case "top":
            return Box(
                children=[
                    Padding(name=name, **kwargs),
                    Box(
                        orientation="vertical",
                        children=[popup, Padding(name=name, **kwargs)],
                    ),
                    Padding(name=name, **kwargs),
                ]
            )
        case "top-right":
            return Box(
                children=[
                    Padding(name=name, **kwargs),
                    Box(
                        h_expand=False,
                        orientation="vertical",
                        children=[popup, Padding(name=name, **kwargs)],
                    ),
                ]
            )
        case "top-center":
            return Box(
                children=[
                    Padding(name=name, **kwargs),
                    Box(
                        h_expand=False,
                        orientation="vertical",
                        children=[popup, Padding(name=name, **kwargs)],
                    ),
                    Padding(name=name, **kwargs),
                ]
            )
        case "top-left":
            return Box(
                children=[
                    Box(
                        h_expand=False,
                        orientation="vertical",
                        children=[popup, Padding(name=name, **kwargs)],
                    ),
                    Padding(name=name, **kwargs),
                ]
            )
        case "bottom-left":
            return Box(
                children=[
                    Box(
                        h_expand=False,
                        orientation="vertical",
                        children=[Padding(name=name, **kwargs), popup],
                    ),
                    Padding(name=name, **kwargs),
                ]
            )
        case "bottom-center":
            return Box(
                children=[
                    Padding(name=name, **kwargs),
                    Box(
                        h_expand=False,
                        orientation="vertical",
                        children=[Padding(name=name, **kwargs), popup],
                    ),
                    Padding(name=name, **kwargs),
                ]
            )
        case "bottom-right":
            return Box(
                children=[
                    Padding(name=name, **kwargs),
                    Box(
                        h_expand=True,
                        orientation="vertical",
                        children=[Padding(name=name, **kwargs), popup],
                    ),
                ]
            )
        case _:
            return None


class PopupWindow(WaylandWindow):
    def __init__(
        self,
        name: str = "popup-window",
        decorations: str = "padding: 1px;",
        child: Widget | None = None,
        transition_type: Literal[
            "none",
            "crossfade",
            "slide-right",
            "slide-left",
            "slide-up",
            "slide-down",
        ]
        | None = None,
        transition_duration: int = 100,
        popup_visible: bool = False,
        anchor: Literal[
            "center-left",
            "center",
            "center-right",
            "top",
            "top-right",
            "top-center",
            "top-left",
            "bottom-left",
            "bottom-center",
            "bottom-right",
        ] = "top-right",
        enable_inhibitor: bool = False,
        keyboard_mode: Literal["none", "exclusive", "on-demand"] = "on-demand",
        timeout: int = 1000,
        **kwargs,
    ):
        self.timeout = timeout
        self.currtimeout = 0
        self.popup_running = False

        self.popup_visible = popup_visible

        self.enable_inhibitor = enable_inhibitor

        self.monitor_number: int | None = None
        self.hyprland_monitor = HyprlandWithMonitors()

        self.reveal_child = PopupRevealer(
            name=name,
            popup_window=self,
            child=child,
            transition_type=transition_type,
            transition_duration=transition_duration,
            decorations=decorations,
        )

        super().__init__(
            layer="top",
            keyboard_mode=keyboard_mode,
            visible=False,
            exclusivity="normal",
            anchor="top bottom right left",
            child=make_layout(
                anchor=anchor,
                name=name,
                popup=self.reveal_child,
                on_button_press_event=self.on_inhibit_click,
            ),
            on_key_release_event=self.on_key_release,
        )

    def on_key_release(self, _, event_key):
        if event_key.get_keycode()[1] == 9:
            self.popup_visible = False
            self.reveal_child.revealer.set_reveal_child(self.popup_visible)

    def on_inhibit_click(self, *_):
        self.popup_visible = False
        self.reveal_child.revealer.set_reveal_child(self.popup_visible)

    def toggle_popup(self, monitor: bool = False):
        if monitor:
            curr_monitor = self.hyprland_monitor.get_current_gdk_monitor_id()
            self.monitor = curr_monitor
            if self.monitor_number != curr_monitor and self.popup_visible:
                self.monitor_number = curr_monitor
                return

            self.monitor_number = curr_monitor

        if not self.popup_visible:
            self.reveal_child.revealer.show()

        self.popup_visible = not self.popup_visible
        self.reveal_child.revealer.set_reveal_child(self.popup_visible)

    def popup_timeout(self):
        curr_monitor = self.hyprland_monitor.get_current_gdk_monitor_id()
        self.monitor = curr_monitor

        if not self.popup_visible:
            self.reveal_child.revealer.show()
        if self.popup_running:
            self.currtimeout = 0
            return
        self.popup_visible = True
        self.reveal_child.revealer.set_reveal_child(self.popup_visible)
        self.popup_running = True

        def popup_func():
            if self.currtimeout >= self.timeout:
                self.popup_visible = False
                self.reveal_child.revealer.set_reveal_child(self.popup_visible)
                self.currtimeout = 0
                self.popup_running = False
                return False
            self.currtimeout += 500
            return True

        GLib.timeout_add(500, popup_func)
