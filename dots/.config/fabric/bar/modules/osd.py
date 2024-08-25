from __init__ import *

class OSD(Window):
    def __init__(self):
        super().__init__(
            layer="top",
            anchor="bottom",
            margin="0px 0px 0px 0px",
            visible=True,
            all_visible=True,
            exclusive=False,
            keyboard_mode="none",
        )

        self.osd_label = Label(name="osd-label", label="Hello, World!", markup=True)

        self.osd_box = Box(
            name="osd-box",
            orientation="h",
            h_align="center",
            v_align="center",
            children=[
                self.osd_label
            ]
        )

        self.osd = Revealer(
            name="osd",
            transition_type="slide-up",
            transition_duration=500,
            reveal_child=True,
            child=self.osd_box
        )

        self.add(self.osd)
        
        GLib.Thread.new(None, self.commands)

    def commands(self):
        while True:
            command = listen()
            GLib.idle_add(self.binds, command)

    def binds(self, command):
        child_mapping = {
            "dashboard",
            "apps",
        }

        if command in child_mapping:
            if command == "dashboard":
                self.osd_label.set_label("Hello, World!")
            if command == "apps":
                self.osd_label.set_label("Hello, Apps!")

        return False
