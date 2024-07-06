from __init__ import *
from .apps import *

class MainStack(Stack):
    def __init__(self):
        super().__init__(
            name="main-stack",
            transition_type="slide-left",
            transition_duration=500,
            h_expand=True,
            v_expand=True,
        )

        self.chat = AIchat()
        self.dashboard = Dashboard()
        self.wallpapers = Wallpapers(self)
        self.apps = Apps()

        self.set_children(
            [
                self.chat,
                self.dashboard,
                self.apps,
                self.wallpapers,
            ]
        )
