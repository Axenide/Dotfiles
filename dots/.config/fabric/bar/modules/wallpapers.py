from __init__ import *

WALLPAPERS_PATH = f"{os.getenv('XDG_PICTURES_DIR')}/Wallpapers"

def get_wallpapers():
    walls = []
    for wallpaper in os.listdir(WALLPAPERS_PATH):
        if wallpaper.endswith(".png") or wallpaper.endswith(".jpg") or wallpaper.endswith(".jpeg") or wallpaper.endswith(".webp") or wallpaper.endswith(".gif"):
            walls.append(wallpaper)
            sorted(walls)

    return walls

class Wallpapers(ScrolledWindow):
    def __init__(self):
        super().__init__(
            name="wallpapers",
            h_expand=True,
            v_expand=True,
        )

        self.wallpapers = get_wallpapers()

        self.test = Button(
            name="wall",
            style=f"""
            background-image: url("{WALLPAPERS_PATH}/current.wall");
            background-size: cover;
            background-position: center;
            """,
        )

        self.wall_box = Box(
            name="wall-box",
            orientation="v",
            spacing=4,
            h_expand=True,
            children=[
                self.test
            ]
        )

        self.add(self.wall_box)
