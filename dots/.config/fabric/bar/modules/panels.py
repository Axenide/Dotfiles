from __init__ import *

class Panels(EventBox):
    def __init__(self):
        super().__init__(
            name="panels-event",
            # orientation="v",
        )
        self.apps = Button(
            name="panels-apps",
            child=Label(label=f"{icons.apps}", markup=True),
        )

        self.dashboard = Button(
            name="panels-dashboard",
            child=Label(label=f"{icons.dashboard}", markup=True),
        )

        self.chat = Button(
            name="panels-chat",
            child=Label(label=f"{icons.chat}", markup=True),
        )

        self.wallpapers = Button(
            name="panels-wallpapers",
            child=Label(label=f"{icons.wallpapers}", markup=True),
        )

        self.windows = Button(
            name="panels-windows",
            child=Label(label=f"{icons.windows}", markup=True),
        )

        self.panels_box = Box(
            name="panels-box",
            orientation="v",
            # spacing=16,
            children=[
                self.dashboard,
                self.chat,
                self.wallpapers,
                self.windows,
            ]
        )

        self.revealer = Revealer(
            name="panels-revealer",
            transition_type="slide-down",
            transition_duration=300,
            child=self.panels_box
        )

        self.full_panels = Box(
            name="full-panels",
            orientation="v",
            children=[
                self.apps,
                self.revealer,
            ]
        )

        self.add(self.full_panels)

        self.buttons = [
            self.apps,
            self.dashboard,
            self.chat,
            self.wallpapers,
            self.windows,
            self,
        ]

        for btn in self.buttons:
            bulk_connect(
                btn,
                {
                    "button-press-event": self.on_button_press,
                    "enter-notify-event": self.on_button_hover,
                    "leave-notify-event": self.on_button_unhover,
                },
            )

    def on_button_hover(self, button: Button, event):
        if button == self:
            self.revealer.set_reveal_child(True)
        return self.change_cursor("pointer")

    def on_button_unhover(self, button: Button, event):
        if button == self:
            self.revealer.set_reveal_child(False)
        return self.change_cursor("default")

    def on_button_press(self, button: Button, event):
        commands = {
            self.apps: f"{fabricSend} apps",
            self.dashboard: f"{fabricSend} dashboard",
            self.chat: f"{fabricSend} chat",
            self.wallpapers: f"{fabricSend} wallpapers",
            self.windows: f"{fabricSend} windows",
        }

        command = commands.get(button)
        if command:
            exec_shell_command_async(command, lambda *_: None)

        return True
