from __init__ import *

WALLPAPERS_PATH = f"{os.getenv('XDG_PICTURES_DIR')}/Wallpapers"


class Wallpapers(ScrolledWindow):
    def __init__(self, parent):
        super().__init__(
            name="wallpapers",
            h_expand=True,
            v_expand=True,
        )

        self.parent = parent

        self.wallpapers = self.get_wallpapers()

        self.wall_box = Box(
            name="wall-box",
            orientation="v",
            spacing=4,
            h_expand=True,
            children=self.wallpapers,
        )

        self.add(self.wall_box)

    def get_wallpapers(self):
        walls = []
        wall_buttons = []
        for wallpaper in os.listdir(WALLPAPERS_PATH):
            if wallpaper.endswith((".png", ".jpg", ".jpeg", ".webp", ".gif")):
                walls.append(wallpaper)
        
        walls.sort()

        for wall in walls:
            wall_buttons.append(
                Button(
                    name="wall",
                    child=Box(
                        name=f"{wall}",
                        style=f"""
                        background-image: url("{WALLPAPERS_PATH}/.thumbnails/{wall}");
                        background-size: cover;
                        background-position: center;
                        """,
                    )
                )
            )

            for btn in wall_buttons:
                bulk_connect(
                    btn,
                    {
                        "button-press-event": self.on_button_press,
                        "enter-notify-event": self.on_button_hover,
                        "leave-notify-event": self.on_button_unhover,
                    },
                )

        return wall_buttons

    def on_button_hover(self, button: Button, event):
        return self.change_cursor("pointer")

    def on_button_unhover(self, button: Button, event):
        return self.change_cursor("default")

    def on_button_press(self, button: Button, event):
        img = f"{WALLPAPERS_PATH}/{button.get_child().get_name()}"
        commands = {
            1: f"wal -i {img}",
            3: f"wal -i {img} --backend colorthief",
        }
        exec_shell_command(commands.get(event.button))
        exec_shell_command_async(f"""
        swww img
        -t outer
        --transition-duration 1
        --transition-step 255
        --transition-fps 60
        {img}
        """,
        lambda *args: None)
        exec_shell_command_async(f"""
        ln -sf
        {img}
        {home_dir}/.current.wall
        """,
        lambda *args: None)
        self.parent.dashboard.player.cover.set_style(f"background-image: url('{img}');")
        exec_shell_command_async(f"python {home_dir}/.config/wal/set.py", lambda *args: None)
        return True
