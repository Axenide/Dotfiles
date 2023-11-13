import OverviewButton from './buttons/OverviewButton.js';
import Workspaces from './buttons/Workspaces.js';
import DateButton from './buttons/DateButton.js';
import SysTray from './buttons/SysTray.js';
import ColorPicker from './buttons/ColorPicker.js';
import SystemIndicators from './buttons/SystemIndicators.js';
import PowerMenu from './buttons/PowerMenu.js';
import Separator from '../misc/Separator.js';
import ScreenRecord from './buttons/ScreenRecord.js';
import SubMenu from './buttons/SubMenu.js';
import { SystemTray, Widget, Variable } from '../imports.js';
import { Battery } from '../imports.js';
import Recorder from '../services/screenrecord.js';
import * as vars from '../variables.js';
import BatteryBar from './buttons/BatteryBar.js';

const submenuItems = Variable(1);
SystemTray.connect('changed', () => {
    submenuItems.setValue(SystemTray.items.length + 1);
});

const SysProgress = (type, title, unit) => Widget.Box({
    className: `system-resources-box ${type}`,
    hexpand: false,
    binds: [['tooltipText', vars[type], 'value', v =>
        `${title}: ${Math.floor(v * 100)}${unit}`]],
    child: Widget.CircularProgress({
        hexpand: true,
        inverted: false,
        className: `circular-progress ${type}`,
        binds: [['value', vars[type]]],
        startAt: 0.75
    }),
});

const SeparatorDot = (service, condition) => Separator({
    orientation: 'vertical',
    valign: 'center',
    connections: service && [[service, dot => {
        dot.visible = condition(service);
    }]],
});

const Start = () => Widget.Box({
    className: 'start',
    children: [
        OverviewButton(),
        SeparatorDot(),
        Workspaces(),
        Widget.Box({ hexpand: true }),
    ],
});

const Center = () => Widget.Box({
    className: 'center',
    children: [
        DateButton(),
    ],
});

const End = () => Widget.Box({
    className: 'end',
    children: [
        Widget.Box({ hexpand: true }),

        SubMenu({
            items: submenuItems,
            children: [
                SysTray(),
                ColorPicker(),
            ],
        }),
        
        Widget.Box({
            className: 'system-info',
            children: [
                SysProgress('cpu', 'CPU', '%'),
                SysProgress('ram', 'Memory', '%'),
                SysProgress('temp', 'Temperature', '°C'),
            ],
        }),
        SeparatorDot(Recorder, r => r.recording),
        ScreenRecord(),
        SeparatorDot(Battery, b => b.available),
        BatteryBar(),
        SeparatorDot(),
        SystemIndicators(),
        SeparatorDot(),
        PowerMenu(),
    ],
});

export default monitor => Widget.Window({
    name: `bar${monitor}`,
    exclusive: true,
    monitor,
    anchor: ['top', 'left', 'right'],
    child: Widget.CenterBox({
        className: 'panel',
        startWidget: Start(),
        centerWidget: Center(),
        endWidget: End(),
    }),
});
