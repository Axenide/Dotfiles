<h1 align="center">✨ Dotfiles</h1>

<p align="center">
    <i>These are my configuration files also known as <b>dotfiles</b>.</i>
<img src="screenshots/cover.png">
</p>

> [!CAUTION]
> This setup is specific for [Hyprland](https://github.com/hyprwm/Hyprland). Dont install it if you don't know what you're doing.

<details>
<summary><i>
📸 Screenshots
</i></summary>
<img src="screenshots/0.png">
<img src="screenshots/1.png">
<img src="screenshots/2.png">
</details>

## Installation
```bash
git clone --recurse-submodules https://github.com/Axenide/Dotfiles
cd Dotfiles
./dots.sh
```
This will install the config for the system. For example, selecting NVIDIA will add the correct environment variables to the Hyprland config.

> [!NOTE]
> This won't install the needed packages. That's a WIP.

## 💥 Rofi
<details>
  <summary>App Launcher</summary>
    <br>
  <img src="screenshots/rofi/launcher.png">
</details>

<details>
  <summary>Power Menu</summary>
    <br>
  <img src="screenshots/rofi/powermenu.png">
</details>

<details>
  <summary>Emojis</summary>
    <br>
  <img src="screenshots/rofi/emoji.png">
</details>

<details>
  <summary>Wallpaper Changer</summary>
    <br>
  <img src="screenshots/rofi/wallpaper.png">
</details>

<details>
  <summary>Tmux Session Manager</summary>
    <br>
  <img src="screenshots/rofi/tmux.png">
</details>

<details>
  <summary>Sound Manager</summary>
    <br>
  <img src="screenshots/rofi/volume.png">
</details>

<details>
  <summary>Notes</summary>
    <br>
  <img src="screenshots/rofi/notes.png">
</details>

<details>
  <summary>To-Do</summary>
    <br>
  <img src="screenshots/rofi/todo.png">
</details>

<details>
  <summary>Bluetooth</summary>
    <br>
  <img src="screenshots/rofi/bluetooth.png">
</details>

<details>
  <summary>Network</summary>
    <br>
  <img src="screenshots/rofi/network.png">
</details>

## ⌨️ Keybindings

### Hyprland

| Keys                                         | Action                          |
|---------------------------------------------:|:--------------------------------|
| <kbd>SUPER + C</kbd>                                  | Close window                    |
| <kbd>SUPER + SHIFT + Escape</kbd>                     | Exit Hyprland                   |
| <kbd>SUPER + SHIFT + B</kbd>                                  | Toggle Waybar                     |
| <kbd>SUPER + ALT + B</kbd>                            | Restart Waybar                  |
| <kbd>SUPER + Space</kbd>                              | Toggle tiled/floating           |
| <kbd>SUPER + P</kbd>                                  | Toggle pseudo-tiling            |
| <kbd>SUPER + D</kbd>                                  | Toggle split                    |
| <kbd>SUPER + F</kbd>                                  | Fullscreen                      |
| <kbd>SUPER + SHIFT + F</kbd>                          | Fake Fullscreen                 |
| <kbd>SUPER + CTRL + F</kbd>                            | Maximize                        |
| <kbd>SUPER + Y</kbd>                                  | Pin window                      |
| <kbd>SUPER + G</kbd>                                  | Center window                   |
| <kbd>SUPER + Arrows or H,J,K,L</kbd>                  | Move window focus               |
| <kbd>SUPER + SHIFT + Arrows or H,J,K,L</kbd>          | Move tiled window               |
| <kbd>SUPER + CTRL + Arrows or H,J,K,L</kbd>        | Resize window                   |
| <kbd>SUPER + ALT + Arrows or H,J,K,L</kbd>            | Move floating window            |
| <kbd>SUPER + [1-9][0]</kbd>                           | Change workspace [1-10]         |
| <kbd>SUPER + SHIFT + [1-9][0]</kbd>                   | Move window to workspace [1-10] |
| <kbd>SUPER + Z</kbd>                                  | Go to previous workspace        |
| <kbd>SUPER + SHIFT + Z</kbd><br><kbd>SUPER + Scroll Down</kbd> | Go to previous active workspace |
| <kbd>SUPER + X</kbd>                                  | Go to next workspace            |
| <kbd>SUPER + SHIFT + X</kbd><br><kbd>SUPER + Scroll Up</kbd>   | Go to next active workspace     |
| <kbd>SUPER + Left Click</kbd>                         | Drag window                     |
| <kbd>SUPER + Right Click</kbd>                        | Drag resize window              |

### Programs

| Keys                                         | Action                          |
|---------------------------------------------:|:--------------------------------|
| <kbd>SUPER + RETURN</kbd>                             | Open Kitty terminal             |
| <kbd>SUPER + SHIFT + RETURN</kbd>                     | Open floating Kitty terminal    |
| <kbd>SUPER + ALT + RETURN</kbd>                       | Open Kitty with slurp           |
| <kbd>SUPER + T</kbd>                                  | Tmux Session Manager            |
| <kbd>SUPER + E</kbd>                                  | File explorer                   |
| <kbd>SUPER + SHIFT + E</kbd>                          | Floating file explorer          |
| <kbd>SUPER + W</kbd>                                  | Brave Nightly                   |
| <kbd>SUPER + SHIFT + W</kbd>                          | Incognito Brave Nightly         |
| <kbd>SUPER + R</kbd>                                  | App Launcher                    |
| <kbd>SUPER + Escape</kbd>                             | Powermenu                       |
| <kbd>SUPER + .</kbd>                                  | Emojis                          |
| <kbd>SUPER + ,</kbd>                                  | Wallpaper Selector              |
| <kbd>SUPER + V</kbd>                                  | Sound Manager                   |
| <kbd>SUPER + N</kbd>                                  | Notes                           |
| <kbd>SUPER + Q</kbd>                                  | To-Do                           |
| <kbd>SUPER + M</kbd>                                  | Calculator                      |
| <kbd>SUPER + B</kbd>                                  | Bluetooth                       |
| <kbd>SUPER + D</kbd>                                  | Networks                        |
| <kbd>Print</kbd>                                      | Save and copy screenshot        |
| <kbd>SHIFT + Print</kbd>                              | Copy screenshot                 |
| <kbd>SUPER + S</kbd>                                  | Save and copy area screenshot   |
| <kbd>SUPER + SHIFT + S</kbd>                          | Copy area screenshot            |
| <kbd>SUPER + A</kbd>                                  | Toggle notification center      |

### Tmux

> [!IMPORTANT]
> **PREFIX** is set to <kbd>CTRL + Space</kbd>

| Keys                | Action                          |
|--------------------:|:--------------------------------|
| <kbd>PREFIX + c</kbd>        | Create window                   |
| <kbd>SHIFT + ALT + H,L</kbd> | Navigate windows                |
| <kbd>PREFIX + [1-9]</kbd>    | Change to window from 1 to 9    |
| <kbd>PREFIX + &</kbd>        | Kill window                     |
| <kbd>PREFIX + /</kbd>        | Vertical split                  |
| <kbd>PREFIX + -</kbd>        | Horizontal split                |
| <kbd>CTRL + H,J,K,L</kbd>    | Navigate panes                  |
| <kbd>PREFIX + { or }</kbd>   | Swap pane position              |
| <kbd>PREFIX + q</kbd>        | Go to pane pressing a number    |
| <kbd>PREFIX + x</kbd>        | Kill pane                       |
| <kbd>PREFIX + s</kbd>        | List sessions                   |
| <kbd>PREFIX + w</kbd>        | List windows                    |
| <kbd>PREFIX + [</kbd>        | Yank mode (copy)                |
| <kbd>v</kbd>                 | Start selection                 |
| <kbd>CTRL + v</kbd>          | Toggle rectangle/line selection |
| <kbd>y</kbd>                 | Yank selection                  |

<p align="center">
<samp>
  <i>Please consider giving me a tip. :)</i>
  <br>
  <sup>
    <b>
    <a href="https://cafecito.app/axenide">☕ Cafecito</a> |
    <a href="https://ko-fi.com/axenide">❤️ Ko-Fi</a> |
    <a href="https://paypal.me/Axenide">💸 PayPal</a>
    </b>
    <br>
    <b>💵 USDT:</b> <i>TDub4eGEbXMqv4CFo65oNTaBYMJpbJyrtQ</i> (TRC20)
    <br>
    <b>💶 USDC:</b> <i>0x1959681e522dbaedd93f90b0ece0d627f96432ee</i> (ERC20)
    <br>
    <b>🪙 BTC:</b> <i>16BTDDEmE2D98YPePt6VAvsC4s9xrVLpk4</i>
  </sup>
</samp>
</p>
