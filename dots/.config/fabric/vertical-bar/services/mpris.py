import gi
from gi.repository import GLib  # type: ignore
from loguru import logger

from fabric.service import Property, Service, Signal, SignalContainer
from fabric.utils import bulk_connect


class PlayerctlImportError(ImportError):
    def __init__(self, *args):
        super().__init__(
            "Playerctl is not installed, please install it first",
            *args,
        )


try:
    gi.require_version("Playerctl", "2.0")
    from gi.repository import Playerctl  # type: ignore
except ValueError:
    raise PlayerctlImportError()

# TODO: consider building my own mpris service using dbus rather than playerctl


class MprisPlayer(Service):
    __gsignals__ = SignalContainer(
        Signal("exit", "run-first", None, (bool,)),
        Signal("changed", "run-first", None, ()),  # type: ignore
    )

    def __init__(
        self,
        player: Playerctl.Player,
        **kwargs,
    ):
        self._signal_connectors: dict = {}
        self._player: Playerctl.Player = player
        super().__init__(**kwargs)
        for sn in ["playback-status", "loop-status", "shuffle", "volume", "seeked"]:
            self._signal_connectors[sn] = self._player.connect(
                sn, lambda *args, sn=sn: self.notifier(sn, args)
            )

        self._signal_connectors["exit"] = self._player.connect(
            "exit", self.on_player_exit
        )
        self._signal_connectors["metadata"] = self._player.connect(
            "metadata", lambda *args: self.update_status()
        )
        GLib.idle_add(lambda *args: self.update_status_once())

    def update_status(self):
        for prop in [
            "metadata",
            "title",
            "artist",
            "arturl",
            "length",
        ]:
            self.notifier(prop) if self.get_property(prop) is not None else None
        for prop in [
            "can-seek",
            "can-pause",
            "can-shuffle",
            "can-go-next",
            "can-go-previous",
        ]:
            self.notifier(prop)

    def update_status_once(self):
        for prop in self.list_properties():  # type: ignore
            self.notifier(prop.name)

    def notifier(self, name: str, args=None):
        self.notify(name)
        self.emit("changed")  # type: ignore
        return

    def on_player_exit(self, player):
        for id in self._signal_connectors.values():
            try:
                self._player.disconnect(id)
            except Exception:
                pass
        del self._player
        self.emit("exit", True)  # type: ignore
        # TODO check if this is needed
        del self

    def toggle_shuffle(self):
        self._player.set_shuffle(
            not self._player.props.shuffle  # type: ignore
        ) if self.can_shuffle else None

    def play_pause(self):
        self._player.play_pause() if self.can_pause else None

    def next(self):
        self._player.next() if self.can_go_next else None

    def previous(self):
        self._player.previous() if self.can_go_previous else None

    def set_position(self, pos: int):
        self._player.set_position(pos) if self.can_seek else None

    def get_position(self) -> int:
        return self._player.get_position() if self.can_seek else None  # type: ignore

    def set_loop_status(self, status: str):
        loop_status = {
            "none": Playerctl.LoopStatus.NONE,
            "track": Playerctl.LoopStatus.TRACK,
            "playlist": Playerctl.LoopStatus.PLAYLIST,
        }.get(status, None)

        self._player.set_loop_status(loop_status) if loop_status else None

    # Properties
    @Property(value_type=int, flags="readable")
    def position(self) -> int:
        return self._player.get_property("position")  # type: ignore

    @Property(value_type=object, flags="readable")
    def metadata(self) -> dict:
        return self._player.get_property("metadata")  # type: ignore

    @Property(value_type=str or None, flags="readable")
    def arturl(self) -> str | None:
        if "mpris:artUrl" in self.metadata.keys():  # type: ignore
            return self.metadata["mpris:artUrl"]  # type: ignore
        return None

    @Property(value_type=str or None, flags="readable")
    def length(self) -> str | None:
        if "mpris:length" in self.metadata.keys():  # type: ignore
            return self.metadata["mpris:length"]  # type: ignore
        return None

    @Property(value_type=str, flags="readable")
    def artist(self) -> str:
        return self._player.get_artist()  # type: ignore

    @Property(value_type=str, flags="readable")
    def album(self) -> str:
        return self._player.get_album()  # type: ignore

    @Property(value_type=str, flags="readable")
    def title(self):
        return self._player.get_title()

    @Property(value_type=bool, default_value=False, flags="readable")
    def shuffle(self) -> bool:
        return self._player.get_property("shuffle")  # type: ignore

    @Property(value_type=str, flags="readable")
    def playback_status(self) -> str:
        return {
            Playerctl.PlaybackStatus.PAUSED: "paused",
            Playerctl.PlaybackStatus.PLAYING: "playing",
            Playerctl.PlaybackStatus.STOPPED: "stopped",
        }.get(self._player.get_property("playback_status"), "unknown")  # type: ignore

    @Property(value_type=str, flags="readable")
    def loop_status(self) -> str:
        return {
            Playerctl.LoopStatus.NONE: "none",
            Playerctl.LoopStatus.TRACK: "track",
            Playerctl.LoopStatus.PLAYLIST: "playlist",
        }.get(self._player.get_property("loop_status"), "unknown")  # type: ignore

    @Property(value_type=bool, default_value=False, flags="readable")
    def can_go_next(self) -> bool:
        return self._player.get_property("can_go_next")  # type: ignore

    @Property(value_type=bool, default_value=False, flags="readable")
    def can_go_previous(self) -> bool:
        return self._player.get_property("can_go_previous")  # type: ignore

    @Property(value_type=bool, default_value=False, flags="readable")
    def can_seek(self) -> bool:
        return self._player.get_property("can_seek")  # type: ignore

    @Property(value_type=bool, default_value=False, flags="readable")
    def can_pause(self) -> bool:
        return self._player.get_property("can_pause")  # type: ignore

    @Property(value_type=bool, default_value=False, flags="readable")
    def can_shuffle(self) -> bool:
        try:
            self._player.set_shuffle(self._player.get_property("shuffle"))
            return True
        except Exception:
            return False

    @Property(value_type=bool, default_value=False, flags="readable")
    def can_loop(self) -> bool:
        try:
            self._player.set_shuffle(self._player.get_property("shuffle"))
            return True
        except Exception:
            return False


