from __init__ import *

class Circles(Box):
    def __init__(self):
        super().__init__(
            visible=False,
            all_visible=False,
        )

        self.cpu_circular_progress_bar = CircularProgressBar(
            size=(42, 42),
            line_style="round",
            percentage=0,
            name="cpu-circular-progress-bar",
        )

        self.memory_circular_progress_bar = CircularProgressBar(
            size=(42, 42),
            line_style="round",
            percentage=0,
            name="memory-circular-progress-bar",
        )

        self.battery_circular_progress_bar = CircularProgressBar(
            size=(42, 42),
            line_style="round",
            percentage=100,
            name="battery-circular-progress-bar",
        )

        self.disk_circular_progress_bar = CircularProgressBar(
            size=(42, 42),
            line_style="round",
            percentage=0,
            name="disk-circular-progress-bar",
        )

        self.temp_circular_progress_bar = CircularProgressBar(
            size=(42, 42),
            line_style="round",
            percentage=0,
            name="temp-circular-progress-bar",
        )

        GLib.Thread.new(None, self.update_status)

        self.temp_icon = Label(name="temp-icon", label="<span>&#xeb38;</span>", markup=True)
        self.disk_icon = Label(name="disk-icon", label="<span>&#xea88;</span>", markup=True)
        self.battery_icon = Label(name="battery-icon", label="<span>&#xea38;</span>", markup=True)
        self.memory_icon = Label(name="memory-icon", label="<span>&#xfa97;</span>", markup=True)
        self.cpu_icon = Label(name="cpu-icon", label="<span>&#xef8e;</span>", markup=True)

        self.add(
            Box(
                name="circles-container",
                h_expand=True,
                h_align="fill",
                orientation="h",
                children=[
                    Box(
                        h_expand=True,
                        h_align="center",
                        children=[
                            Overlay(
                                children=self.temp_circular_progress_bar,
                                overlays=[self.temp_icon],
                            )
                        ],
                    ),

                    Box(
                        h_expand=True,
                        h_align="center",
                        children=[
                            Overlay(
                                children=self.disk_circular_progress_bar,
                                overlays=[self.disk_icon],
                            )
                        ]
                    ),

                    Box(
                        h_expand=True,
                        h_align="center",
                        children=[
                            Overlay(
                                children=self.battery_circular_progress_bar,
                                overlays=[self.battery_icon],
                            ),
                        ]
                    ),

                    Box(
                        h_expand=True,
                        h_align="center",
                        children=[
                            Overlay(
                                children=self.memory_circular_progress_bar,
                                overlays=[self.memory_icon],
                            )
                        ]
                    ),

                    Box(
                        h_expand=True,
                        h_align="center",
                        children=[
                            Overlay(
                                children=self.cpu_circular_progress_bar,
                                overlays=[self.cpu_icon],
                            )
                        ]
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
            self.disk_circular_progress_bar.percentage = psutil.disk_usage("/").percent
            self.temp_circular_progress_bar.percentage = psutil.sensors_temperatures()["k10temp"][0].current
