import PanelButton from '../PanelButton.js';
import { Hyprland, Utils, Widget } from '../../imports.js';

export const ClientLabel = substitutes => Widget.Label({
    binds: [['label', Hyprland.active.client, 'class', c => substitutes
        .find(([from]) => from === c)?.[1] || c]],
});

export const ClientIcon = substitutes => Widget.Icon({
    connections: [[Hyprland.active.client, icon => {
        let classIcon = Hyprland.active.client.class;
        let titleIcon = Hyprland.active.client.title;
        substitutes.forEach(([from, to]) => {
            if (classIcon === from)
                classIcon = to;

            if (titleIcon === from)
                titleIcon = to;
        });

        classIcon += '-symbolic';
        titleIcon += '-symbolic';

        const hasTitleIcon = Utils.lookUpIcon(titleIcon);
        const hasClassIcon = Utils.lookUpIcon(classIcon);

        if (hasClassIcon)
            icon.icon = classIcon;

        if (hasTitleIcon)
            icon.icon = titleIcon;

        icon.visible = hasTitleIcon || hasClassIcon;
    }]],
});

export default () => PanelButton({
    className: 'focused-client',
    content: Widget.Box({
        children: [
            ClientIcon([
                ['transmission-gtk', 'transmission'],
                ['blueberry.py', 'bluetooth'],
                ['org.wezfurlong.wezterm', 'folder-code'],
                ['com.raggesilver.BlackBox', 'folder-code'],
                ['Caprine', 'facebook-messenger'],
                ['', 'preferences-desktop-display'],
            ]),
            ClientLabel([
                ['transmission-gtk', 'Transmission'],
                ['com.obsproject.Studio', 'OBS'],
                ['com.usebottles.bottles', 'Bottles'],
                ['com.github.wwmm.easyeffects', 'Easy Effects'],
                ['org.gnome.TextEditor', 'Text Editor'],
                ['org.gnome.design.IconLibrary', 'Icon Library'],
                ['blueberry.py', 'Blueberry'],
                ['org.wezfurlong.wezterm', 'Wezterm'],
                ['com.raggesilver.BlackBox', 'BlackBox'],
                ['firefox', 'Firefox'],
                ['org.gnome.Nautilus', 'Files'],
                ['libreoffice-writer', 'Writer'],
                ['', 'Desktop'],
            ]),
        ],
    }),
});
