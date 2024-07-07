from __init__ import *

class MasterWithRevealer(EventBox):
    def __init__(self, master_name, master_icon, master_button_name, children, position="top", open_on_hover=True):
        super().__init__(name=f"{master_name}-event")
        
        self.open_on_hover = open_on_hover
        self.revealer_open = False

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

        if self.open_on_hover:
            bulk_connect(
                self,
                {
                    "enter-notify-event": self.on_eventbox_hover,
                    "leave-notify-event": self.on_eventbox_unhover,
                },
            )

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

    def on_eventbox_hover(self, widget, event):
        self.revealer.set_reveal_child(True)
        return self.change_cursor("pointer")

    def on_eventbox_unhover(self, widget, event):
        self.revealer.set_reveal_child(False)
        return self.change_cursor("default")

    def on_button_press(self, button: Button, event):
        if button == self.master_button and not self.open_on_hover:
            self.revealer_open = not self.revealer_open
            self.revealer.set_reveal_child(self.revealer_open)
        else:
            commands = self.get_commands()
            command = commands.get(button)
            if command:
                exec_shell_command_async(command, lambda *_: None)
        return True

    def get_commands(self):
        return {
            self.master_button: "master_command",
            # Agregar comandos específicos para cada hijo
        }

class Power(MasterWithRevealer):
    def __init__(self):
        children = [
            Button(name="power-lock", child=Label(label=icons.lock, markup=True)),
            Button(name="power-suspend", child=Label(label=icons.suspend, markup=True)),
            Button(name="power-logout", child=Label(label=icons.logout, markup=True)),
            Button(name="power-reboot", child=Label(label=icons.reboot, markup=True)),
        ]
        super().__init__("power", icons.shutdown, "shutdown", children, position="bottom", open_on_hover=False)

    def get_commands(self):
        children = self.children_box.get_children()
        return {
            self.master_button: "notify-send 'Shutting down system'",
            children[0]: "swaylock",
            children[1]: "notify-send 'Suspending system'",
            children[2]: "notify-send 'Logging out'",
            children[3]: "notify-send 'Rebooting system'",
        }

class Panels(MasterWithRevealer):
    def __init__(self):
        children = [
            Button(name="panels-dashboard", child=Label(label=icons.dashboard, markup=True)),
            Button(name="panels-chat", child=Label(label=icons.chat, markup=True)),
            Button(name="panels-wallpapers", child=Label(label=icons.wallpapers, markup=True)),
            Button(name="panels-windows", child=Label(label=icons.windows, markup=True)),
        ]
        super().__init__("panels", icons.apps, "apps", children, position="top", open_on_hover=True)

    def get_commands(self):
        children = self.children_box.get_children()
        return {
            self.master_button: f"{fabricSend} apps",
            children[0]: f"{fabricSend} dashboard",
            children[1]: f"{fabricSend} chat",
            children[2]: f"{fabricSend} wallpapers",
            # children[3]: f"{fabricSend} windows",
            children[3]: f"swaync-client -t",
        }
