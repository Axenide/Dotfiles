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

        self.icon = Label(label="<span>&#xed46;</span>", markup=True)

        self.play_icon = Label(label="<span>&#xed46;</span>", markup=True)
        self.pause_icon = Label(label="<span>&#xed45;</span>", markup=True)
        self.stop_icon = Label(label="<span>&#xed4a;</span>", markup=True)

        self.skip_back_icon = Label(label="<span>&#xed48;</span>", markup=True)
        self.skip_forward_icon = Label(label="<span>&#xed49;</span>", markup=True)

        self.prev_icon = Label(label="<span>&#xed4c;</span>", markup=True)
        self.next_icon = Label(label="<span>&#xed4b;</span>", markup=True)

        self.shuffle_icon = Label(label="<span>&#xf000;</span>", markup=True)
        self.repeat_icon = Label(label="<span>&#xeb72;</span>", markup=True)

        self.shuffle = False
        self.repeat = False

        self.play_button = Button(
            name="play-button",
            child=self.icon,
        )
        self.skip_back_button = Button(
            name="skip-back-button",
            child=self.skip_back_icon,
        )
        self.skip_forward_button = Button(
            name="skip-forward-button",
            child=self.skip_forward_icon,
        )
        self.prev_button = Button(
            name="prev-button",
            child=self.prev_icon,
        )
        self.next_button = Button(
            name="next-button",
            child=self.next_icon,
        )
        self.shuffle_button = Button(
            name="shuffle-button",
            child=self.shuffle_icon,
        )
        self.repeat_button = Button(
            name="repeat-button",
            child=self.repeat_icon,
        )

        self.cover_file = f"{home_dir}/.current.wall"

        self.title = Label(
            name="title",
            # label=str(exec_shell_command('playerctl metadata title')).rstrip(),
            label="Title",
        )
        self.artist = Label(
            name="artist",
            # label=str(exec_shell_command('playerctl metadata artist')).rstrip(),
            label="Artist",
        )
        self.cover = Box(
            name="cover",
            style="background-image: url(\"" + self.cover_file + "\");",
            h_expand=True,
            v_align="end",
            orientation="v",
            children=[
                # self.title,
                # self.artist,
            ]
        )

        self.status = Label(
            name="status",
            label="",
        )
        
        # self.player_fabricator = Fabricator(stream=True, poll_from=r"""playerctl --follow metadata --format '{{status}}\n{{position}}\n{{mpris:length}}\n{{artist}}\n{{album}}\n{{title}}'""")
        self.player_fabricator = Fabricator(stream=True, poll_from=r"""playerctl --follow metadata --format '{{status}}\n{{artist}}\n{{mpris:artUrl}}\n{{title}}'""")

        def decode_player_data(_, data: str):
            data = data.split("\\n")
            playback: str = data[0] # "Playing" | "Paused"
            # position: str = data[1] # can be casted to a int if it's not empty
            # length: str = data[2] # can be casted to a int if it's not empty
            artist: str = data[1]
            album: str = data[2]
            title: str = data[3]
            # print(playback, position, length, artist, album, title)
            # print(playback, artist, album, title)
            self.status.label = playback
            self.artist.set_label(artist)
            self.title.set_label(title)
            if album == "":
                self.cover.set_style("background-image: url(\"" + self.cover_file + "\");")
            else:
                self.cover.set_style("background-image: url(\"" + album + "\");")

            if playback == "Playing":
                self.icon.set_markup("<span>&#xed46;</span>")
            elif playback == "Paused":
                self.icon.set_markup("<span>&#xed45;</span>")
            else:
                self.icon.set_markup("<span>&#xed4a;</span>")
            # self.cover.style = "background-image: url(\"" + self.cover_file + "\");"

        self.player_fabricator.connect("changed", decode_player_data)

        self.player_box = Box(
            name="player-box",
            orientation="v",
            v_align="center",
            h_align="center",
            # spacing=8,
            children=[
                self.prev_button,
                # self.skip_back_button,
                self.play_button,
                # self.skip_forward_button,
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
            name="full-player",
            orientation="h",
            h_expand=True,
            children=[
                self.cover,
                self.player_box,
                # self.title,
                # self.artist,
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
