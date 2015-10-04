# yoga3-modeswitch
*With code from <https://github.com/malept/yoga-modeswitch>*

Note: It is built initially for the Lenovo Yoga 3, but does work with any device. See more under Configuration

This small piece of code is for switching between the different modes of a 360° Convertible: Laptop, Stand and Tablet mode. It deactivates the Keyboard, Touchpad and rotates your screen.

Unfortunately it does not read data from the the built-in sensors, because it was not possible for me to fetch data from them. If you know how to get the sensors going under a Lenovo Yoga 3, please contact me.

## Installation (optional)
If you want to have it in your Applications bar, modify the .desktop file (replace PATH-TO-FILE) and copy it to one of the following locations:
> These files usually reside in `/usr/share/applications` or `/usr/local/share/applications` for applications installed system-wide, or `~/.local/share/applications` for user-specific applications. User entries take precedence over system entries. (Source: [wiki.archlinux.org](https://wiki.archlinux.org/index.php/Desktop_entries))

You can also search an icon for the .desktop file. See more in the [Desktop Entry Specification](http://standards.freedesktop.org/desktop-entry-spec/latest/).

## Configuration
This small piece of code is designed for the Lenovo Yoga 3. Nevertheless you can use it with any device, just type `xinput list` in your terminal, identify your touchpad and keyboard and modify the value of `TOUCHPAD` and `KEYBOARD` in yoga_switch.py.

## Use
### Via terminal
`python2 yoga_switch.py *mode*`

Possible modes are: normal, stand, tablet. If you do not use a mode, it switches: normal -> stand -> tablet

### Via application menu
It switches between normal -> stand -> tablet

### Modes
* **normal** Touchpad and Keyboard are enabled, screen is rotated normal
* **stand** Touchpad and Keyboard are disabled, screen is rotated 180 degree
* **tablet** Touchpad and Keyboard are disabled, screen is rotated normal
