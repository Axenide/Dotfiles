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

        self.play_button = Button(
            name="play-button",
            icon_image=Image(
                image_file=get_relative_path("../assets/stop.svg"),
            )
        )
        self.skip_back_button = Button(
            name="skip-back-button",
            icon_image=Image(
                image_file=get_relative_path("../assets/skip-back.svg"),
            )
        )
        self.skip_forward_button = Button(
            name="skip-forward-button",
            icon_image=Image(
                image_file=get_relative_path("../assets/skip-forward.svg"),
            )
        )
        self.prev_button = Button(
            name="prev-button",
            icon_image=Image(
                image_file=get_relative_path("../assets/prev.svg"),
            )
        )
        self.next_button = Button(
            name="next-button",
            icon_image=Image(
                image_file=get_relative_path("../assets/next.svg"),
            )
        )
        self.shuffle_button = Button(
            name="shuffle-button",
            icon_image=Image(
                image_file=get_relative_path("../assets/shuffle-off.svg"),
            )
        )
        self.repeat_button = Button(
            name="repeat-button",
            icon_image=Image(
                image_file=get_relative_path("../assets/repeat-off.svg"),
            )
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
                self.play_button.set_image(
                    Image(
                        image_file=get_relative_path("../assets/pause.svg"),
                    )
                )
            elif playback == "Paused":
                self.play_button.set_image(
                    Image(
                        image_file=get_relative_path("../assets/play.svg"),
                    )
                )
            else:
                self.play_button.set_image(
                    Image(
                        image_file=get_relative_path("../assets/stop.svg"),
                    )
                )
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
        
    # def update_status(self):
    #     def get_cover():
    #         if str(exec_shell_command('playerctl metadata mpris:artUrl')).rstrip() != "":
    #             return "file:///home/adriano/Imágenes/Wallpapers/current.wall"
    #         else:
    #             return str(exec_shell_command('playerctl metadata mpris:artUrl')).rstrip()
    #
    #     self.cover_file = get_cover()
    #     self.cover.style = "background-image: url(\"" + self.cover_file + "\");"
    #     self.title.label = str(exec_shell_command('playerctl metadata title')).rstrip()
    #     self.artist.label = str(exec_shell_command('playerctl metadata artist')).rstrip()
    #     print(self.cover_file)
    #     return True
    
    def on_button_hover(self, button: Button, event):
        if button == self.play_button:
            if self.status.label == "Playing":
                self.play_button.set_image(
                    Image(
                        image_file=get_relative_path("../assets/pause-hover.svg"),
                    )
                )
            elif self.status.label == "Paused":
                self.play_button.set_image(
                    Image(
                        image_file=get_relative_path("../assets/play-hover.svg"),
                    )
                )
            else:
                self.play_button.set_image(
                    Image(
                        image_file=get_relative_path("../assets/stop-hover.svg"),
                    )
                )
        # elif button == self.skip_back_button:
        #     exec_shell_command("playerctl position 10-")
        # elif button == self.skip_forward_button:
        #     exec_shell_command("playerctl position 10+")
        elif button == self.prev_button:
            self.prev_button.set_image(
                Image(
                    image_file=get_relative_path("../assets/prev-hover.svg"),
                )
            )
        elif button == self.next_button:
            self.next_button.set_image(
                Image(
                    image_file=get_relative_path("../assets/next-hover.svg"),
                )
            )
        # elif button == self.shuffle_button:
        #     exec_shell_command("playerctl shuffle")
        # elif button == self.repeat_button:
        #     exec_shell_command("playerctl repeat")
        return self.change_cursor("pointer")

    def on_button_unhover(self, button: Button, event):
        if button == self.play_button:
            if self.status.label == "Playing":
                self.play_button.set_image(
                    Image(
                        image_file=get_relative_path("../assets/pause.svg"),
                    )
                )
            elif self.status.label == "Paused":
                self.play_button.set_image(
                    Image(
                        image_file=get_relative_path("../assets/play.svg"),
                    )
                )
            else:
                self.play_button.set_image(
                    Image(
                        image_file=get_relative_path("../assets/stop.svg"),
                    )
                )
        elif button == self.prev_button:
            self.prev_button.set_image(
                Image(
                    image_file=get_relative_path("../assets/prev.svg"),
                )
            )
        elif button == self.next_button:
            self.next_button.set_image(
                Image(
                    image_file=get_relative_path("../assets/next.svg"),
                )
            )
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
