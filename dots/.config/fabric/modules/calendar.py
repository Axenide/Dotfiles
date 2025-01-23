import calendar
from datetime import datetime
import gi
import modules.icons as icons
from fabric.widgets.label import Label

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib

class Calendar(Gtk.Box):
    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=4, name="calendar")

        self.current_year = datetime.now().year
        self.current_month = datetime.now().month
        self.current_day = datetime.now().day

        self.header = Gtk.Box(spacing=4, name="header")
        self.pack_start(self.header, False, False, 0)

        self.prev_month_button = Gtk.Button(name="prev-month-button", child=Label(name="month-button-label", markup=icons.chevron_left))
        self.prev_month_button.connect("clicked", self.on_prev_month_clicked)
        self.header.pack_start(self.prev_month_button, False, False, 0)

        self.month_label = Gtk.Label(name="month-label")
        self.header.pack_start(self.month_label, True, True, 0)

        self.next_month_button = Gtk.Button(name="next-month-button", child=Label(name="month-button-label", markup=icons.chevron_right))
        self.next_month_button.connect("clicked", self.on_next_month_clicked)
        self.header.pack_start(self.next_month_button, False, False, 0)

        self.weekday_row = Gtk.Box(spacing=4, name="weekday-row")
        self.pack_start(self.weekday_row, False, False, 0)

        self.grid = Gtk.Grid(column_homogeneous=True, row_homogeneous=False, name="calendar-grid")
        self.pack_start(self.grid, True, True, 0)

        self.update_calendar()
        GLib.timeout_add_seconds(60, self.check_date_change)

    def update_calendar(self):
        self.grid.foreach(lambda widget: self.grid.remove(widget))
        self.weekday_row.foreach(lambda widget: self.weekday_row.remove(widget))
        self.month_label.set_text(datetime(self.current_year, self.current_month, 1).strftime("%B %Y").capitalize())

        days = self.get_weekday_initials()  # Dynamically fetch weekday initials
        for day in days:
            label = Gtk.Label(label=day.upper(), name="weekday-label")
            self.weekday_row.pack_start(label, True, True, 0)

        cal = calendar.Calendar(firstweekday=6)
        month_days = cal.monthdayscalendar(self.current_year, self.current_month)

        # Ensure consistent number of rows (6) and placeholders for missing days
        while len(month_days) < 6:
            month_days.append([0] * 7)

        for row, week in enumerate(month_days):
            for col, day in enumerate(week):
                day_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, name="day-box")

                top_spacer = Gtk.Box(hexpand=True, vexpand=True)
                middle_box = Gtk.Box(hexpand=True, vexpand=True)
                bottom_spacer = Gtk.Box(hexpand=True, vexpand=True)

                if day == 0:
                    label = Label(name="day-empty", markup=icons.cancel)
                else:
                    label = Gtk.Label(label=str(day), name="day-label")
                    if (
                        day == self.current_day
                        and self.current_month == datetime.now().month
                        and self.current_year == datetime.now().year
                    ):
                        label.get_style_context().add_class("current-day")

                middle_box.pack_start(Gtk.Box(hexpand=True, vexpand=True), True, True, 0)  # Left spacer
                middle_box.pack_start(label, False, False, 0)  # Centered label
                middle_box.pack_start(Gtk.Box(hexpand=True, vexpand=True), True, True, 0)  # Right spacer

                day_box.pack_start(top_spacer, True, True, 0)
                day_box.pack_start(middle_box, True, True, 0)
                day_box.pack_start(bottom_spacer, True, True, 0)

                self.grid.attach(day_box, col, row, 1, 1)

        self.weekday_row.show_all()
        self.grid.show_all()

    def get_weekday_initials(self):
        # Get the localized weekday initials from the system
        return [datetime(2023, 1, i + 1).strftime("%a")[:1] for i in range(7)]

    def on_prev_month_clicked(self, widget):
        if self.current_month == 1:
            self.current_month = 12
            self.current_year -= 1
        else:
            self.current_month -= 1
        self.update_calendar()

    def on_next_month_clicked(self, widget):
        if self.current_month == 12:
            self.current_month = 1
            self.current_year += 1
        else:
            self.current_month += 1
        self.update_calendar()

    def check_date_change(self):
        now = datetime.now()
        if now.day != self.current_day or now.month != self.current_month or now.year != self.current_year:
            self.current_day = now.day
            self.current_month = now.month
            self.current_year = now.year
            self.update_calendar()
        return True
