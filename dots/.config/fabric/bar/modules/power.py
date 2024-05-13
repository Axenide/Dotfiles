from __init__ import *

class Power(EventBox):
    def __init__(self):
        super().__init__(
            name="power-event",
            # orientation="v",
        )
        self.lock = Button(
            name="lock",
            icon_image=Image(image_file=get_relative_path("../assets/lock.svg"))
        )

        self.suspend = Button(
            name="suspend",
            icon_image=Image(image_file=get_relative_path("../assets/suspend.svg"))
        )

        self.logout = Button(
            name="logout",
            icon_image=Image(image_file=get_relative_path("../assets/logout.svg"))
        )

        self.reboot = Button(
            name="reboot",
            icon_image=Image(image_file=get_relative_path("../assets/reboot.svg"))
        )

        self.shutdown = Button(
            name="shutdown",
            icon_image=Image(image_file=get_relative_path("../assets/shutdown.svg"))
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
                # self.shutdown,
            ]
        )

        self.revealer = Revealer(
            name="power-revealer",
            transition_type="slide-up",
            transition_duration=500,
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

        for btn in [self.lock, self.suspend, self.logout, self.reboot, self.shutdown, self]:
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
            self.set_name("power-event-hover")
            print("hovering")
            print(self.name)
        return self.change_cursor("pointer")

    def on_button_unhover(self, button: Button, event):
        if button == self:
            self.revealer.set_reveal_child(False)
            self.set_name("power-event")
            print("unhovering")
            print(self.name)
        return self.change_cursor("default")

    def on_button_press(self, button: Button, event):
        if button == self.lock:
            exec_shell_command("swaylock")
            # exec_shell_command("notify-send 'Locking screen'")
        elif button == self.suspend:
            # exec_shell_command("systemctl suspend")
            exec_shell_command("notify-send 'Suspending system'")
        elif button == self.logout:
            # exec_shell_command("hyprctl dispatch exit")
            exec_shell_command("notify-send 'Logging out'")
        elif button == self.reboot:
            # exec_shell_command("systemctl reboot")
            exec_shell_command("notify-send 'Rebooting system'")
        elif button == self.shutdown:
            # exec_shell_command("systemctl poweroff")
            exec_shell_command("notify-send 'Shutting down system'")
        return True
