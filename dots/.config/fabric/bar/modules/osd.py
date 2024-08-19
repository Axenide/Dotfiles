from __init__ import *

class OSD(Window):
    def __init__(self):
        super().__init__(
            name="osd",
            layer="top",
            anchor="bottom",
        )
