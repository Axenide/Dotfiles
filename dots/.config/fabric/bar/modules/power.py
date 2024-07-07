from __init__ import *

class Power(EventBox):
    def __init__(self):
        super().__init__(
            name="power-event",
            # orientation="v",
        )
        self.lock = Button(
            name="lock",
            child=Label(label=f"{icons.lock}", markup=True),
        )

        self.suspend = Button(
            name="suspend",
            child=Label(label=f"{icons.suspend}", markup=True),
        )

        self.logout = Button(
            name="logout",
            child=Label(label=f"{icons.logout}", markup=True),
        )

        self.reboot = Button(
            name="reboot",
            child=Label(label=f"{icons.reboot}", markup=True),
        )

        self.shutdown = Button(
            name="shutdown",
            child=Label(label=f"{icons.shutdown}", markup=True),
        )

        self.power_box = Box(
            name="power-box",
            orientation="v",
            # spacing=16,
            children=[
                self.lock,
                self.suspend,
                self.logout,
                self.reboot,
            ]
        )

        self.revealer = Revealer(
            name="power-revealer",
            transition_type="slide-up",
            transition_duration=300,
            child=self.power_box
        )

        self.full_power = Box(
            name="full-power",
            orientation="v",
            children=[
                self.revealer,
                self.shutdown,
            ]
        )

        self.add(self.full_power)

        self.buttons = [
            self.lock,
            self.suspend,
            self.logout,
            self.reboot,
            self.shutdown,
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
            self.lock: "swaylock",
            self.suspend: "notify-send 'Suspending system'",
            self.logout: "notify-send 'Logging out'",
            self.reboot: "notify-send 'Rebooting system'",
            self.shutdown: "notify-send 'Shutting down system'"
        }

        command = commands.get(button)
        if command:
            exec_shell_command_async(command, lambda *_: None)

        return True
