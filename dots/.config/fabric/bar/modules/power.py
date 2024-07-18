from __init__ import *

class Power(EventBox):
    def __init__(self):
        super().__init__(name="power-event")

        icons_map = {
            "power-lock": icons.lock,
            "power-suspend": icons.suspend,
            "power-logout": icons.logout,
            "power-reboot": icons.reboot,
            "power-shutdown": icons.shutdown
        }

        self.buttons = {name: Button(name=name, child=Label(label=f"{icon}", markup=True))
                        for name, icon in icons_map.items()}

        self.power_box = Box(
            name="power-box",
            orientation="v",
            children=[self.buttons[name] for name in ["power-lock", "power-suspend", "power-logout", "power-reboot"]]
        )

        self.accept_button = Button(
            name="accept",
            child=Label(label=f"{icons.accept}", markup=True)
        )
        self.cancel_button = Button(
            name="cancel",
            child=Label(label=f"{icons.cancel}", markup=True)
        )

        self.revealer_buttons_box = Box(
            name="confirm-box",
            orientation="v",
            children=[self.accept_button, self.cancel_button]
        )

        self.revealer = Revealer(
            name="power-revealer",
            transition_type="slide-up",
            transition_duration=300,
            child=self.power_box,
            reveal_child=False
        )

        self.super_box = Box(
            name="super-box",
            orientation="v",
            children=[self.revealer, self.buttons["power-shutdown"]]
        )

        self.super_revealer = Revealer(
            name="super-revealer",
            transition_type="slide-up",
            transition_duration=300,
            child=self.super_box,
            reveal_child=True
        )

        self.confirm_revealer = Revealer(
            name="confirm-revealer",
            transition_type="slide-up",
            transition_duration=300,
            child=self.revealer_buttons_box,
            reveal_child=False
        )

        self.full_power = Box(
            name="full-power",
            orientation="v",
            children=[self.super_revealer, self.confirm_revealer]
        )

        self.add(self.full_power)
        self.buttons["self"] = self

        for btn in self.buttons.values():
            bulk_connect(
                btn,
                {
                    "button-press-event": self.on_button_press,
                    "enter-notify-event": self.on_button_hover,
                    "leave-notify-event": self.on_button_unhover,
                },
            )

        self.current_command = None

        self.accept_button.connect("button-press-event", self.on_accept_press)
        self.cancel_button.connect("button-press-event", self.on_cancel_press)

    def on_button_hover(self, button, event):
        if button == self:
            self.revealer.set_reveal_child(True)
        return self.change_cursor("pointer")

    def on_button_unhover(self, button, event):
        if button == self:
            self.revealer.set_reveal_child(False)
        return self.change_cursor("default")

    def on_button_press(self, button, event):
        commands = {
            self.buttons["power-lock"]: "swaylock",
            self.buttons["power-suspend"]: "hyprctl dispatch exec swaylock && systemctl suspend",
            self.buttons["power-logout"]: "hyprctl dispatch exit",
            self.buttons["power-reboot"]: "systemctl reboot",
            self.buttons["power-shutdown"]: "systemctl poweroff"
        }

        if button in commands:
            if button != self.buttons["power-lock"]:
                self.current_command = commands[button]
                self.super_revealer.set_reveal_child(False)
                self.confirm_revealer.set_reveal_child(True)
            else:
                exec_shell_command_async(commands[button], lambda *_: None)

        return True

    def on_accept_press(self, button, event):
        if self.current_command:
            exec_shell_command_async(self.current_command, lambda *_: None)
            self.current_command = None
            self.confirm_revealer.set_reveal_child(False)
            self.super_revealer.set_reveal_child(True)

        return True

    def on_cancel_press(self, button, event):
        self.current_command = None
        self.confirm_revealer.set_reveal_child(False)
        self.super_revealer.set_reveal_child(True)

        return True
