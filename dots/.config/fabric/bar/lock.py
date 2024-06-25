from __init__ import *

class LockScreen(Window):
    def __init__(self, lock: GtkSessionLock.Lock):
        self.lock = lock
        self.entry = Entry(
            name="lock-entry",
            on_activate=self.on_activate,
        )
        self.entry.set_visibility(False)  # Esto oculta el texto ingresado
        self.entry.set_alignment(0.5)

        self.clock = Box(
            orientation="v",
            v_align="center",
            h_align="center",
            h_expand=True,
            children=[
                DateTime(name="lock-time", format_list=['%H:%M:%S']),
                # DateTime(name="lock-time", format_list=['%H:%M']),
                # DateTime(name="lock-time", format_list=['%H']),
                # DateTime(name="lock-time", format_list=['%M']),
            ],
        )

        self.box = CenterBox(
            name="lock-box",
            orientation="v",
            h_expand=True,
            h_align="center",
            spacing=20,
        )

        self.player = Box(
            name="lock-player",
            orientation="v",
            h_align="center",
            children=[
                Player("lock"),
            ],
        )

        self.box.add_center(self.clock)
        self.box.add_center(self.entry)
        self.box.add_end(self.player)

        self.entry.grab_focus()

        super().__init__(
            name="lock",
            layer="top",
            visible=False,
            all_visible=False,
            children=self.box,
            anchor="left top bottom right",
            style=f"background: url('{home_dir}/.current.lock'); background-size: cover; background-position: center; transition: all 1s ease; opacity: 0.0;",
        )

    def on_activate(self, entry: Entry, *args):
        if entry.get_text() == "help":
            pass
        elif not pam.authenticate(f"{user}", (entry.get_text() or "").strip()):
            return
        self.lock.unlock_and_destroy()
        self.destroy()


def initialize():
    lock = GtkSessionLock.prepare_lock()
    lock.lock_lock()
    lockscreen = LockScreen(lock)
    lock.new_surface(lockscreen, Gdk.Display.get_default().get_monitor(0))
    lockscreen.show_all()
    set_stylesheet_from_file(get_relative_path("style.css"))
    lockscreen.set_style(f"background: url('{home_dir}/.current.lock'); background-size: cover; background-position: center; transition: all 1s ease; opacity: 1.0;")



initialize()

fabric.start()
