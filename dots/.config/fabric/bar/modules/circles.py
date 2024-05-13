from __init__ import *

class Circles(Box):
    def __init__(self):
        super().__init__(
            visible=False,
            all_visible=False,
        )
        self.cpu_circular_progress_bar = CircularProgressBar(
            size=(50, 50),
            line_style="none",
            percentage=0,
            name="cpu_circular-progress-bar",
        )
        self.memory_circular_progress_bar = CircularProgressBar(
            size=(50, 50),
            line_style="none",
            percentage=0,
            name="memory_circular-progress-bar",
        )
        self.battery_circular_progress_bar = CircularProgressBar(
            size=(50, 50),
            line_style="none",
            percentage=100,
            name="battery_circular-progress-bar",
        )
        GLib.Thread.new(None, self.update_status)
        self.add(
            Box(
                spacing=24,
                name="circles-container",
                v_expand=True,
                orientation="v",
                children=[
                    Box(
                        name="circular-progress-bar-container",
                        v_expand=True,
                        v_align="fill",
                        spacing=4,
                        orientation="v",
                        children=[
                            Box(
                                children=[
                                    Overlay(
                                        children=self.cpu_circular_progress_bar,
                                        overlays=[
                                            Image(
                                                image_file=get_relative_path("../assets/cpu.svg"),
                                            ),
                                        ],
                                    )
                                ],
                            ),
                            Box(
                                children=[
                                    Overlay(
                                        children=self.memory_circular_progress_bar,
                                        overlays=[
                                            Image(
                                                image_file=get_relative_path("../assets/ram.svg"),
                                            ),
                                        ],
                                    )
                                ]
                            ),
                            Box(
                                children=[
                                    Overlay(
                                        children=self.battery_circular_progress_bar,
                                        overlays=[
                                            Image(
                                                image_file=get_relative_path("../assets/bolt.svg"),
                                            ),
                                        ],
                                    ),
                                ]
                            ),
                        ],
                    ),
                ],
            ),
        )
        self.show_all()

    def update_status(self):
        while True:
            self.cpu_circular_progress_bar.percentage = psutil.cpu_percent(interval=1)
            self.memory_circular_progress_bar.percentage = psutil.virtual_memory().percent
            self.battery_circular_progress_bar.percentage = (
                psutil.sensors_battery().percent
                if psutil.sensors_battery() is not None
                else 100
            )
