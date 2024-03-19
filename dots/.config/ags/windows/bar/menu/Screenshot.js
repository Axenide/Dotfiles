export default function() {
  const Screenshot = Widget.Box({
    className: 'screenshot menu',
    vertical: true,
    spacing: 8,
    children: [
      Widget.Button({
        className: 'slider',
        value: BrightnessService.bind('screen-value'),
        onChange: ({ value }) => BrightnessService.screenValue = value,
        drawValue: false,
        vexpand: true,
        vertical: true,
        inverted: true
      }),
      Widget.Label({
        className: 'icon',
        label: ' '
      })
    ]
  })

  return Widget.Box({
    className: 'system_controls menu',
    children: [
      Brightness
    ]
  })
}
