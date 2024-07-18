from __init__ import *

class MasterWithButton(EventBox):
    def __init__(self, master_name, master_icon, master_button_name, children, position="top", on_reveal=None, unhover_close=False):
        super().__init__(name=f"{master_name}-event")

        self.revealer_open = False
        self.on_reveal = on_reveal
        self.unhover_close = unhover_close

        self.master_button = Button(
            name=f"{master_name}-{master_button_name}",
            child=Label(label=f"{master_icon}", markup=True),
        )

        self.children_box = Box(
            name=f"{master_name}-box",
            orientation="v",
            children=children,
        )

        self.revealer = Revealer(
            name=f"{master_name}-revealer",
            transition_type="slide-down" if position == "top" else "slide-up",
            transition_duration=300,
            child=self.children_box,
        )

        self.full_container = Box(
            name=f"{master_name}-container",
            orientation="v",
            children=[self.master_button, self.revealer] if position == "top" else [self.revealer, self.master_button],
        )

        self.add(self.full_container)

        bulk_connect(
            self.master_button,
            {
                "button-press-event": self.on_button_press,
            },
        )

        for child in children:
            bulk_connect(
                child,
                {
                    "button-press-event": self.on_button_press,
                },
            )

        bulk_connect(
            self,
            {
                "leave-notify-event": self.on_eventbox_unhover,
            },
        )

    def on_button_press(self, button: Button, event):
        if button == self.master_button:
            self.revealer_open = not self.revealer_open
            self.revealer.set_reveal_child(self.revealer_open)
            if self.revealer_open and self.on_reveal:
                self.on_reveal()
        else:
            commands = self.get_commands()
            command = commands.get(button)
            if command:
                exec_shell_command_async(command, lambda *_: None)
            if button.get_name().endswith("cancel"):  # Check if the button is a "cancel" button
                self.revealer_open = False
                self.revealer.set_reveal_child(self.revealer_open)
        return True

    def get_commands(self):
        return {
            self.master_button: "master_command",
            # Agregar comandos específicos para cada hijo
        }

    def on_eventbox_unhover(self, widget, event):
        if self.revealer_open and self.unhover_close:
            self.revealer_open = False
            self.revealer.set_reveal_child(self.revealer_open)


class MasterWithHover(EventBox):
    def __init__(self, master_name, master, children, position="top"):
        super().__init__(name=f"{master_name}-event")

        self.revealer_open = False

        self.master = master

        self.children_box = Box(
            name=f"{master_name}-box",
            orientation="v",
            children=children,
        )

        self.revealer = Revealer(
            name=f"{master_name}-revealer",
            transition_type="slide-down" if position == "top" else "slide-up",
            transition_duration=300,
            child=self.children_box,
        )

        self.full_container = Box(
            name=f"{master_name}-container",
            orientation="v",
            children=[self.master, self.revealer] if position == "top" else [self.revealer, self.master],
        )

        self.add(self.full_container)

        bulk_connect(
            self,
            {
                "enter-notify-event": self.on_eventbox_hover,
                "leave-notify-event": self.on_eventbox_unhover,
            },
        )

        bulk_connect(
            self.master,
            {
                "button-press-event": self.on_master_button_press,
            },
        )

        for child in children:
            bulk_connect(
                child,
                {
                    "button-press-event": self.on_button_press,
                },
            )

    def on_eventbox_hover(self, widget, event):
        self.revealer.set_reveal_child(True)
        return self.change_cursor("pointer")

    def on_eventbox_unhover(self, widget, event):
        self.revealer.set_reveal_child(False)
        return self.change_cursor("default")

    def on_master_button_press(self, button: Button, event):
        return self.on_button_press(button, event)

    def on_button_press(self, button: Button, event):
        commands = self.get_commands(event.button)
        command = commands.get(button)
        if command:
            exec_shell_command_async(command, lambda *_: None)
        return True

    def get_commands(self, event_button):
        return {
            # Agregar comandos específicos para cada hijo
        }
