from __init__ import *

class Calendar(EventBox):
    def __init__(self):
        super().__init__(
            # name="calendar",
            h_expand=True,
            h_align="fill",
            v_align="fill",
            # orientation="v",
        )

        self.set_above_child(False)

        self.current_year = datetime.now().year
        self.current_month = datetime.now().month

        self.prev_month_button = Button(name="chevron", child=Label(label="<span>&#xea60;</span>", markup=True))
        self.prev_month_button.connect("clicked", self.on_prev_month_clicked)

        self.month_label = Label(name="month")

        self.next_month_button = Button(name="chevron", child=Label(label="<span>&#xea61;</span>", markup=True))
        self.next_month_button.connect("clicked", self.on_next_month_clicked)

        self.prev_year_button = Button(name="chevron", child=Label(label="<span>&#xea60;</span>", markup=True))
        self.prev_year_button.connect("clicked", self.on_prev_year_clicked)

        self.year_label = Label(name="year")

        self.next_year_button = Button(name="chevron", child=Label(label="<span>&#xea61;</span>", markup=True))
        self.next_year_button.connect("clicked", self.on_next_year_clicked)

        self.prev_month_rev = Revealer(
            transition_type="slide-left",
            transition_duration=300,
            child=self.prev_month_button,
        )

        self.next_month_rev = Revealer(
            transition_type="slide-right",
            transition_duration=300,
            child=self.next_month_button,
        )

        self.prev_year_rev = Revealer(
            transition_type="slide-left",
            transition_duration=300,
            child=self.prev_year_button,
        )

        self.next_year_rev = Revealer(
            transition_type="slide-right",
            transition_duration=300,
            child=self.next_year_button,
        )

        self.month_header = Box(
            orientation="h",
            children=[
                self.prev_month_rev,
                self.month_label,
                self.next_month_rev,
            ],
        )

        self.year_header = Box(
            orientation="h",
            children=[
                self.prev_year_rev,
                self.year_label,
                self.next_year_rev,
            ],
        )

        self.header = Box(
            name="header",
            orientation="h",
            children=[
                self.month_header,
                Box(h_expand=True),
                self.year_header,
            ],
        )

        self.overlay = Overlay()
        self.grid = Gtk.Grid()
        self.overlay.add(self.grid)
        self.hover_area = EventBox()
        self.hover_area.set_size_request(-1, -1)
        self.overlay.add_overlay(self.hover_area)

        self.calendar = Box(
            name="calendar",
            orientation="v",
            h_expand=True,
            h_align="fill",
            v_align="fill",
            children=[
                self.header,
                self.overlay,
            ],
        )

        self.revealers = [self.prev_month_rev, self.next_month_rev, self.prev_year_rev, self.next_year_rev]

        for revealer in self.revealers:
            revealer.set_reveal_child(False)

        # self.overlay = Overlay()
        # self.overlay.add(self.calendar)
        # self.overlay.add(self.grid)
        # self.hover_area = EventBox()
        # self.hover_area.set_size_request(-1, -1)
        # self.overlay.add_overlay(self.hover_area)

        self.add(self.calendar)
        # self.add(self.overlay)

        self.connect("enter-notify-event", self.on_hover)
        self.connect("leave-notify-event", self.on_unhover)
        self.prev_month_button.connect("enter-notify-event", self.on_hover)
        self.prev_month_button.connect("leave-notify-event", self.on_unhover)
        self.next_month_button.connect("enter-notify-event", self.on_hover)
        self.next_month_button.connect("leave-notify-event", self.on_unhover)
        self.prev_year_button.connect("enter-notify-event", self.on_hover)
        self.prev_year_button.connect("leave-notify-event", self.on_unhover)
        self.next_year_button.connect("enter-notify-event", self.on_hover)
        self.next_year_button.connect("leave-notify-event", self.on_unhover)
        self.hover_area.connect("enter-notify-event", self.on_hover)
        self.hover_area.connect("leave-notify-event", self.on_unhover)

        self.update_calendar()
        self.reset_calendar()

    def update_calendar(self):
        self.create_calendar(self.current_year, self.current_month)
        self.month_label.set_text(datetime(self.current_year, self.current_month, 1).strftime("%B").capitalize())
        self.year_label.set_text(str(self.current_year))

    def create_calendar(self, year, month):
        # Clear the grid first
        for child in self.grid.get_children():
            self.grid.remove(child)

        days = self.get_weekday_initials()
        
        # Create headers for days of the week
        for i, day in enumerate(days):
            label = Label(name="week-days", label=day, h_expand=True, h_align="fill", v_expand=True, v_align="fill")
            self.grid.attach(label, i, 0, 1, 1)

        cal = calendar.Calendar(firstweekday=6)  # Start the week with Sunday
        month_days = cal.monthdayscalendar(year, month)
        
        # Ensure 6 rows are displayed
        while len(month_days) < 6:
            month_days.append([0] * 7)
        
        for i, week in enumerate(month_days):
            revealer = Revealer(transition_type="slide-down", transition_duration=300)
            revealer.set_reveal_child(True)
            week_box = Box(orientation="h", h_expand=True, v_expand=True)

            self.revealers.append(revealer)

            for j, day in enumerate(week):
                if day == 0:
                    label = Label(name="dimmed", label="×", h_expand=True, h_align="fill", v_expand=True, v_align="fill")
                else:
                    label = Label(name="day", label=str(day).zfill(2), h_expand=True, h_align="fill", v_expand=True, v_align="fill")
                    if (day == datetime.now().day and
                        month == datetime.now().month and
                        year == datetime.now().year):
                        label.set_name("current-day")
                        revealer.set_reveal_child(True)
                    if i == 0 and day > 7:
                        label.set_name("dimmed")
                    if i == 5 and day < 15:
                        label.set_name("dimmed")

                week_box.add(label)
            
            revealer.add(week_box)
            self.grid.attach(revealer, 0, i + 1, 7, 1)

    def get_weekday_initials(self):
        # Return the initials of the days starting from Sunday
        return [datetime(2021, 1, i).strftime('%a')[0].upper() for i in range(3, 10)]  # Jan 3, 2021 is a Sunday

    def reset_calendar(self):
        for revealer in self.revealers:
            week_box = revealer.get_child()
            if any(label.get_name() == "current-day" for label in week_box.get_children()):
                revealer.set_reveal_child(True)
            else:
                revealer.set_reveal_child(False)

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

    def on_prev_year_clicked(self, widget):
        self.current_year -= 1
        self.update_calendar()

    def on_next_year_clicked(self, widget):
        self.current_year += 1
        self.update_calendar()

    def on_hover(self, widget, event):
        for revealer in self.revealers:
            revealer.set_reveal_child(True)

    def on_unhover(self, widget, event):
        for revealer in self.revealers:
            if self.current_month == datetime.now().month and self.current_year == datetime.now().year:
                week_box = revealer.get_child()
                if any(label.get_name() == "current-day" for label in week_box.get_children()):
                    revealer.set_reveal_child(True)
                else:
                    revealer.set_reveal_child(False)
