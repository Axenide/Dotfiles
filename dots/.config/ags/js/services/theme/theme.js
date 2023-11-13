import themes from '../../themes.js';
import setupScss from './scss.js';
import setupHyprland from './hyprland.js';
import SettingsDialog from '../../settingsdialog/SettingsDialog.js';
import IconBrowser from '../../misc/IconBrowser.js';
import { Service, Utils } from '../../imports.js';
import GLib from 'gi://GLib';


const THEME_CACHE = Utils.CACHE_DIR + '/theme-overrides.json';

class ThemeService extends Service {
    static { Service.register(this); }

    get themes() { return themes; }

    _defaultAvatar = `/home/${Utils.USER}/face.png`;
    _defaultTheme = themes[0].name;

    constructor() {
        super();
        Utils.exec('swww init');
        this.setup();
        
    }

    openSettings() {
        if (!this._dialog)
            this._dialog = SettingsDialog();

        this._dialog.hide();
        this._dialog.present();
    }

    iconBrowser() {
        IconBrowser();
    }

    getTheme() {
        return themes.find(({ name }) => name === this.getSetting('theme'));
        
    }

    setup() {
        const theme = {
            ...this.getTheme(),
            ...this.settings,
        };
        setupScss(theme);
        setupHyprland(theme);
        this.setupOther();
        this.getGTK();
        this.getGTKIcons();
        this.getPyWall();
        this.AutoWallpaper();
        
    }

    reset() {
        Utils.exec(`rm ${THEME_CACHE}`);
        this._settings = null;
        this.setup();
        this.emit('changed');
    }

    setupOther() {
        const darkmode = this.getSetting('color_scheme') === 'dark';

        if (Utils.exec('which gsettings')) {
            const gsettings = 'gsettings set org.gnome.desktop.interface color-scheme';
            Utils.execAsync(`${gsettings} "prefer-${darkmode ? 'dark' : 'light'}"`).catch(print);
        }
    }

    get settings() {
        if (this._settings)
            return this._settings;

        try {
            this._settings = JSON.parse(Utils.readFile(THEME_CACHE));
        } catch (_) {
            this._settings = {};
        }

        return this._settings;
    }

    setSetting(prop, value) {
        const settings = this.settings;
        settings[prop] = value;
        Utils.writeFile(JSON.stringify(settings, null, 2), THEME_CACHE).catch(print);
        this._settings = settings;
        this.emit('changed');

        if (prop === 'layout') {
            if (!this._notiSent) {
                this._notiSent = true;
                Utils.execAsync(['notify-send', 'Layout Change Needs a Reload']);
            }
            return;
        }

        this.setup();
    }

    getSetting(prop) {
        if (prop === 'theme')
            return this.settings.theme || this._defaultTheme;

        if (prop === 'avatar')
            return this.settings.avatar || this._defaultAvatar;

        return this.settings[prop] !== undefined
            ? this.settings[prop]
            : this.getTheme()[prop];
    }

    getGTK() {
        const currentGTKName = this.getSetting('gtk_theme');
        if (currentGTKName) {
            const gtk = themes.find(({ gtk_theme }) => gtk_theme === currentGTKName);
            Utils.execAsync(`gsettings set org.gnome.desktop.interface gtk-theme ${currentGTKName}`);
            return gtk;
        } else {
            return null; 
        }
    }

    getGTKIcons() {
        const currentGTKIcons = this.getSetting('icons');
        if (currentGTKIcons) {
            const icons = themes.find(({ icons }) => icons === currentGTKIcons);
            Utils.execAsync(`gsettings set org.gnome.desktop.interface icon-theme ${currentGTKIcons}`);
            return icons;
        } else {
            return null;
        }
    } 
    
    getPyWall() {
        const currentPyWallTheme = this.getSetting('pywall_theme');
        if (currentPyWallTheme) {
            const pywall = themes.find(({ pywall_theme }) => pywall_theme === currentPyWallTheme);
            Utils.execAsync(`wal --theme ${currentPyWallTheme}`);
            return pywall;
        } else {
            return null;
        }
    } 
    
    AutoWallpaper() {
        const backgrounds = GLib.get_home_dir() + '/.dots/backgrounds';
        const AutoWallpaper = this.getSetting('theme_wallpaper');
        if (AutoWallpaper) {
            const wallpaper_var = themes.find(({ theme_wallpaper }) => theme_wallpaper === AutoWallpaper);
            Utils.execAsync(`swww img ${backgrounds}/${AutoWallpaper} --transition-step 4 -f CatmullRom --transition-fps 120`);
            Utils.execAsync(`cp ${backgrounds}/${AutoWallpaper} ${backgrounds}/last/image.png`);
            Utils.subprocess(
                ['sh', '-c', '~/.dots/ags/prepare_background.sh'], 
                (output) => print(output),
                (err) => logError(err),
              );
            return wallpaper_var;
        } else {
            return null;
        }
    } 
}

export default new ThemeService();
