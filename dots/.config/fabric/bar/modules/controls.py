from __init__ import *

class Controls():
    def __init__(self):
        self.volume = EventBox(
            name="volume",
            children=[
                CircularProgressBar(
                    size=(42, 42),
                    line_style="round",
                    percentage=0,
                    name="volume-circular-progress-bar",
                ),
                Overlay(
                    overlays=[
                        Label(
                            name="vol-label",
                            label="",
                            markup=True,
                        )
                    ]
                ),
            ]
        )
