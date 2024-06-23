from __init__ import *

class Player(Box):
    def __init__(self, location):
        super().__init__(
            name="player",
            visible=False,
            all_visible=False,
            h_expand=True,
            orientation="h",
        )

        self.icon = Label(label=f"{icons.stop}", markup=True)

        self.shuffle = False
        self.repeat = False

        self.play_button = Button(
            name="play-button",
            child=self.icon,
        )
        self.skip_back_button = Button(
            name="skip-back-button",
            child=Label(label=f"{icons.skip_back}", markup=True),
        )
        self.skip_forward_button = Button(
            name="skip-forward-button",
            child=Label(label=f"{icons.skip_forward}", markup=True),
        )
        self.prev_button = Button(
            name="prev-button",
            child=Label(label=f"{icons.prev}", markup=True),
        )
        self.next_button = Button(
            name="next-button",
            child=Label(label=f"{icons.next}", markup=True),
        )
        self.shuffle_button = Button(
            name="shuffle-button",
            child=Label(label=f"{icons.shuffle}", markup=True),
        )
        self.repeat_button = Button(
            name="repeat-button",
            child=Label(label=f"{icons.repeat}", markup=True),
        )

        self.cover_file = f"{home_dir}/.current.wall"

        self.title = Label(
            name="title",
            label="Nothing playing.",
            markup=True,
            justification="left",
            ellipsization="end",
            character_max_width=30,
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
            character_max_width=30,
            v_align="end",
            v_expand=True,
            h_align="start",
            h_expand=True,
        )

        self.position = Gtk.ProgressBar(
            name="position",
            fraction=True,
        )

        self.position.set_fraction(0.5)
        self.position.set_no_show_all(True)

        self.cover_text = Box(
            name=f"cover-text-{location}",
            h_expand=True,
            v_expand=True,
            v_align="fill",
            orientation="v",
            children=[
                self.artist,
                self.title,
                self.position,
            ],
        )


        self.cover = Box(
            name=f"cover-{location}",
            style=f"background-image: url('{self.cover_file}');",
            h_expand=True,
            h_align="fill",
            v_expand=True,
            v_align="fill",
            orientation="v",
            children=[
                self.cover_text,
            ]
        )

        self.status = Label(
            name="status",
            label="",
        )
        
        # self.player_fabricator = Fabricator(stream=True, poll_from=r"""
        # playerctl --follow metadata --format
        # '{{status}}\n{{artist}}\n{{title}}\n{{mpris:artUrl}}\n{{album}}\n{{position}}\n{{mpris:length}}'
        # """)
        
        self.player_fabricator = Fabricator(stream=True, poll_from=r"""
        playerctl --follow metadata --format
        '{{status}}\n{{artist}}\n{{title}}\n{{mpris:artUrl}}'
        """)

        def decode_player_data(_, data: str):
            datalist = data.split('\\n')
            playback = datalist[0]
            artist = datalist[1]
            title = datalist[2]
            cover = datalist[3]
            # album = datalist[4]
            # position = datalist[5]
            # length = datalist[6]

            self.status.label = playback
            self.artist.set_label(artist) if artist != "" else self.artist.set_label(r"¯\_(ツ)_/¯")
            self.title.set_label(f"{icons.music} {title}") if title != "" else self.title.set_label("Nothing playing.")

            if cover == "":
                self.cover.set_style(f"background-image: url('{self.cover_file}');")
            else:
                self.cover.set_style(f"background-image: url('{cover}');")

            if playback == "Playing":
                self.icon.set_markup(f"{icons.pause}")
            elif playback == "Paused":
                self.icon.set_markup(f"{icons.play}")
            else:
                self.icon.set_markup(f"{icons.stop}")

        self.player_fabricator.connect("changed", decode_player_data)

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

        for btn in [self.play_button, self.skip_back_button, self.skip_forward_button, self.prev_button, self.next_button, self.shuffle_button, self.repeat_button]:
            bulk_connect(
                btn,
                {
                    "button-press-event": self.on_button_press,
                    "enter-notify-event": self.on_button_hover,
                    "leave-notify-event": self.on_button_unhover,
                },
            )

        self.full_player = Box(
            name=f"full-player-{location}",
            orientation="h",
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
        if button == self.play_button:
            exec_shell_command('playerctl play-pause')
        elif button == self.skip_back_button:
            exec_shell_command("playerctl position 10-")
        elif button == self.skip_forward_button:
            exec_shell_command("playerctl position 10+")
        elif button == self.prev_button:
            exec_shell_command("playerctl previous")
        elif button == self.next_button:
            exec_shell_command("playerctl next")
        elif button == self.shuffle_button:
            exec_shell_command("playerctl shuffle")
        elif button == self.repeat_button:
            exec_shell_command("playerctl repeat")
        return True
