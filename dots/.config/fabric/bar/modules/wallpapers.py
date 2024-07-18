from __init__ import *

WALLPAPERS_PATH = f"{os.getenv('XDG_PICTURES_DIR')}/Wallpapers"

class WallpaperButton(Button):
    def __init__(self, wallpaper: str, **kwargs):
        self.wallpaper = wallpaper
        self.wallpaper_box = Box(
            name=f"{wallpaper}",
            style=f"""
            background-image: url("{WALLPAPERS_PATH}/.thumbnails/{wallpaper}");
            background-size: cover;
            background-position: center;
            """,
        )

        super().__init__(name="wallpaper-button", **kwargs)
        self.add(self.wallpaper_box)
        self.connect("button-press-event", self.on_button_press)
        self.connect("key-press-event", self.on_key_press)  # Conectar evento de tecla

    def on_button_press(self, button, event):
        img = f"{WALLPAPERS_PATH}/{self.wallpaper}"

        commands = {
            1: f"wal -i {img}",
            2: f"echo 'Not using Pywal'",
            3: f"wal -i {img} --backend colorthief",
        }

        if event.button in commands:
            exec_shell_command(commands[event.button])

        ln_command = f"ln -sf {img} {home_dir}/.current.wall"

        # Asegúrate de que `self.parent` esté correctamente configurado
        if hasattr(self, 'parent') and hasattr(self.parent, 'dashboard') and hasattr(self.parent.dashboard, 'player') and hasattr(self.parent.dashboard.player, 'cover'):
            self.parent.dashboard.player.cover.set_style(f"background-image: url('{img}');")

        wal_script_command = f"python {home_dir}/.config/wal/set.py"

        for command in [ln_command, wal_script_command]:
            exec_shell_command_async(command, lambda *args: None)

        return True

    def on_key_press(self, widget, event):
        if event.keyval == Gdk.KEY_Return and not (event.state & Gdk.ModifierType.SHIFT_MASK):  # Enter key
            self.trigger_command(1)
        elif event.keyval == Gdk.KEY_space:  # Space key
            self.trigger_command(2)
        elif event.keyval == Gdk.KEY_Return and (event.state & Gdk.ModifierType.SHIFT_MASK):  # Shift + Enter
            self.trigger_command(3)

    def trigger_command(self, command_type):
        img = f"{WALLPAPERS_PATH}/{self.wallpaper}"

        commands = {
            1: f"wal -i {img}",
            2: f"echo 'Not using Pywal'",
            3: f"wal -i {img} --backend colorthief",
        }

        if command_type in commands:
            exec_shell_command(commands[command_type])

        ln_command = f"ln -sf {img} {home_dir}/.current.wall"

        # Asegúrate de que `self.parent` esté correctamente configurado
        if hasattr(self, 'parent') and hasattr(self.parent, 'dashboard') and hasattr(self.parent.dashboard, 'player') and hasattr(self.parent.dashboard.player, 'cover'):
            self.parent.dashboard.player.cover.set_style(f"background-image: url('{img}');")

        wal_script_command = f"python {home_dir}/.config/wal/set.py"

        for command in [ln_command, wal_script_command]:
            exec_shell_command_async(command, lambda *args: None)

class Wallpapers(Box):
    def __init__(self, parent, **kwargs):
        self.parent = parent
        self.scrolled_window = ScrolledWindow(
            name="wallpaper-scroll",
            h_expand=True,
            v_expand=True,
        )

        self.wallpapers = sorted(
            [wall for wall in os.listdir(WALLPAPERS_PATH) if wall.endswith((".png", ".jpg", ".jpeg", ".webp", ".gif"))]
        )
        self.wallpaper_buttons = {}
        self.buttons_box = Box(orientation="v", spacing=4)
        self.wallpaper_entry = Entry(
            name="search-entry",
            placeholder_text="Search wallpapers...",
            editable=True,
        )
        self.wallpaper_entry.connect("key-release-event", self.keypress)
        self.wallpaper_entry.connect("activate", self.on_enter_press)  # Conectamos el evento de Enter

        for wallpaper in self.wallpapers:
            wall_btn = WallpaperButton(wallpaper)
            self.wallpaper_buttons[wallpaper] = wall_btn
            wall_btn.connect("button-press-event", self.on_button_press)
            self.buttons_box.add(wall_btn)

        self.wallpaper_names = self.wallpaper_buttons.keys()
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
                name="wallpapers",
                orientation="v",
                h_expand=True,
                spacing=4,
                children=[self.wallpaper_entry, self.scrolled_window],
            ),
        )

        self.selected_index = -1  # Índice seleccionado para la navegación del teclado

    def keypress(self, entry: Entry, event_key):
        key_code = event_key.get_keycode()[1]
        if key_code == 9:  # Escape key
            self.toggle_popup()
        elif key_code == 38:  # Up arrow key
            self.navigate_up()
        elif key_code == 40:  # Down arrow key
            self.navigate_down()
        elif key_code == 36 and not (event_key.state & Gdk.ModifierType.SHIFT_MASK):  # Enter key
            self.execute_command(1)
        elif key_code == 65:  # Space key
            self.execute_command(2)
        elif key_code == 36 and (event_key.state & Gdk.ModifierType.SHIFT_MASK):  # Shift + Enter
            self.execute_command(3)
        else:
            search_text = entry.get_text().lower()
            if search_text.strip() == "":
                self.reset_wallpaper_menu()
                return
            for name, wall_button in self.wallpaper_buttons.items():
                if search_text in name.lower():
                    wall_button.show()
                else:
                    wall_button.hide()

    def toggle_popup(self):
        self.wallpaper_entry.set_text("")
        self.wallpaper_entry.grab_remove()
        self.parent.set_keyboard_mode("none")
        self.reset_wallpaper_menu()
        self.parent.content_box.set_reveal_child(False)

    def reset_wallpaper_menu(self):
        for wall_button in self.wallpaper_buttons.values():
            wall_button.show()

    def navigate_up(self):
        if self.selected_index > 0:
            self.selected_index -= 1
            self.highlight_selected()

    def navigate_down(self):
        if self.selected_index < len(self.wallpaper_buttons) - 1:
            self.selected_index += 1
            self.highlight_selected()

    def highlight_selected(self):
        for index, button in enumerate(self.wallpaper_buttons.values()):
            if index == self.selected_index:
                button.set_style("border: 2px solid blue;")
                button.grab_focus()  # Asignar el foco al botón seleccionado
            else:
                button.set_style("border: none;")

    def execute_command(self, command_type):
        if self.selected_index >= 0 and self.selected_index < len(self.wallpaper_buttons):
            button = list(self.wallpaper_buttons.values())[self.selected_index]
            event = Gdk.EventButton()
            event.button = command_type
            self.on_button_press(button, event)

    def on_enter_press(self, entry: Entry):
        self.execute_command(1)

    def on_button_press(self, button: Button, event):
        img = f"{WALLPAPERS_PATH}/{button.get_child().get_name()}"

        commands = {
            1: f"wal -i {img}",
            2: f"echo 'Not using Pywal'",
            3: f"wal -i {img} --backend colorthief",
        }

        if event.button in commands:
            exec_shell_command(commands[event.button])

        ln_command = f"ln -sf {img} {home_dir}/.current.wall"

        self.parent.dashboard.player.cover.set_style(f"background-image: url('{img}');")

        wal_script_command = f"python {home_dir}/.config/wal/set.py"

        for command in [ln_command, wal_script_command]:
            exec_shell_command_async(command, lambda *args: None)

        return True
