# Beep keyboard NVDA Add-on #
This add-on allows the user to configure NVDA to beeps with some keyboard events.

Copyright (C) 2019 David CM <dhf360@gmail.com>

This package is distributed under the terms of the GNU General Public License, version 2 or later.

## Features
  This add-on provides the following features you can use to adapt NVDA keyboard behavior:

* Beep for uppercases  when caps lock is on: if this feature is enabled, NVDA will beep when you typing an uppercase and caps lock is on. Don't make any more uppercase mistakes!
* Beep for typed characters when shift is pressed: with this feature NVDA will beep if you type a character with shift key pressed.
* Beep for toggle keys changes: with this feature, NVDA will beep higher if a toggle key goes on, and lower tone if it goes off.
* Announce toggle keys changes: just when "Beep for toggle keys changes" is on. You can enable or disable NVDA to announce toggle key status.

## Requirements
  You need NVDA 2018.2 or later.

## Installation
  Just install it as a NVDA add-on.

## Usage
  To enable or disable features, go to NVDA settings and select beep keyboard category. In that category you can configure all  supported features by this add-on.  
  "Beep for uppercases  when caps lock is on" is enabled by default.

## Packaging it for distribution
  Open a command line, change to the Add-on root folder  and run the scons command. The created add-on, if there were no errors, is placed in the root directory.

## Notes
* scons and gettext tools on this project are  compatible with python 3 only. Doesn't work with python 2.7.