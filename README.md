# Installation and configuration Manual

## Required Hardware
* Raspberry Pi (2 or 3)
* HDMI cable
* Monitor or TV with HDMI input
* Numeric keyboard

## Required Software
*   Raspbian OS
*   ProSeeDure program
*   evince - PDF reader
    
    `sudo apt-get install evince`
*   xbindkeys
    
    `sudo apt-get install xbindkeys && xbindkeys-config`
*   remove mouse cursor
    
    `sudo apt-get install unclutter`

## Configuration
* Set a program to always run in full screen

`sudo leafpad /home/pi/.config/openbox/lxde*.xml`

```xml
<application name="lxterminal">
    <focus>yes</focus> # Ensure that keyboard directly working on the application
    <fullscreen>yes</fullscreen> # Set to always run on full screen
</application>
```

* Hide mouse cursor
```bash
unclutter -display :0 -noevents -grab
```

* Attaching events on selected keys - Xbindkeys-config

`*` key runs the program
```bash
lxterminal --command 'sh /home/pi/milara/autorun.sh'
```
`/` key clears the screen
```bash
sudo killall evince lxterminal
```