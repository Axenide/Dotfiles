import Clock from '../misc/Clock.js';
import { Widget } from '../imports.js';

export default () => Widget.Box({
    vertical: true,
    className: 'datemenu',
    children: [
        Clock({ format: '%H:%M' }),
        Widget.Box({
            className: 'calendar',
            children: [
                Widget({
                    type: imports.gi.Gtk.Calendar,
                    hexpand: true,
                    halign: 'center',
                }),
            ],
        }),
    ],
});
