import TopBar from './js/bar/TopBar.js';
import ScreenCorners from './js/screencorner/ScreenCorners.js';
import Overview from './js/overview/Overview.js';
import Dashboard from './js/dashboard/Dashboard.js';
import OSD from './js/osd/OSD.js';
import Applauncher from './js/applauncher/Applauncher.js';
import PowerMenu from './js/powermenu/PowerMenu.js';
import Notifications from './js/notifications/Notifications.js';
import QuickSettings from './js/quicksettings/QuickSettings.js';
import options from './js/options.js';
import * as setup from './js/utils.js';
import { forMonitors } from './js/utils.js';
import Verification from './js/powermenu/Verification.js';

setup.warnOnLowBattery();
setup.scssWatcher();
setup.globalServices();

export default {
    maxStreamVolume: 1.05,
    cacheNotificationActions: true,
    closeWindowDelay: {
        'quicksettings': options.windowAnimationDuration,
        'dashboard': options.windowAnimationDuration,
    },
    windows: [
        forMonitors(TopBar),
        forMonitors(ScreenCorners),
        forMonitors(OSD),
        forMonitors(Notifications),
        Applauncher(),
        Overview(),
        Dashboard(),
        QuickSettings(),
        PowerMenu(),
        Verification(),
    ].flat(2),
};

