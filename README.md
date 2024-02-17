<h1 align="center">✨ Dotfiles</h1>

<p align="center">
    <i>These are my configuration files also known as <b>dotfiles</b>.</i>
<table align="center">
  <tr>
    <td colspan="2" align="center"><img src="screenshots/0.png"></td>
  </tr>
  <tr>
    <td align="center"><img src="screenshots/1.png"></td>
    <td align="center"><img src="screenshots/2.png"></td>
  </tr>
</table>
</p>

> [!CAUTION]
> This setup is specific for [Hyprland](https://github.com/hyprwm/Hyprland). Dont install it if you don't know what you're doing.

## Installation
```bash
git clone https://github.com/Axenide/Dotfiles
cd Dotfiles
./dots.sh
```
This will execute the installation wizard.

> [!NOTE]
> This packages are needed to fully use the config and will be installed if you choose the option in script:
```
adw-gtk3 alsa-utils awesome-terminal-fonts brightnessctl btop cava firefox fish floorp-bin grim grimblast-git hyprland hyprpicker-git hyprshade imv kitty kooha ly nemo nemo-audio-tab nemo-emblems nemo-fileroller nemo-image-converter nemo-pastebin nemo-share neofetch neovim otf-font-awesome pamixer pavucontrol ranger rofi-calc rofi-lbonn-wayland rofimoji slurp starship stow swaylock-effects-git swaync swayosd-git thefuck tmux ttf-all-the-icons ttf-font-awesome waybar wl-clip-persist-git wl-clipboard wtype xdg-desktop-portal-hyprland xdg-user-dirs-gtk xdg-utils xfce-polkit zathura zathura-cb zathura-djvu zathura-pdf-mupdf zathura-ps
```
Also it will install `yay`, but you can skip the installation and use any AUR helper you want and install them manually. 

## 💥 Rofi
<b>
<table align="center">
  <tr>
    <td align="center">App Launcher</td>
  </tr>
  <tr>
    <td align="center"><img src="screenshots/rofi/launcher.png"><br><kbd>SUPER + R</kbd></td>
  </tr>
  <tr>
    <td align="center">Power Menu</td>
  </tr>
  <tr>
    <td align="center"><img src="screenshots/rofi/powermenu.png"><br><kbd>SUPER + Escape</kbd></td>
  </tr>
  <tr>
    <td align="center">Emojis</td>
  </tr>
  <tr>
    <td align="center"><img src="screenshots/rofi/emoji.png"><br><kbd>SUPER + .</kbd></td>
  </tr>
  <tr>
    <td align="center">Wallpaper Changer</td>
  </tr>
  <tr>
    <td align="center"><img src="screenshots/rofi/wallpaper.png"><br><kbd>SUPER + ,</kbd></td>
  </tr>
  <tr>
    <td align="center">Tmux Session Manager</td>
  </tr>
  <tr>
    <td align="center"><img src="screenshots/rofi/tmux.png"><br><kbd>SUPER + T</kbd></td>
  </tr>
  <tr>
    <td align="center">Sound Manager</td>
  </tr>
  <tr>
    <td align="center"><img src="screenshots/rofi/sound.png"><br><kbd>SUPER + V</kbd></td>
  </tr>
  <tr>
    <td align="center">Notes</td>
  </tr>
  <tr>
    <td align="center"><img src="screenshots/rofi/notes.png"><br><kbd>SUPER + N</kbd></td>
  </tr>
  <tr>
    <td align="center">To-Do</td>
  </tr>
  <tr>
    <td align="center"><img src="screenshots/rofi/todo.png"><br><kbd>SUPER + Q</kbd></td>
  </tr>
  <tr>
    <td align="center">Bluetooth</td>
  </tr>
  <tr>
    <td align="center"><img src="screenshots/rofi/bluetooth.png"><br><kbd>SUPER + B</kbd></td>
  </tr>
  <tr>
    <td align="center">Networks</td>
  </tr>
  <tr>
    <td align="center"><img src="screenshots/rofi/networks.png"><br><kbd>SUPER + D</kbd></td>
  </tr>
  <tr>
    <td align="center">Keepmenu</td>
  </tr>
  <tr>
    <td align="center"><img src="screenshots/rofi/keepmenu.png"><br><kbd>SUPER + U</kbd></td>
  </tr>
  <tr>
    <td align="center">Calendar</td>
  </tr>
  <tr>
    <td align="center"><img src="screenshots/rofi/calendar.png"><br><kbd>SUPER + C</kbd></td>
  </tr>
</table>
</b>

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
| <kbd>SUPER + E</kbd>                                  | File explorer                   |
| <kbd>SUPER + SHIFT + E</kbd>                          | Floating file explorer          |
| <kbd>SUPER + W</kbd>                                  | Floorp                          |
| <kbd>SUPER + SHIFT + W</kbd>                          | Private Floorp                  |
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

## 🌐 Browser Theme
### Floorp
I'm currently using Floorp, a Firefox ESR fork with a sidebar and a lot of customization options.

I tweaked some details with CSS and used [Firefox Color](https://addons.mozilla.org/es/firefox/addon/firefox-color/) to recolor it.

[Click here to get my theme](https://color.firefox.com/?theme=XQAAAAKcAQAAAAAAAABBqYhm849SCia73laEGccwS-xMDPrv2Sw6Caq-qy5QgqeHG4K15QdnKP13g2bqt8iOj4e4VN6fpUJ5Y-FzVYxdRh4Jahskc87JAlD7QBtVsQPah1lEVOrnQjk3fT6hspa42dQuogENOnAprj5_ike7fU8X50TCyvscVMl171BNW9KlAwx9YXTNFIe88acOqVJdFP3RkU0w-83gHO2TCPgp6u3Rj6XNlZo5kGZp5XVxUhBxMUeEyKqrvWVVCE6HxKDOaQmyU6HCP6gxuQcEMxGY0p-irKqZzYgd_-6pswA) or make your own!

### Firefox
If you want, you can use my custom CSS. An automated script for this is included in the root folder of this repository as `firefox.sh`. You will also be asked if you want to use my config when running `dots.sh`.

### Chromium
I made a custom theme that you can use on any Chromium based browser. You have to add it via developer mode on your extensions settings. I really like Brave, but you can use it on every Chromium browser (except Opera for some reason).

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
