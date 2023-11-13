const resource = file => `resource:///com/github/Aylur/ags/${file}.js`;
const require = async file => (await import(resource(file))).default;
const service = async file => (await require(`service/${file}`));

export const App = await require('app');
export const Widget = await require('widget');
export const Service = await require('service');
export const Variable = await require('variable');
export const Utils = await import(resource('utils'));

export const Applications = await service('applications');
export const Audio = await service('audio');
export const Battery = await service('battery');
export const Bluetooth = await service('bluetooth');
export const Hyprland = await service('hyprland');
export const Mpris = await service('mpris');
export const Network = await service('network');
export const Notifications = await service('notifications');
export const SystemTray = await service('systemtray');
