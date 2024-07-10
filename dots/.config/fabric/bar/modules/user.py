from __init__ import *

PROFILE_PICTURE = f"{home_dir}/.face.icon"

class User(Box):
    def __init__(self):
        super().__init__(
            name="user",
            visible=False,
            all_visible=False,
            h_expand=True,
        )
        self.user_label = Label(
            name="user-label",
            h_align="left",
            label=f"{user.capitalize()}",
        )
        self.host_label = Label(
            name="host-label",
            h_align="left",
            label=f"{host.capitalize()}",
        )
        self.user_box = Box(
            name="user-box",
            orientation="v",
            v_align="center",
            children=[
                self.user_label,
                self.host_label,
            ]
        )
        self.user_image = Box(
            name="user-image",
            style="background-image: url(\"" + PROFILE_PICTURE + "\");",
        )
        self.add(
            Box(
                name="user-container",
                h_expand=True,
                v_align="center",
                orientation="h",
                children=[
                    self.user_image,
                    self.user_box,
                ]
            )
        )
