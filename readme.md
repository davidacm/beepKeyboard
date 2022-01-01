# Beep keyboard NVDA Add-on #
This add-on allows the user to configure NVDA to beeps with some keyboard events.

Copyright (C) 2019 David CM <dhf360@gmail.com>

This package is distributed under the terms of the GNU General Public License, version 2 or later.

## Download.
 The latest release is available to [download in this link](https://davidacm.github.io/getlatest/gh/davidacm/beepKeyboard)

# Contributing with the project.
### Donations.
  If you like my project or this software is useful for you in your daily life and you would like to contribute in some way, you can donate via the following methods.
  
* [PayPal.](https://paypal.me/davicm)
* [Ko-fi.](https://ko-fi.com/davidacm)
* [cryptocurrencies and other methods.](https://davidacm.github.io/donations/)


### fixing bugs and new features.
  If you want to fix a bug or add new feature, You will need to fork this repository.

  #### Forking the repository.
  If this is your first contribution, you will first need to "fork" the BeepKeyboard repository on GitHub:

  1. Fork this repo in your github account.
  2. Clone your forked repo locally: "git clone yourRepoUrl".
  3. Add this repo in your forked repo from the command line:  
  "git remote add davidacm https://github.com/davidacm/beepKeyboard.git".
  4. fetch my branches:  
  "git fetch davidacm".
  5. Switch to the local master branch: "git checkout master".
  6. Set the local master to use the davidacm  master as its upstream:  
  "git branch -u davidacm/master".  

#### Steps before coding.
  You must use a separate "topic" branch for each issue or feature. All code should usually be based on the latest commit in the official master branch at the time you start the work.
  So, before begin to work, do the following:

  1. Remember the steps of "Forking the repository" section.
  2. Checkout to master branch: "git checkout master".
  3. Update the local master: "git pull".
  4. Create a new branch based on the updated master branch: "git checkout -b YourNewBranch".
  5. write your code.
  6. Add your work to be commited (clean unwanted files first): git "add ."
  7. create a commit: "git commit" and write the commit message.
  8. push your branch in your repository: "git push". if the branch doesn't exist, git will tell you how to deal with this.
  9. Request a pull request on my repository.

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
