import icons from '../../icons.js';
import PowerMenu from '../../services/powermenu.js';
import Theme from '../../services/theme/theme.js';
import Avatar from '../../misc/Avatar.js';
import { uptime } from '../../variables.js';
import { Battery, Widget, Utils } from '../../imports.js';

export const BatteryProgress = () => Widget.Box({
    className: 'battery-progress',
    vexpand: true,
    binds: [['visible', Battery, 'available']],
    connections: [[Battery, w => {
        w.toggleClassName('half', Battery.percent < 46);
        w.toggleClassName('low', Battery.percent < 30);
    }]],
    child: Widget.Overlay({
        vexpand: true,
        child: Widget.ProgressBar({
            hexpand: true,
            vexpand: true,
            connections: [[Battery, progress => {
                progress.fraction = Battery.percent / 100;
            }]],
        }),
        overlays: [Widget.Label({
            connections: [[Battery, l => {
                l.label = Battery.charging || Battery.charged
                    ? icons.battery.charging
                    : `${Battery.percent}%`;
            }]],
        })],
    }),
});

export default () => Widget.Box({
    className: 'header',
    children: [
        Avatar(),
        Widget.Box({
            className: 'system-box',
            vertical: true,
            hexpand: true,
            children: [
                Widget.Box({
                    children: [
                        Widget.Button({
                            valign: 'center',
                            onClicked: () => Theme.openSettings(),
                            child: Widget.Icon(icons.settings),
                        }),
                        Widget.Label({
                            className: 'uptime',
                            hexpand: true,
                            valign: 'center',
                            connections: [[uptime, label => {
                                label.label = `uptime: ${uptime.value}`;
                            }]],
                        }),
                        Widget.Button({
                            valign: 'center',
                            onClicked: () => Utils.execAsync(`gtklock`),
                            child: Widget.Icon(icons.lock),

                        }),
                        Widget.Button({
                            valign: 'center',
                            onClicked: () => PowerMenu.action('shutdown'),
                            child: Widget.Icon(icons.powermenu.shutdown),
                        }),
                    ],
                }),
                BatteryProgress(),
            ],
        }),
    ],
});
