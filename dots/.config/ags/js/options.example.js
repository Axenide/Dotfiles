import { Utils } from './imports.js';

// Run the `grep` command to check for "closed" in the file
const lidStateOutput = Utils.exec('cat /proc/acpi/button/lid/LID/state');
const isLidClosed = lidStateOutput.includes('closed');

const hyprctlOutput = JSON.parse(Utils.exec('hyprctl -j monitors'));

const monitorIdToCheck = 1; // The ID to check for

// Check if the monitor with the specified ID is in the list
const isMonitorConnected = hyprctlOutput.some(monitor => monitor.id === monitorIdToCheck);

let configuration;

console.log('Lid state output:', lidStateOutput); // Debugging
console.log('Monitor is connected:', isMonitorConnected); // Debugging

if (isLidClosed || !isMonitorConnected) {
  console.log('Lid is closed or monitor is not connected'); // Debugging
  configuration = {
    preferredMpris: 'spotify',
    workspaces: 10,
    dockItemSize: 56,
    battaryBar: {
      showPercentage: true,
      low: 20,
      medium: 50,
    },
    temperature: '/sys/class/thermal/thermal_zone0/temp',
    systemFetchInterval: 1000,
    windowAnimationDuration: 350,
    brightnessctlKBD: 'asus::kbd_backlight',
  };
} else {
  console.log('Lid is open and monitor is connected'); // Debugging
  configuration = {
    preferredMpris: 'spotify',
    workspaces: 20,
    dockItemSize: 56,
    battaryBar: {
      showPercentage: true,
      low: 20,
      medium: 50,
    },
    temperature: '/sys/class/thermal/thermal_zone0/temp',
    systemFetchInterval: 1000,
    windowAnimationDuration: 350,
    brightnessctlKBD: 'asus::kbd_backlight',
  };
}

export default configuration;
