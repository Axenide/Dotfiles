from __init__ import *

def create_common_buttons():
    return [
        Button(name="accept", child=Label(label=icons.accept, markup=True)),
        Button(name="cancel", child=Label(label=icons.cancel, markup=True)),
    ]

class PowerAction(MasterWithButton):
    def __init__(self, name, icon, command):
        super().__init__(name, icon, "confirm", create_common_buttons(), position="top", unhover_close=True)
        self.command = command

    def get_commands(self):
        children = self.children_box.get_children()
        return {
            children[0]: self.command,
            children[1]: "",
        }

class Power(MasterWithHover):
    def __init__(self):
        master_shutdown = PowerAction("shutdown", icons.shutdown, "systemctl poweroff")
        children = [
            Button(name="power-lock", child=Label(label=icons.lock, markup=True)),
            PowerAction("suspend", icons.suspend, "systemctl suspend"),
            PowerAction("logout", icons.logout, "hyprctl dispatch exit"),
            PowerAction("reboot", icons.reboot, "systemctl reboot"),
        ]
        super().__init__("power", master_shutdown, children, position="bottom")

    def close_self(self):
        self.revealer.set_reveal_child(False)

    def get_commands(self):
        children = self.children_box.get_children()
        return {
            children[0]: "swaylock",
        }
