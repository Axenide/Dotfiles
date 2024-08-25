from __init__ import *

class Circles(Box):
    def __init__(self):
        super().__init__(visible=False, all_visible=False)

        self.cpu_circular_progress_bar = self.create_circular_progress_bar("cpu-circular-progress-bar")
        self.memory_circular_progress_bar = self.create_circular_progress_bar("memory-circular-progress-bar")
        self.battery_circular_progress_bar = self.create_circular_progress_bar("battery-circular-progress-bar", 100)
        self.disk_circular_progress_bar = self.create_circular_progress_bar("disk-circular-progress-bar")
        self.temp_circular_progress_bar = self.create_circular_progress_bar("temp-circular-progress-bar")

        self.temp_icon = self.create_icon_label("temp-icon", icons.temp)
        self.disk_icon = self.create_icon_label("disk-icon", icons.disk)
        self.battery_icon = self.create_icon_label("battery-icon", icons.battery)
        self.memory_icon = self.create_icon_label("memory-icon", icons.memory)
        self.cpu_icon = self.create_icon_label("cpu-icon", icons.cpu)

        GLib.Thread.new(None, self.update_status)

        self.add(Box(
            name="circles-container",
            h_expand=True,
            h_align="fill",
            orientation="h",
            children=[
                self.create_circular_box(self.temp_circular_progress_bar, self.temp_icon),
                self.create_circular_box(self.disk_circular_progress_bar, self.disk_icon),
                self.create_circular_box(self.battery_circular_progress_bar, self.battery_icon),
                self.create_circular_box(self.memory_circular_progress_bar, self.memory_icon),
                self.create_circular_box(self.cpu_circular_progress_bar, self.cpu_icon),
            ],
        ))
        self.show_all()

    def create_circular_progress_bar(self, name, percentage=0):
        return CircularProgressBar(
            size=(42, 42),
            line_style="round",
            percentage=percentage,
            name=name,
        )

    def create_icon_label(self, name, icon):
        return Label(name=name, label=icon, markup=True)

    def create_circular_box(self, progress_bar, icon):
        return Box(
            h_expand=True,
            h_align="center",
            children=[
                Overlay(
                    children=progress_bar,
                    overlays=[icon],
                )
            ]
        )

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
