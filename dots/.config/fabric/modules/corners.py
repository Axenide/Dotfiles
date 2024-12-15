from fabric.widgets.box import Box
from fabric.widgets.centerbox import CenterBox
from fabric.widgets.button import Button
from fabric.widgets.wayland import WaylandWindow as Window
from fabric.widgets.shapes import Corner
from gi.repository import GLib

class MyCorner(Box):
    def __init__(self, corner):
        super().__init__(
            name="corner-container",
            children=Corner(
                name="corner",
                orientation=corner,
                size=20,
            ),
        )

class Corners(Window):
    def __init__(self):
        super().__init__(
            name="corners",
            layer="top",
            anchor="top bottom left right",
            exclusivity="normal",
            pass_through=True,
            visible=False,
            all_visible=False,
        )

        self.all_corners = Box(
            name="all-corners",
            orientation="v",
            h_expand=True,
            v_expand=True,
            h_align="fill",
            v_align="fill",
            children=[
                Box(
                    name="top-corners",
                    orientation="h",
                    h_align="fill",
                    children=[
                        MyCorner("top-left"),
                        Box(h_expand=True),
                        MyCorner("top-right"),
                    ],
                ),
                Box(v_expand=True),
                Box(
                    name="bottom-corners",
                    orientation="h",
                    h_align="fill",
                    children=[
                        MyCorner("bottom-left"),
                        Box(h_expand=True),
                        MyCorner("bottom-right"),
                    ],
                ),
            ],
        )

        self.add(self.all_corners)

        self.show_all()
