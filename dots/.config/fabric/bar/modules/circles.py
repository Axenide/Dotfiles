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

        self.cpu_icon = Label(name="cpu-icon", label="<span>&#xef8e;</span>", markup=True)
        self.memory_icon = Label(name="memory-icon", label="<span>&#xfa97;</span>", markup=True)
        self.battery_icon = Label(name="battery-icon", label="<span>&#xea38;</span>", markup=True)

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
                        v_align="center",
                        spacing=4,
                        orientation="v",
                        children=[
                            Box(
                                children=[
                                    Overlay(
                                        children=self.cpu_circular_progress_bar,
                                        overlays=[self.cpu_icon],
                                    )
                                ],
                            ),
                            Box(
                                children=[
                                    Overlay(
                                        children=self.memory_circular_progress_bar,
                                        overlays=[self.memory_icon],
                                    )
                                ]
                            ),
                            Box(
                                children=[
                                    Overlay(
                                        children=self.battery_circular_progress_bar,
                                        overlays=[self.battery_icon],
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
