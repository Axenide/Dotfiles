from __init__ import *

WALLPAPERS_PATH = f"{os.getenv('XDG_PICTURES_DIR')}/Wallpapers"

class ReloadWallpapers(Button):
    def __init__(self, parent, **kwargs):
        super().__init__(
            name="common-button",
            child=Label(label=icons.reload, markup=True),
            **kwargs,
        )

        self.parent = parent

        self.connect("button-press-event", self.on_button_press)
        self.connect("key-press-event", self.on_key_press)

    def on_button_press(self, button, event):
        utils.format(WALLPAPERS_PATH)
        utils.thumbs(WALLPAPERS_PATH, 300, 200)
        self.parent.reload_wallpapers_list()

    def on_key_press(self, widget, event):
        key = event.keyval
        if key == Gdk.KEY_Return or key == Gdk.KEY_KP_Enter:
            self.on_button_press(widget, event)
            return True

class ReorderWallpapers(Button):
    def __init__(self, parent, **kwargs):
        super().__init__(
            name="common-button",
            child=Label(label=icons.sort, markup=True),
            **kwargs,
        )

        self.parent = parent
        self.is_alphabetical = True

        self.connect("button-press-event", self.on_button_press)
        self.connect("key-press-event", self.on_key_press)

    def on_button_press(self, button, event):
        self.is_alphabetical = not self.is_alphabetical
        self.parent.reload_wallpapers_list(order="alphabetical" if self.is_alphabetical else "recent")

    def on_key_press(self, widget, event):
        key = event.keyval
        if key == Gdk.KEY_Return or key == Gdk.KEY_KP_Enter:
            self.on_button_press(widget, event)
            return True

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
        self.connect("key-press-event", self.on_key_press)

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

        self.parent.dashboard.player.cover.set_style(f"background-image: url('{img}');")

        wal_script_command = f"hyprctl dispatch exec python {home_dir}/.config/wal/set.py"

        for command in [ln_command, wal_script_command]:
            exec_shell_command_async(command, lambda *args: None)

        return True

    def on_key_press(self, widget, event):
        if event.keyval == Gdk.KEY_Return and not (event.state & Gdk.ModifierType.SHIFT_MASK):
            self.trigger_command(1)
        elif event.keyval == Gdk.KEY_space:
            self.trigger_command(2)
        elif event.keyval == Gdk.KEY_Return and (event.state & Gdk.ModifierType.SHIFT_MASK):
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

        if hasattr(self, 'parent') and hasattr(self.parent, 'dashboard') and hasattr(self.parent.dashboard, 'player') and hasattr(self.parent.dashboard.player, 'cover'):
            self.parent.dashboard.player.cover.set_style(f"background-image: url('{img}');")

        wal_script_command = f"hyprctl dispatch exec python {home_dir}/.config/wal/set.py"

        for command in [ln_command, wal_script_command]:
            exec_shell_command_async(command, lambda *args: None)

class Wallpapers(Box):
    def __init__(self, parent):
        self.parent = parent
        self.scrolled_window = ScrolledWindow(
            name="wallpaper-scroll",
            h_expand=True,
            v_expand=True,
        )

        self.wallpapers = []
        self.wallpaper_buttons = {}
        self.buttons_box = Box(orientation="v", spacing=4)
        self.wallpaper_entry = Entry(
            name="search-entry",
            h_expand=True,
            placeholder_text="Search wallpapers...",
            editable=True,
        )
        self.wallpaper_entry.props.xalign = 0.5
        self.wallpaper_entry.connect("key-release-event", self.keypress)
        self.wallpaper_entry.connect("activate", self.on_enter_press)

        self.reload_wallpapers_list()

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

        self.entry = Box(
            orientation="h",
            spacing=4,
            children=[ReloadWallpapers(self), self.wallpaper_entry, ReorderWallpapers(self)],
        )

        # self.themes = Themes()

        super().__init__(
            child=Box(
                name="wallpapers",
                orientation="v",
                h_expand=True,
                spacing=4,
                children=[self.entry, self.scrolled_window],
            ),
        )

        self.selected_index = -1

    def keypress(self, entry: Entry, event_key):
        key_code = event_key.get_keycode()[1]
        if key_code == 9:
            self.toggle_popup()
        elif key_code == 38:
            self.navigate_up()
        elif key_code == 40:
            self.navigate_down()
        elif key_code == 36 and not (event_key.state & Gdk.ModifierType.SHIFT_MASK):
            self.execute_command(1)
        elif key_code == 65:
            self.execute_command(2)
        elif key_code == 36 and (event_key.state & Gdk.ModifierType.SHIFT_MASK):
            self.execute_command(3)
        else:
            self.filter_wallpapers(entry.get_text().lower())

    def filter_wallpapers(self, search_text):
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
                # button.grab_focus()
                pass

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

        wal_script_command = f"hyprctl dispatch exec python {home_dir}/.config/wal/set.py"

        for command in [ln_command, wal_script_command]:
            exec_shell_command_async(command, lambda *args: None)

        return True

    def reload_wallpapers_list(self, order="alphabetical"):
        self.wallpapers = [wall for wall in os.listdir(WALLPAPERS_PATH) if wall.endswith((".png", ".jpg", ".jpeg", ".webp", ".gif"))]
        
        if order == "alphabetical":
            self.wallpapers.sort()
        else:  # order == "recent"
            self.wallpapers.sort(key=lambda x: os.path.getmtime(os.path.join(WALLPAPERS_PATH, x)), reverse=True)
        
        self.wallpaper_buttons.clear()

        # Eliminar todos los hijos del buttons_box
        for child in self.buttons_box.get_children():
            self.buttons_box.remove(child)

        for wallpaper in self.wallpapers:
            wall_btn = WallpaperButton(wallpaper)
            self.wallpaper_buttons[wallpaper] = wall_btn
            wall_btn.connect("button-press-event", self.on_button_press)
            self.buttons_box.add(wall_btn)

        self.buttons_box.show_all()
        self.filter_wallpapers(self.wallpaper_entry.get_text().lower())
