from __init__ import *

class SystemTray(Box):
    def __init__(self, pixel_size: int = 20, **kwargs) -> None:
        super().__init__(name="system-tray", orientation="v", spacing=10)
        self.pixel_size = pixel_size
        self.watcher = Gray.Watcher()
        self.watcher.connect("item-added", self.on_item_added)

    def on_item_added(self, _, identifier: str):
        item = self.watcher.get_item_for_identifier(identifier)
        item_button = self.do_bake_item_button(item)
        item.connect("removed", lambda *args: item_button.destroy())
        item_button.show_all()
        self.add(item_button)

    def do_bake_item_button(self, item: Gray.Item) -> Button:
        button = Button()

        button.connect(
            "button-press-event",
            lambda button, event: self.on_button_click(button, item, event),
        )

        pixmap = Gray.get_pixmap_for_pixmaps(item.get_icon_pixmaps(), self.pixel_size)

        try:
            if pixmap is not None:
                pixbuf = pixmap.as_pixbuf(self.pixel_size, GdkPixbuf.InterpType.HYPER)
            else:
                pixbuf = Gtk.IconTheme().load_icon(
                    item.get_icon_name(),
                    self.pixel_size,
                    Gtk.IconLookupFlags.FORCE_SIZE,
                )
        except GLib.Error:
            # Icon not found, use a default icon
            pixbuf = Gtk.IconTheme().get_default().load_icon(
                "image-missing",  # default icon name, adjust as needed
                self.pixel_size,
                Gtk.IconLookupFlags.FORCE_SIZE,
            )

        button.set_image(Gtk.Image.new_from_pixbuf(pixbuf))
        return button

    def on_button_click(self, button, item: Gray.Item, event):
        match event.button:
            case 1:
                try:
                    item.activate(event.x, event.y)
                except Exception as e:
                    logger.error(e)
            case 3:
                menu = item.get_menu()
                menu.set_name("system-tray-menu")
                if menu:
                    menu.popup_at_widget(
                        button,
                        Gdk.Gravity.SOUTH,
                        Gdk.Gravity.NORTH,
                        event,
                    )
                else:
                    item.context_menu(event.x, event.y)
