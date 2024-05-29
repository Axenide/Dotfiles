from __init__ import *

class Dashboard(Box):
    def __init__(self):
        super().__init__(
            name="dashboard",
            spacing=4,
            orientation="v",
            h_expand=True,
            v_expand=True,
        )

        self.applets = Applets()
        self.circles = Circles()
        self.player = Player()
        self.calendar = Gtk.Calendar(name="calendar", hexpand=True)
        
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
                        Label(name="ext-label", label="No Notifications!"),
                        Label(name="bell-label", label="<span>&#xf814;</span>", markup=True),
                        Label(name="ext-label-2", label="(Because I haven't coded that yet)"),
                    ]
                )
            ]
        )

        self.set_children(
            [
                self.applets,
                self.player,
                self.ext,
                Box(name="bottom-box", orientation="h", h_expand=True, spacing=4, children=[self.calendar, self.circles]),
            ]
        )
