from __init__ import *

THEMES_PATH = f"{home_dir}/.config/fabric/bar/styles/themes"

themes = {
    "AxGruv": "axgruv",
    "AxDusk": "axdusk",
    "Gruvbox Dark Hard": "gruvbox-dark-hard",
    "Gruvbox Dark Medium": "gruvbox-dark-medium",
    "Gruvbox Dark Soft": "gruvbox-dark-soft",
    "Tokyonight": "tokyonight",
    "Catppuccin Frappe": "catppuccin-frappe",
    "Catppuccin Macchiato": "catppuccin-macchiato",
    "Catppuccin Mocha": "catppuccin-mocha",
}

class Themes(MasterWithButton):
    def __init__(self):
        self.theme_buttons = []
        for theme in themes:
            self.theme_buttons.append(ThemeButton(title=theme, theme=themes[theme]))

        super().__init__(
            master_name="themes",
            master_button_name="themes-toggle",
            master_icon=icons.chevrons_up,
            children=self.theme_buttons,
        )

class ThemeButton(Button):
    def __init__(self, title: str, theme: str, **kwargs):
        self.theme = theme

        # Load theme colors from the JSON file
        self.load_theme_colors()

        self.title = Label(name="theme-title", label=title, style=f"color: {self.foreground};", markup=True)

        self.color1_circle = Label(name="color-label", label=icons.circle, markup=True, style=f"color: {self.color1};")
        self.color2_circle = Label(name="color-label", label=icons.circle, markup=True, style=f"color: {self.color2};")
        self.color3_circle = Label(name="color-label", label=icons.circle, markup=True, style=f"color: {self.color3};")
        self.color4_circle = Label(name="color-label", label=icons.circle, markup=True, style=f"color: {self.color4};")
        self.color5_circle = Label(name="color-label", label=icons.circle, markup=True, style=f"color: {self.color5};")
        self.color6_circle = Label(name="color-label", label=icons.circle, markup=True, style=f"color: {self.color6};")
        self.color7_circle = Label(name="color-label", label=icons.circle, markup=True, style=f"color: {self.color7};")

        self.theme_box = Box(
            name="theme-box",
            orientation="v",
            spacing=4,
            h_expand=True,
            h_align="fill",
            v_align="center",
            style=f"background-color: {self.background};",
            children=[
                self.title,
                Box(
                    orientation="h",
                    spacing=8,
                    h_expand=True,
                    h_align="center",
                    v_align="center",
                    children=[
                        self.color1_circle,
                        self.color2_circle,
                        self.color3_circle,
                        self.color4_circle,
                        self.color5_circle,
                        self.color6_circle,
                        self.color7_circle,
                    ],
                ),
            ],
        )

        super().__init__(name="theme-button", **kwargs)
        self.add(self.theme_box)
        self.connect("button-press-event", self.on_button_press)
        self.connect("key-press-event", self.on_key_press)

    def load_theme_colors(self):
        theme_path = os.path.join(THEMES_PATH, f"{self.theme}.json")
        try:
            with open(theme_path, 'r') as file:
                data = json.load(file)
                self.background = data['special']['background']
                self.foreground = data['special']['foreground']
                self.color1 = data['colors']['color1']
                self.color2 = data['colors']['color2']
                self.color3 = data['colors']['color3']
                self.color4 = data['colors']['color4']
                self.color5 = data['colors']['color5']
                self.color6 = data['colors']['color6']
                self.color7 = data['colors']['color7']
        except Exception as e:
            print(f"Failed to load theme {self.theme}: {e}")
            self.background = ""
            self.foreground = ""
            self.color1 = ""
            self.color2 = ""
            self.color3 = ""
            self.color4 = ""
            self.color5 = ""
            self.color6 = ""
            self.color7 = ""

    def on_button_press(self, button, event):
        exec_shell_command_async(f"hyprctl dispatch exec 'wal --theme {THEMES_PATH}/{self.theme}.json && python {home_dir}/.config/wal/set.py'", lambda *_: None)

    def on_key_press(self, widget, event):
        key = event.keyval
        if key == Gdk.KEY_Return or key == Gdk.KEY_KP_Enter:
            self.on_button_press(widget, event)
            return True
