import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import GdkPixbuf
from gi.repository import GLib

from services.mpris import MprisPlayer

class MusicPlayerWidget(Gtk.Box):
    def __init__(self, player_service):
        super().__init__(orientation=Gtk.Orientation.VERTICAL)
        self.player_service = player_service

        self.image = Gtk.Image()
        self.add(self.image)

        self.controls_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        self.add(self.controls_box)

        self.play_button = Gtk.Button(label="Play")
        self.play_button.connect("clicked", self.on_play_pause)
        self.controls_box.pack_start(self.play_button, False, False, 0)

        self.next_button = Gtk.Button(label="Next")
        self.next_button.connect("clicked", self.on_next)
        self.controls_box.pack_start(self.next_button, False, False, 0)

        self.previous_button = Gtk.Button(label="Previous")
        self.previous_button.connect("clicked", self.on_previous)
        self.controls_box.pack_start(self.previous_button, False, False, 0)

        self.update_metadata()
        self.player_service.connect("changed", self.update_metadata)

    def update_metadata(self, *args):
        metadata = self.player_service.metadata
        if metadata:
            arturl = metadata.get("arturl", None)
            if arturl:
                pixbuf = GdkPixbuf.Pixbuf.new_from_file(arturl)
                self.image.set_from_pixbuf(pixbuf)
            else:
                self.image.clear()
            title = metadata.get("title", "Unknown")
            artist = metadata.get("artist", "Unknown")
            album = metadata.get("album", "Unknown")
            print(f"Title: {title}, Artist: {artist}, Album: {album}")

    def on_play_pause(self, button):
        self.player_service.play_pause()

    def on_next(self, button):
        self.player_service.next()

    def on_previous(self, button):
        self.player_service.previous()

# Ejemplo de uso:
player_service = MprisPlayer()  # Instancia de tu servicio MprisPlayer
widget = MusicPlayerWidget(player_service)

window = Gtk.Window(title="Music Player Widget")
window.add(widget)
window.connect("destroy", Gtk.main_quit)
window.show_all()

Gtk.main()
