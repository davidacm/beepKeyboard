# -*- coding: UTF-8 -*-
# Copyright (C) 2024 David CM, released under the GPL.
# Author: David CM <dhf360@gmail.com>.

import sys, os, wx, gui, addonHandler

addonDir = os.path.abspath(os.path.join(os.path.dirname(__file__), "globalPlugins", "beepKeyboard"))
sys.path.append(addonDir)
from beepKeyboardUtils import showDonationsDialog
sys.path.remove(sys.path[-1])

addonHandler.initTranslation()


DONATE_METHODS = (
	{
		'label': _('Using Paypal'),
		'url': 'https://paypal.me/davicm'
	},
	{
		'label': _('using Co-fi'),
		'url': 'https://ko-fi.com/davidacm'
	},
	{
		'label': _('See more methods on my github Page'),
		'url': 'https://davidacm.github.io/donations/'
	}
)


def onInstall():
	gui.mainFrame.prePopup()
	wx.CallAfter(showDonationsDialog, gui.mainFrame, "Beep Keyboard", DONATE_METHODS)
	gui.mainFrame.postPopup()
