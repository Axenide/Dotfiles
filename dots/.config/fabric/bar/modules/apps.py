from __init__ import *

class AppButton(Button):
    def __init__(self, app: Application, **kwargs):
        self.app: Application = app
        self.app_icon = (
            Image(pixbuf=self.app.get_icon_pixbuf())
            if self.app.get_icon_pixbuf()
            else Image(icon_name="application-x-executable", pixel_size=24, icon_size=1)
        )
        self.actions_list = self.app._app.list_actions()
        self.app_name = Box(
            children=[
                Label(
                    label=self.app.display_name,
                    justification="left",
                    ellipsization="end",
                ),
            ],
        )
        self.button_box = Box(
            spacing=4,
            children=[
                # self.app_icon,
                self.app_name,
            ],
        )

        self.parent = self

        super().__init__(name="app-button", **kwargs)
        self.connect("clicked", lambda _: self.launch_app())
        self.add(self.button_box)

    def rm_percent(self, command):
        pattern = r'\s?%\w'
        cleaned_command = re.sub(pattern, '', command)
        return cleaned_command

    def launch_app(self):
        exec_shell_command_async(
            f"hyprctl dispatch exec '{self.rm_percent(self.app.command_line)}'",
            lambda *_: logger.info(f"Launched {self.app.name}"),
        ) if self.app.command_line else None

class Apps(Box):
    def __init__(self, **kwargs):
        self.scrolled_window = ScrolledWindow(
            name="app-scroll",
            h_expand=True,
            v_expand=True,
        )
        self.applications = sorted(
            get_desktop_applications(),
            key=lambda x: x.name.lower(),
        )
        self.application_buttons = {}
        self.buttons_box = Box(orientation="v", spacing=4)
        self.app_entry = Entry(
            name="search-entry",
            placeholder_text="Search applications...",
            editable=True,
        )
        self.app_entry.props.xalign = 0.5
        self.app_entry.connect("key-release-event", self.keypress)
        self.app_entry.connect("activate", self.on_enter_press)  # Aquí conectamos el evento de Enter
        for app in self.applications:
            appL = AppButton(app)
            self.application_buttons[app.name] = appL
            appL.connect("clicked", lambda *args: self.toggle_popup())
            self.buttons_box.add(appL)
        self.app_names = self.application_buttons.keys()
        self.searched_buttons_box = Box(orientation="v", visible=False)
        self.scrolled_window.add_children(
            Box(
                orientation="v",
                children=[
                    self.buttons_box,
                    self.searched_buttons_box,
                ],
            ),
        )
        super().__init__(
            child=Box(
                name="apps",
                orientation="v",
                h_expand=True,
                spacing=4,
                children=[self.app_entry, self.scrolled_window],
            ),
        )

    def toggle_popup(self):
        self.app_entry.set_text("")
        self.app_entry.grab_remove()
        self.parent.set_keyboard_mode("none")
        self.reset_app_menu()
        self.parent.content_box.set_reveal_child(False)

    def keypress(self, entry: Entry, event_key):
        if event_key.get_keycode()[1] == 9:
            self.toggle_popup()
        search_text = entry.get_text().lower()
        if search_text.strip() == "":
            self.reset_app_menu()
            return
        for name, app_button in self.application_buttons.items():
            if search_text in name.lower():
                app_button.show()
            else:
                app_button.hide()

    def reset_app_menu(self):
        for app_button in self.application_buttons.values():
            app_button.show()

    def on_enter_press(self, entry: Entry):
        for app_button in self.application_buttons.values():
            if app_button.get_visible() and self.app_entry.get_text() != "":
                app_button.emit("clicked")
                break
