from __init__ import *

class Panels(MasterWithHover):
    def __init__(self):
        master = Button(name="common-button-1", child=Label(label=icons.apps, markup=True))
        children = [
            Button(name="common-button-1", child=Label(label=icons.dashboard, markup=True)),
            Button(name="common-button-1", child=Label(label=icons.chat, markup=True)),
            Button(name="common-button-1", child=Label(label=icons.wallpapers, markup=True)),
            Button(name="common-button-1", child=Label(label=icons.windows, markup=True)),
        ]
        super().__init__("panels", master, children, position="top")

    def get_commands(self, event_button):
        children = self.children_box.get_children()
        commands = {
            1: {
                self.master: f"{fabricSend} apps",
                children[0]: f"{fabricSend} dashboard",
                children[1]: f"{fabricSend} chat",
                children[2]: f"{fabricSend} wallpapers",
                children[3]: f"swaync-client -t",
            },
            2: {
                self.master: f"{fabricSend} apps",
                children[0]: f"{fabricSend} dashboard",
                children[1]: f"{fabricSend} chat",
                children[2]: f"{fabricSend} wallpapers",
                children[3]: f"swaync-client -t",
            },
            3: {
                self.master: f"{fabricSend} apps",
                children[0]: f"{fabricSend} dashboard",
                children[1]: f"{fabricSend} chat",
                children[2]: f"{fabricSend} wallpapers",
                children[3]: f"swaync-client -t",
            }
        }
        return commands.get(event_button, {})
