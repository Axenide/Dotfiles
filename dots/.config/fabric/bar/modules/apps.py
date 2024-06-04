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
                    justfication="left",
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

    # TODO look into how ags does this
    def launch_app(self):
        cmd = [x for x in self.app.command_line.split(" ") if x[0] != "%"]
        print(cmd)
        subprocess.Popen(
            cmd,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.STDOUT,
            start_new_session=True,
        )

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
            name="app-entry",
            placeholder_text="Search...",
            editable=True,
        )
        self.app_entry.connect("key-release-event", self.keypress)
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
        self.reset_app_menu()
        self.parent.content_box.set_reveal_child(False)

    def keypress(self, entry: Entry, event_key):
        if event_key.get_keycode()[1] == 9:
            self.toggle_popup()
        if entry.get_text() == " " or entry.get_text() == "":
            self.reset_app_menu()
            return
        lister = process.extract(
            entry.get_text(),
            self.app_names,
            scorer=fuzz.partial_ratio,
            limit=10,
        )
        for elem_i in range(len(lister)):
            name = lister[elem_i][0]
            self.buttons_box.reorder_child(self.application_buttons[name], elem_i)

    def reset_app_menu(self):
        i = 0
        for app_button in self.application_buttons.values():
            self.buttons_box.reorder_child(app_button, i)
            i += 1
