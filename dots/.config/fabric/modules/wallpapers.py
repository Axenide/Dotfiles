import os
from gi.repository import GdkPixbuf, Gtk, GLib
from fabric.widgets.box import Box
from fabric.widgets.entry import Entry
from fabric.widgets.button import Button
from fabric.widgets.scrolledwindow import ScrolledWindow
from fabric.widgets.label import Label
import modules.icons as icons
import hashlib

class WallpaperSelector(Box):
    CACHE_DIR = os.path.expanduser("~/.cache/ax-shell/wallpapers")

    def __init__(self, wallpapers_dir: str, **kwargs):
        super().__init__(name="wallpapers", spacing=4, orientation="v", **kwargs)

        self.wallpapers_dir = wallpapers_dir
        os.makedirs(self.CACHE_DIR, exist_ok=True)

        self.files = [
            f for f in os.listdir(wallpapers_dir) if self._is_image(f)
        ]
        self.thumbnails = []

        self.viewport = Gtk.IconView()
        self.viewport.set_model(Gtk.ListStore(GdkPixbuf.Pixbuf, str))
        self.viewport.set_pixbuf_column(0)
        self.viewport.set_text_column(1)
        self.viewport.set_item_width(0)
        self.viewport.connect("item-activated", self.on_wallpaper_selected)

        self.scrolled_window = ScrolledWindow(
            name="scrolled-window",
            spacing=10,
            h_expand=True,
            v_expand=True,
            child=self.viewport,
        )

        self.search_entry = Entry(
            name="search-entry",
            placeholder="Search Wallpapers...",
            h_expand=True,
            notify_text=lambda entry, *_: self.arrange_viewport(entry.get_text()),
        )
        self.search_entry.props.xalign = 0.5

        # Opciones para el dropdown (clave: valor)
        self.schemes = {
            "scheme-tonal-spot": "Tonal Spot",
            "scheme-content": "Content",
            "scheme-expressive": "Expressive",
            "scheme-fidelity": "Fidelity",
            "scheme-fruit-salad": "Fruit Salad",
            "scheme-monochrome": "Monochrome",
            "scheme-neutral": "Neutral",
            "scheme-rainbow": "Rainbow",
        }

        # Crear el dropdown
        self.scheme_dropdown = Gtk.ComboBoxText()
        self.scheme_dropdown.set_name("scheme-dropdown")
        self.scheme_dropdown.set_tooltip_text("Select color scheme")
        for key, display_name in self.schemes.items():
            self.scheme_dropdown.append(key, display_name)
        self.scheme_dropdown.set_active_id("scheme-tonal-spot")  # Seleccionar Tonal Spot por defecto
        self.scheme_dropdown.connect("changed", self.on_scheme_changed)

        self.dropdown_box = Box(
            name="dropdown-box",
            spacing=10,
            orientation="h",
            children=[
                self.scheme_dropdown,
                Label(name="dropdown-label", markup=icons.chevron_down),
            ],
        )

        self.header_box = Box(
            name="header-box",
            spacing=10,
            orientation="h",
            children=[
                self.search_entry,
                self.dropdown_box,
                Button(
                    name="close-button",
                    child=Label(name="close-label", markup=icons.cancel),
                    tooltip_text="Close Selector",
                    on_clicked=lambda *_: self.close_selector(),
                ),
            ],
        )

        self.add(self.header_box)
        self.add(self.scrolled_window)

        self._start_thumbnail_thread()
        self.show_all()

    def close_selector(self):
        GLib.spawn_command_line_async("fabric-cli exec ax-shell 'notch.close_notch()'")

    def arrange_viewport(self, query: str = ""):
        self.viewport.get_model().clear()
        filtered_thumbnails = [
            (thumb, name)
            for thumb, name in self.thumbnails
            if query.casefold() in name.casefold()
        ]
        
        # Ordenar los elementos alfabéticamente por el nombre de archivo
        filtered_thumbnails.sort(key=lambda x: x[1].lower())

        # Añadir los elementos ordenados al modelo
        for pixbuf, file_name in filtered_thumbnails:
            self.viewport.get_model().append([pixbuf, file_name])

    def on_wallpaper_selected(self, iconview, path):
        model = iconview.get_model()
        file_name = model[path][1]
        full_path = os.path.join(self.wallpapers_dir, file_name)
        selected_scheme = self.scheme_dropdown.get_active_id()  # Obtener el valor del esquema
        GLib.spawn_command_line_async(f'matugen image {full_path} -t {selected_scheme}')
        # self.close_selector()

    def on_scheme_changed(self, combo):
        selected_scheme = combo.get_active_id()
        print(f"Color scheme selected: {selected_scheme}")
        # Aquí podrías agregar lógica adicional si es necesario.

    def _start_thumbnail_thread(self):
        """Inicia un hilo GLib para precargar las miniaturas."""
        thread = GLib.Thread.new("thumbnail-loader", self._preload_thumbnails, None)

    def _preload_thumbnails(self, _data):
        """Carga miniaturas en segundo plano y las añade a la vista."""
        for file_name in sorted(self.files):  # Ordenar alfabéticamente antes de procesar
            full_path = os.path.join(self.wallpapers_dir, file_name)
            cache_path = self._get_cache_path(file_name)

            # Generar o cargar miniatura
            if not os.path.exists(cache_path):
                pixbuf = self._create_thumbnail(full_path)
                if pixbuf:
                    pixbuf.savev(cache_path, "png", [], [])
            else:
                pixbuf = GdkPixbuf.Pixbuf.new_from_file(cache_path)

            # Añadir miniatura al modelo y actualizar la interfaz
            if pixbuf:
                GLib.idle_add(self._add_thumbnail_to_view, pixbuf, file_name)

    def _add_thumbnail_to_view(self, pixbuf, file_name):
        self.thumbnails.append((pixbuf, file_name))
        self.viewport.get_model().append([pixbuf, file_name])
        return False  # Detiene el callback en GLib

    def _create_thumbnail(self, image_path: str, thumbnail_size=96):
        try:
            pixbuf = GdkPixbuf.Pixbuf.new_from_file(image_path)
            width, height = pixbuf.get_width(), pixbuf.get_height()
            if width > height:
                new_width = thumbnail_size
                new_height = int(height * (thumbnail_size / width))
            else:
                new_height = thumbnail_size
                new_width = int(width * (thumbnail_size / height))
            return pixbuf.scale_simple(new_width, new_height, GdkPixbuf.InterpType.BILINEAR)
        except Exception as e:
            print(f"Error creating thumbnail for {image_path}: {e}")
            return None

    def _get_cache_path(self, file_name: str) -> str:
        file_hash = hashlib.md5(file_name.encode("utf-8")).hexdigest()
        return os.path.join(self.CACHE_DIR, f"{file_hash}.png")

    @staticmethod
    def _is_image(file_name: str) -> bool:
        return file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.webp'))
