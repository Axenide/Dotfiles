import GLib from 'gi://GLib';

const Home = GLib.get_home_dir();

const misc = {
    wm_gaps: 3,
    radii: 10,
    spacing: 9,
    font_size: 16,
    border_width: 0,
    shadow: 'rgba(0, 0, 0, 0)',
    drop_shadow: false,
    transition: 400,
    screen_corners: false,
    bar_style: 'floating',
    layout: 'topbar',
    desktop_clock: 'center center',
    font: 'Ubuntu Nerd Font',
    mono_font: 'Mononoki Nerd Font',
};

const light = {
    color_scheme: 'light',
    red: '#f66151',
    green: '#57e389',
    yellow: '#f6d32d',
    blue: '#fff',
    magenta: '#c061cb',
    teal: '#5bc8aF',
    orange: '#ffa348',
    bg_color: '#fffffa',
    fg_color: '#141414',
    hover_fg: '#0a0a0a',
    border_color: '#476C43',
};

const gruv_dark = {
    
    //colors
    color_scheme: 'gruv_dark',
    red: '#CC241D',
    green: '#476C43',
    yellow: '#D79921',
    blue: '#458588',
    magenta: '#B16286',
    teal: '#689D6A',
    orange: '#D65D0E',
    bg_color: '#1D2021',
    fg_color: '#FBF1C7',
    hover_fg: '#f1f1f1',

    //settings
    wallpaper_fg: 'white',
    hypr_active_border: 'rgba(476C43FF)',
    hypr_inactive_border: 'rgba(3f3f3fDD)',
    accent: '$blue',
    accent_fg: '$bg_color',
    widget_bg: '$fg_color',
    widget_opacity: 94,
    active_gradient: 'to right, $accent, lighten($accent, 25%)',
    border_color: '$yellow',
    bar_border_color: '$green',
    border_opacity: 100,

    //misc
    avatar: '~/face.png',
    name: 'gruvbox_dark_theme',
    icon: '󰄛',
    gtk_theme: 'Gruvbox-Dark-B',
    icons: 'gruvbox_icons',
    pywall_theme: 'base16-gruvbox-hard',
    theme_wallpaper: 'stairs.png',
    //workspace_button_size: '16',

    //includes...
    ...misc,
};

const gruv_darktooth = {

    //colors
    color_scheme: 'gruv_darktooth',
    red: '#FB543F',
    green: '#95C085',
    yellow: '#FAC03B',
    blue: '#0D6678',
    magenta: '#8F4673',
    teal: '#8BA59B',
    orange: '#D65D0E',
    bg_color: '#1D2021',
    fg_color: '#FDF4C1',
    hover_fg: '#FDF4C1',

    //settings
    wallpaper_fg: 'white',
    hypr_active_border: 'rgba(95C085FF)',
    hypr_inactive_border: 'rgba(1D2021DD)',
    accent: '$blue',
    accent_fg: '$bg_color',
    widget_bg: '$fg_color',
    widget_opacity: 94,
    active_gradient: 'to right, $accent, lighten($accent, 25%)',
    border_color: '$yellow',
    bar_border_color: '$green',
    border_opacity: 100,

    //misc
    avatar: '~/face.png',
    name: 'gruvbox_darktooth_theme',
    icon: '󰄛',
    gtk_theme: 'Gruvbox-Dark-B',
    icons: 'gruvbox_icons',
    pywall_theme: 'base16-gruvbox-hard',
    theme_wallpaper: 'gruvbox_forest-4.png',
    //workspace_button_size: '16',

    //includes...
    ...misc,
};


const pico = {

    //colors
    color_scheme: 'pico',
    red: '#FF004D',
    green: '#00E756',
    yellow: '#FFF024',
    blue: '#29ADFF',
    magenta: '#FF77A8',
    teal: '#83769C',
    orange: '#D08770',
    bg_color: '#000000',
    fg_color: '#FFF1E8',
    hover_fg: '#FFF1E8',

    //settings
    wallpaper_fg: 'white',
    hypr_active_border: 'rgba(29ADFFFF)',
    hypr_inactive_border: 'rgba(545862DD)',
    accent: '$teal',
    accent_fg: '$bg_color',
    widget_bg: '$fg_color',
    widget_opacity: 94,
    active_gradient: 'to right, $accent, lighten($accent, 25%)',
    border_color: '$blue',
    bar_border_color: '$blue',
    border_opacity: 100,

    //misc
    avatar: '~/face.png',
    name: 'pico_theme',
    icon: '󰄛',
    gtk_theme: 'adw-gtk3-dark',
    icons: 'pico_icons',
    pywall_theme: 'base16-seti',
    theme_wallpaper: 'color_city.png',
    //workspace_button_size: '16',

    //includes...
    ...misc,
};

const catppuccin_mocha = {

    //colors
    color_scheme: 'catppuccin_mocha',
    red: '#F38BA8',
    green: '#A6E3A1',
    yellow: '#F9E2AF',
    blue: '#89B4FA',
    magenta: '#CBA6F7',
    teal: '#94E2D5',
    orange: '#FAB387',
    bg_color: '#181825',
    fg_color: '#CDD6F4',
    hover_fg: '#CDD6F4',

    //settings
    wallpaper_fg: 'white',
    hypr_active_border: 'rgba(CBA6F7FF)',
    hypr_inactive_border: 'rgba(1E1E2EDD)',
    accent: '$teal',
    accent_fg: '$bg_color',
    widget_bg: '$fg_color',
    widget_opacity: 94,
    active_gradient: 'to right, $accent, lighten($accent, 25%)',
    border_color: '$blue',
    bar_border_color: '$blue',
    border_opacity: 100,

    //misc
    avatar: '~/face.png',
    name: 'catppuccin_mocha_theme',
    icon: '󰄛',
    gtk_theme: 'Catppuccin_Mocha',
    icons: 'catppuccin_mocha',
    pywall_theme: 'base16-seti',
    theme_wallpaper: 'oled-mountains.jpg',
    //workspace_button_size: '16',

    //includes...
    ...misc,
};

