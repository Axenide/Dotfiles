from __init__ import *

class Bar(Window):
    def __init__(self):
        super().__init__(
            layer="top",
            anchor="left top bottom",
            margin="0px -10px 0px 0px",
            visible=False,
            all_visible=False,
            exclusive=True,
            keyboard_mode="none",
        )

        self.system_tray = SystemTray(name="system-tray", orientation="v", spacing=8, icon_size=18)

        self.time_sep = Label(
            label="",
            name="time-separator",
        )

        self.content_box = Revealer(
            transition_duration=500,
            transition_type="slide-right",
        )

        self.dashboard_box = Revealer(
            transition_duration=500,
            transition_type="slide-left",
        )

        self.center_box = CenterBox(name="bar", orientation="v")

        self.run_button = Button(
            name="run-button",
            tooltip_text="Show Applications Menu",
            child=Image(
                name="run-button-image",
                image_file=get_relative_path("../assets/applications.svg"),
            ),
        )

        self.power = Power()

        self.colorpicker = Button(
            name="colorpicker",
            tooltip_text="Color Picker",
            child=Image(
                name="colorpicker-image",
                image_file=get_relative_path("../assets/colorpicker.svg")
            ),
        )
        self.media_button = Button(
            name="media-button",
            tooltip_text=str(exec_shell_command('playerctl metadata artist -f "{{ artist }} - {{ title }}"')).rstrip(),
            child=Image(
                name="media-button-image",
                image_file=get_relative_path("../assets/media.svg")
            )
        )
        self.time_button = Button(
            name="time-button",
            child=DateTime(['%H\n%M']),
        )

        self.buttons = [
            self.run_button,
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
                    self.run_button,
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
        
        self.content_box.add(
            Box(
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
        )

        self.full_box = Box(
            name="full-box",
            orientation="h",
            children=[
                self.content_box,
                self.center_box,
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
        if command == "chat":
            if self.stack.get_visible_child() != self.stack.chat or self.content_box.get_reveal_child() == False:
                self.set_keyboard_mode("on-demand")
                self.stack.set_visible_child(self.stack.chat)
                self.content_box.set_reveal_child(True)
            else:
                self.set_keyboard_mode("none")
                self.content_box.set_reveal_child(False)

        elif command == "dashboard":
            if self.stack.get_visible_child() != self.stack.dashboard or self.content_box.get_reveal_child() == False:
                self.set_keyboard_mode("none")
                self.stack.set_visible_child(self.stack.dashboard)
                self.content_box.set_reveal_child(True)
            else:
                self.content_box.set_reveal_child(False)

        elif command == "wallpapers":
            if self.stack.get_visible_child() != self.stack.wallpapers or self.content_box.get_reveal_child() == False:
                self.set_keyboard_mode("none")
                self.stack.set_visible_child(self.stack.wallpapers)
                self.content_box.set_reveal_child(True)
            else:
                self.content_box.set_reveal_child(False)

        return False

    def on_button_press(self, button: Button, event):
        if button == self.run_button:
            commands = {
                1: f'{home_dir}/.config/rofi/launcher/launcher.sh',
                2: 'swaync-client -t -sw',
                3: 'toggle'
            }
            command = commands.get(event.button)
            if command != 'toggle':
                return exec_shell_command(command)
            else:
                self.content_box.set_reveal_child(not self.content_box.get_reveal_child())
                self.dashboard_box.set_reveal_child(not self.dashboard_box.get_reveal_child())

                if self.content_box.get_reveal_child() == False:
                    self.dashboard_box.set_reveal_child(False)
                    self.chat_box.set_reveal_child(False)
                    self.set_keyboard_mode("none")
        
        elif button == self.colorpicker:
            commands = {
                1: get_relative_path('../scripts/hyprpicker-hex.sh'),
                3: get_relative_path('../scripts/hyprpicker-rgb.sh'),
            }
            command = commands.get(event.button)
            if command:
                return exec_shell_command_async(command, lambda *args: None)
        
        elif button == self.media_button:
            commands = {
                1: 'playerctl previous',
                2: 'playerctl play-pause',
                3: 'playerctl next',
            }
            command = commands.get(event.button)
            if command:
                return exec_shell_command(command)

        elif button == self.time_button:
            commands = {
                1: f'{home_dir}/.config/rofi/calendar/calendar.sh',
            }
            command = commands.get(event.button)
            if command:
                return exec_shell_command(command)

    def on_button_hover(self, button: Button, event):
        return self.change_cursor("pointer")

    def on_button_unhover(self, button: Button, event):
        return self.change_cursor("default")
