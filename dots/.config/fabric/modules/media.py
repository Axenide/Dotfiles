from math import nan
from fabric.widgets.box import Box
from fabric.widgets.label import Label
from fabric.widgets.button import Button
from fabric.widgets.scale import Scale
from widgets.image import CustomImage
from widgets.animator import Animator
from fabric.widgets.overlay import Overlay
from fabric.utils.helpers import FormattedString, truncate
from gi.repository import GLib, GdkPixbuf, Playerctl, Gtk # type: ignore
import modules.icons as icons
import requests


class Media(Box):
    def __init__(self, **kwargs):
        super().__init__(
            name="media",
            visable=False,
            orientation="v",
            spacing=4,
            v_align="end",
            h_align="center",
            h_expand=True,
            visible=False,
            all_visible=False,
            **kwargs,
        )

        #self.title = FormattedString("",truncate=truncate,)
        self.title = Label("",)
        self.add(self.title)

        self.art = CustomImage(name="media-image", width=200, height=200)
        self.add(self.art)

        # self.progress = Scale(
        #             name="media-bar",
        #             min=0,
        #             max=1,
        #             value=0.2,
        #             orientation='h',
        #             draw_value=True
        #         )
        # self.add(self.progress)

        self.player = Playerctl.Player()
        self.set_to_spotify()
        self.play_pause_icon = Label(name="button-label", markup=icons.play)

        self.player.connect('metadata', self.load_song)
        self.player.connect('playback-status', self.icon_player)

        self.icon_player(self.player, self.player.props.playback_status)
        self.load_song(self.player, self.player.props.metadata)

        buttons = [Button(
            name="media-menu-button",
            child=Label(name="button-label", markup=icons.skip_back),
            on_clicked=self.prev,
        ),Button(
            name="media-menu-button",
            child=self.play_pause_icon,
            on_clicked=self.play,
        ),Button(
            name="media-menu-button",
            child=Label(name="button-label", markup=icons.skip_forward),
            on_clicked=self.next,
        )
        ]

        self.box1 = Box(
            orientation="h",
            spacing=4,
            v_align="center",
            h_align="center",
            v_expand=True,
            h_expand=True,
            children=buttons
        )

        self.add(self.box1)

        self.show_all()

    def close_menu(self):
        GLib.spawn_command_line_async("fabric-cli exec ax-shell 'notch.close_notch()'")

    def play(self, *args):
        self.player.play_pause()

    def prev(self, *args):
        self.player.previous()

    def next(self, *args):
        self.player.next()

    def icon_player(self, player, status):
        match status:
            case status.PLAYING:
                self.play_pause_icon.set_markup(icons.pause)
            case status.PAUSED:
                self.play_pause_icon.set_markup(icons.play)

    def load_song(self, player, metadata):
        try:
            # Get the album art URL from playerctl
            album_art_url = metadata['mpris:artUrl']
            if len(metadata['xesam:title']) < 20:
                self.title.set_label(metadata['xesam:title'])
            else:
                self.title.set_label(metadata['xesam:title'][:12]+"...")
            if not album_art_url:
                raise ValueError("No album art URL found!")
            img_data = requests.get(album_art_url).content

            #loading the new image
            loader = GdkPixbuf.PixbufLoader()
            loader.set_size(200, 200)
            loader.write_bytes(GLib.Bytes.new(img_data)) # type: ignore
            loader.close()
            self.art.set_from_pixbuf(loader.get_pixbuf())

        except Exception as e:
            print(f"Error: {e}")
            return False

    def set_to_spotify(self):
        players = [player.name for player in Playerctl.list_players()]
        if "spotify" in players:
            self.player = Playerctl.Player.new("spotify")
        else:
            self.player = Playerctl.Player()