const material_dark = {

    //colors
    color_scheme: 'material_dark',
    red: '#F07178',
    green: '#C3E88D',
    yellow: '#FFCB6B',
    blue: '#82AAFF',
    magenta: '#C792EA',
    teal: '#89DDFF',
    orange: '#D65D0E',
    bg_color: '#212121',
    fg_color: '#EEFFFF',
    hover_fg: '#EEFFFF',

    //settings
    wallpaper_fg: 'white',
    hypr_active_border: 'rgba(C792EAFF)',
    hypr_inactive_border: 'rgba(4A4A4ADD)',
    accent: '$blue',
    accent_fg: '$bg_color',
    widget_bg: '$fg_color',
    widget_opacity: 94,
    active_gradient: 'to right, $accent, lighten($accent, 25%)',
    border_color: '$blue',
    bar_border_color: '$blue',
    border_opacity: 100,

    //misc
    avatar: '~/face.png',
    name: 'material_dark_theme',
    icon: '󰄛',
    gtk_theme: 'material',
    icons: 'material',
    pywall_theme: 'base16-materialer',
    theme_wallpaper: 'japanese-sakura-painting.jpg',
    //workspace_button_size: '16',

    //includes...
    ...misc,
};

const nord = {

    //colors
    color_scheme: 'nord',
    red: '#BF616A',
    green: '#A3BE8C',
    yellow: '#EBCB8B',
    blue: '#5E81AC',
    magenta: '#88C0D0',
    teal: '#8FBCBB',
    orange: '#D08770',
    bg_color: '#272b35',
    fg_color: '#E5E9F0',
    hover_fg: '#E5E9F0',

    //settings
    wallpaper_fg: 'white',
    hypr_active_border: 'rgba(5E81ACFF)',
    hypr_inactive_border: 'rgba(4C566ADD)',
    accent: '$teal',
    accent_fg: '$bg_color',
    widget_bg: '$fg_color',
    widget_opacity: 94,
    active_gradient: 'to right, $accent, lighten($accent, 25%)',
    border_color: '$blue',
    bar_border_color: '$blue',
    border_opacity: 100,

    //misc
    avatar: '~/face.png',
    name: 'nord_theme',
    icon: '󰄛',
    gtk_theme: 'Adwaita-dark-nord',
    icons: 'nord_icons',
    pywall_theme: 'base16-nord',
    theme_wallpaper: 'nord.jpg',
    //workspace_button_size: '16',

    //includes...
    ...misc,
}

const tokyo_night = {

    //colors
    color_scheme: 'tokyo_night',
    red: '#F7768E',
    green: '#9ECE6A',
    yellow: '#D0D040',
    blue: '#7AA2F7',
    magenta: '#BB9AF7',
    teal: '#7DCFFF',
    orange: '#E0AF68',
    bg_color: '#24283B',
    fg_color: '#B5BFE8',
    hover_fg: '#B5BFE8',

    //settings
    wallpaper_fg: 'white',
    hypr_active_border: 'rgba(BB9AF7FF)',
    hypr_inactive_border: 'rgba(24283BDD)',
    accent: '$blue',
    accent_fg: '$bg_color',
    widget_bg: '$fg_color',
    widget_opacity: 94,
    active_gradient: 'to right, $accent, lighten($accent, 25%)',
    border_color: '$magenta',
    bar_border_color: '$magenta',
    border_opacity: 100,

    //misc
    avatar: '~/face.png',
    name: 'tokyo_night_theme',
    icon: '󰄛',
    gtk_theme: 'Tokyonight',
    icons: 'tokyo_night',
    pywall_theme: 'base16-tomorrow-night',
    theme_wallpaper: 'nord-street.png',
    //workspace_button_size: '16',

    //includes...
    ...misc,
};

const adwaita = {

    //colors
    color_scheme: 'adwaita',
    red: '#c01c28',
    green: '#2ec27e',
    yellow: '#f5c211',
    blue: '#3584e4',
    magenta: '#813d9c',
    teal: '#99c1f1',
    orange: '#e66100',
    bg_color: '#1E1E1E',
    fg_color: '#deddda',
    hover_fg: '#c0bfbc',

    //settings
    wallpaper_fg: 'white',
    hypr_active_border: 'rgba(3584e4FF)',
    hypr_inactive_border: 'rgba(241f31DD)',
    accent: '$blue',
    accent_fg: '$bg_color',
    widget_bg: '$fg_color',
    widget_opacity: 94,
    active_gradient: 'to right, $accent, lighten($accent, 25%)',
    border_color: '$magenta',
    bar_border_color: '$blue',
    border_opacity: 100,

    //misc
    avatar: `${Home}/face.png`,
    name: 'adwaita_theme',
    icon: '󰄛',
    gtk_theme: 'adw-gtk3-dark',
    icons: 'Adwaita',
    pywall_theme: 'base16-default',
    theme_wallpaper: 'waves_dark.jpg',
    //workspace_button_size: '16',

    //includes...
    ...misc,
}

export default [
    gruv_dark,
    gruv_darktooth,
    pico,
    catppuccin_mocha,
    material_dark,
    nord,
    tokyo_night,
    adwaita
];
