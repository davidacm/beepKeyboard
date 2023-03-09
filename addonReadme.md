# Beep keyboard NVDA Add-on #
This add-on allows the user to configure NVDA to beeps with some keyboard events.

Copyright (C) 2019 - 2023 David CM <dhf360@gmail.com>

This package is distributed under the terms of the GNU General Public License, version 2 or later.

## Features
  This add-on provides the following features you can use to adapt NVDA keyboard behavior:

* Beep for uppercases  when caps lock is on: if this feature is enabled, NVDA will beep when you typing an uppercase and caps lock is on. Don't make any more uppercase mistakes!
* Beep for typed characters when shift is pressed: with this feature NVDA will beep if you type a character with shift key pressed.
* Beep for toggle keys changes: with this feature, NVDA will beep higher if a toggle key goes on, and lower tone if it goes off. Please note that Windows has a toggle keis beep function built-in on Ease of Access Center. This native feature works well if you don't use laptop keyboard layout setting.
* Announce toggle keys changes: just when "Beep for toggle keys changes" is on. You can enable or disable NVDA to announce toggle key status.
* Beep for specified characters: NVDA will beep for all characters that you set in advanced settings.
* Disable beeping on password fields: this feature is enabled by default to aboid security risks. Disable it if you want to hear beeps on password fields.
## Requirements
  You need NVDA 2018.2 or later.

## Installation
  Just install it as a NVDA add-on.

## Usage
  To enable or disable features, go to NVDA settings and select beep keyboard category. In that category you can configure all  supported features by this add-on.  
  "Beep for uppercases  when caps lock is on" is enabled by default. 
  If you need more settings, open the advanced settings dialog that contains the following options:

* Ignored characters with shift pressed: all characters here will be ignored to beeping when shift is pressed. Escape Sequences are allowed, e.g. "\t" for tab, "\r" for carriage return.
* Beep always for the following characters: set here all characters that you want NVDA beeps for. Escape Sequences are allowed, e.g. "\t" for tab, "\r" for carriage return.
* Select tone to configure: you can configure parameters for all tones. Select one here, and set the parameters in the next text boxes. When change selection, NVDA will beep for the current selected tone with the current parameters set in the dialog.
* Tone pitch: tone pitch for the current selected tone.
* Tone length: tone length for the current selected tone.
* Tone volume: tone volume for the current selected tone.
* Test tone: this button lets you to play a test with the current set parameters.
* Press OK button to save settings or cancel to discard.

## contributions, reports and donations

If you like my project or this software is useful for you in your daily life and you would like to contribute in some way, you can donate via the following methods:

* [PayPal.](https://paypal.me/davicm)
* [Ko-fi.](https://ko-fi.com/davidacm)
* [cryptocurrencies and other methods.](https://davidacm.github.io/donations/)

If you want to fix bugs, report problems or new features, you can contact me at: <dhf360@gmail.com>.

  Or in the github repository of this project:
  [Beep keyboard on GitHub](https://github.com/davidacm/beepKeyboard)

    You can get the latest release of this add-on in that repository.