class MprisPlayerManager(Service):
    __gsignals__ = SignalContainer(
        Signal("player-appeared", "run-first", None, (Playerctl.Player,)),
        Signal("player-vanished", "run-first", None, (str,)),
    )

    def __init__(
        self,
        **kwargs,
    ):
        self._manager = Playerctl.PlayerManager.new()
        bulk_connect(
            self._manager,
            {
                "name-appeared": self.on_name_appeard,
                "name-vanished": self.on_name_vanished,
            },
        )
        self.add_players()
        super().__init__(**kwargs)

    def on_name_appeard(self, manager, player_name: Playerctl.PlayerName):
        logger.info(f"[MprisPlayer] {player_name.name} appeared")
        new_player = Playerctl.Player.new_from_name(player_name)
        manager.manage_player(new_player)
        self.emit("player-appeared", new_player)  # type: ignore

    def on_name_vanished(self, manager, player_name: Playerctl.PlayerName):
        logger.info(f"[MprisPlayer] {player_name.name} vanished")
        self.emit("player-vanished", player_name.name)  # type: ignore

    def add_players(self):
        for player in self._manager.get_property("player-names"):  # type: ignore
            self._manager.manage_player(Playerctl.Player.new_from_name(player))  # type: ignore
        logger.info(f"[MprisPlayer] starting manager: {self._manager}")

    @Property(value_type=object, flags="readable")
    def players(self):
        return self._manager.get_property("players")  # type: ignore
