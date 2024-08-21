from __init__ import *

class Player(Box):
    def __init__(self):
        super().__init__(
            name="player",
            visible=False,
            all_visible=False,
            h_expand=True,
            orientation="h",
        )

        self.icon = Label(label=f"{icons.stop}", markup=True)

        self.play_button = Button(
            name="play-button",
            child=self.icon,
        )
        self.prev_button = Button(
            name="prev-button",
            child=Label(label=f"{icons.prev}", markup=True),
        )
        self.next_button = Button(
            name="next-button",
            child=Label(label=f"{icons.next}", markup=True),
        )

        self.cover_file = f"{home_dir}/.current.wall"

        self.title = Label(
            name="title",
            label="Nothing playing.",
            markup=True,
            justification="left",
            ellipsization="end",
            character_max_width=32,
            v_align="end",
            h_align="start",
            h_expand=True,
        )

        self.artist = Label(
            name="artist",
            label=r"¯\_(ツ)_/¯",
            markup=True,
            justification="left",
            ellipsization="end",
            character_max_width=32,
            v_align="end",
            v_expand=True,
            h_align="start",
            h_expand=True,
        )

        self.player_box = Box(
            name="player-box",
            orientation="v",
            v_align="center",
            h_align="center",
            children=[
                self.prev_button,
                self.play_button,
                self.next_button,
            ]
        )

        self.cover = Box(
            name=f"cover",
            style=f"background-image: linear-gradient( rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5) ), url('{self.cover_file}');",
            h_expand=True,
            v_expand=True,
            v_align="fill",
            orientation="v",
            children=[
                self.artist,
                self.title,
            ],
        )

        self.player_fabricator = Fabricator(stream=True, poll_from=r"""
        playerctl --follow metadata --format
        '{{status}}\n{{artist}}\n{{title}}\n{{mpris:artUrl}}'
        """)

        def decode_player_data(_, data: str):
            playback, artist, title, cover, *_ = data.split('\\n')
            
            self.artist.set_label(artist or r"¯\_(ツ)_/¯")
            self.title.set_label(f"{icons.music} {title}" if title else "Nothing playing.")
            self.cover.set_style(f"background-image: linear-gradient( rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5) ), url('{self.cover_file}');")
            self.icon.set_markup(f"{icons.pause if playback == 'Playing' else icons.play if playback == 'Paused' else icons.stop}")

        self.player_fabricator.connect("changed", decode_player_data)

        for btn in [self.play_button, self.prev_button, self.next_button]:
            bulk_connect(
                btn,
                {
                    "button-press-event": self.on_button_press,
                    "enter-notify-event": self.on_button_hover,
                    "leave-notify-event": self.on_button_unhover,
                },
            )

        self.full_player = Box(
            name=f"full-player",
            orientation="h",
            spacing=4,
            h_expand=True,
            children=[
                self.cover,
                self.player_box,
            ]
        )

        self.add(
            self.full_player,
        )

    def on_button_hover(self, button: Button, event):
        return self.change_cursor("pointer")

    def on_button_unhover(self, button: Button, event):
        return self.change_cursor("default")

    def on_button_press(self, button: Button, event):
        match button:
            case self.play_button:
                exec_shell_command('playerctl play-pause')
            case self.prev_button:
                exec_shell_command("playerctl previous")
            case self.next_button:
                exec_shell_command("playerctl next")
        return True
