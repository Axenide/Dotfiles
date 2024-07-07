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
        self.calendar = Calendar()

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
                        Label(name="ext-label", label="<span font-family='tabler-icons'>&#xf814;</span> No Notifications!", markup=True),
                    ]
                )
            ]
        )

        self.set_children(
            [
                self.applets,
                self.player,
                self.ext,
                self.circles,
                self.calendar,
            ]
        )
