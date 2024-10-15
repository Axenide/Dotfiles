from __init__ import *

class Bar(Window):
    def __init__(self):
        super().__init__(
            layer="bottom",
            anchor="left top bottom",
            margin="0px -20px 0px 0px",
            visible=False,
            all_visible=False,
            exclusive=True,
            keyboard_mode="none",
        )

        self.panels = Panels()

        self.system_tray = SystemTray()
        # self.system_tray = SystemTray(name="system-tray", icon_size=20, orientation="v", spacing=10)

        self.content_box = Revealer(
            transition_duration=500,
            transition_type="slide-right",
        )

        self.dashboard_box = Revealer(
            transition_duration=500,
            transition_type="slide-left",
        )

        self.center_box = CenterBox(name="bar", orientation="v")

        self.power = Power()

        self.colorpicker = Button(
            name="colorpicker",
            child=Label(label=f"{icons.colorpicker}", markup=True),
        )
        self.media_button = Button(
            name="media-button",
            child=Label(label=f"{icons.media}", markup=True),
        )
        self.time_button = Button(
            name="time-button",
            child=DateTime(['%H\n%M']),
        )

        self.buttons = [
            self.colorpicker,
            self.media_button,
            self.time_button,
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

        self.center_box.add_start(
            Box(
                orientation="v",
                spacing=4,
                children=[
                    self.panels,
                    Box(name="module-separator"),
                    self.system_tray,
                    Box(name="module-separator"),
                    self.media_button,
                ],
            )
        )

        self.center_box.add_center(WorkspacesBox())

        self.center_box.add_end(
            Box(
                orientation="v",
                spacing=4,
                children=[
                    self.colorpicker,
                    Box(name="module-separator"),
                    self.time_button,
                    Box(name="module-separator"),
                    self.power,
                ],
            )
        )
        
        self.user = User()
        self.stack = MainStack()
        self.stack.chat.buttons.parent = self

        self.stack.apps.parent = self

        self.content_box_child = Box(
            name="content-box",
            spacing=4,
            orientation="v",
            h_expand=True,
            v_expand=True,
            children=[
                self.user,
                self.stack,
            ]
        )
        
        self.content_box.add(
            self.content_box_child
        )

        self.corners = CenterBox(
            name="corners",
            orientation="v",
            v_expand=True,
        )

        self.corner_top = Corner(name="corner", orientation="top-left", size=20)
        
        self.corner_bottom = Corner(name="corner", orientation="bottom-left", size=20)

        self.corners.add_start(self.corner_top)
        self.corners.add_end(self.corner_bottom)

        self.full_box = Box(
            name="full-box",
            orientation="h",
            children=[
                self.content_box,
                self.center_box,
                self.corners,
            ],
        )

        self.add(self.full_box)
        self.show_all()

        GLib.Thread.new(None, self.commands)

    def commands(self):
        while True:
            command = listen()
            GLib.idle_add(self.binds, command)

    def binds(self, command):
        child_mapping = {
            "chat": (self.stack.chat, "on-demand"),
            "dashboard": (self.stack.dashboard, "none"),
            "wallpapers": (self.stack.wallpapers, "exclusive"),
            "apps": (self.stack.apps, "exclusive")
        }

        if command in child_mapping:
            new_child, kb_mode = child_mapping[command]
            if not self.content_box.get_reveal_child() or self.stack.get_visible_child() != new_child:
                self.set_keyboard_mode(kb_mode)
                self.stack.set_visible_child(new_child)
                self.content_box.set_reveal_child(True)
            else:
                self.content_box.set_reveal_child(False)
            if command == "apps":
                self.stack.apps.app_entry.grab_focus()
            if command == "wallpapers":
                self.stack.wallpapers.wallpaper_entry.grab_focus()
        elif command == "update-style":
            set_stylesheet_from_file(get_relative_path("../style.css"))

        if not self.content_box.get_reveal_child():
            self.set_keyboard_mode("none")

        return False

    def on_button_press(self, button: Button, event):
        match button:
            case self.colorpicker:
                commands = {
                    1: get_relative_path('./scripts/hyprpicker-hex.sh'),
                    3: get_relative_path('./scripts/hyprpicker-rgb.sh'),
                }
                command = commands.get(event.button)
                if command:
                    return exec_shell_command_async(command, lambda *args: None)
            
            case self.media_button:
                commands = {
                    1: 'playerctl previous',
                    2: 'playerctl play-pause',
                    3: 'playerctl next',
                }
                command = commands.get(event.button)
                if command:
                    return exec_shell_command_async(command, lambda *args: None)

            case self.time_button:
                commands = {
                    1: f'{home_dir}/.config/rofi/calendar/calendar.sh',
                }
                command = commands.get(event.button)
                if command:
                    return exec_shell_command_async(command, lambda *args: None)

    def on_button_hover(self, button: Button, event):
        return self.change_cursor("pointer")

    def on_button_unhover(self, button: Button, event):
        return self.change_cursor("default")
