# -*- coding: UTF-8 -*-
# Beep keyboard: This add-on beeps with some keyboard events.
# Copyright (C) 2019 David CM
# Author: David CM <dhf360@gmail.com>
# Released under GPL 2
#globalPlugins/capsLockBeeper.py

import config, globalPluginHandler, gui, keyboardHandler, tones, winUser, wx, addonHandler
addonHandler.initTranslation()

confspec = {
	"beepUpperWithCapsLock": "boolean(default=True)",
	"beepCharacterWithShift": "boolean(default=False)",
	"beepToggleKeyChanges": "boolean(default=False)",
	"announceToggleStatus": "boolean(default=True)"
}
config.conf.spec["beepKeyboard"] = confspec

#saves the original _reportToggleKey function
origReportToggleKey = keyboardHandler.KeyboardInputGesture._reportToggleKey
# alternate function to report state key.
def _reportToggleKey(self):
	if winUser.getKeyState(self.vkCode) & 1:
		tones.beep(2000,40)
	else: tones.beep(1000,40)
	if config.conf['beepKeyboard']['announceToggleStatus']: origReportToggleKey(self)

class BeepKeyboardSettingsPanel(gui.SettingsPanel):
	# Translators: This is the label for the beepKeyboard  settings category in NVDA Settings screen.
	title = _("Beep keyboard")

	def makeSettings(self, settingsSizer):
		sHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		# Translators: label for a checkbox option in the settings panel.
		self.beepUpperWithCapsLock = sHelper.addItem(wx.CheckBox(self, label=_("Beep for uppercases  when &caps lock is on")))
		self.beepUpperWithCapsLock.SetValue(config.conf['beepKeyboard']['beepUpperWithCapsLock'])
		# Translators: label for a checkbox option in the settings panel.
		self.beepCharacterWithShift = sHelper.addItem(wx.CheckBox(self, label=_("Beep for typed characters when &shift is pressed")))
		self.beepCharacterWithShift.SetValue(config.conf['beepKeyboard']['beepCharacterWithShift'])
		# Translators: label for a checkbox option in the settings panel.
		self.beepToggleKeyChanges = sHelper.addItem(wx.CheckBox(self, label=_("Beep for &toggle keys changes")))
		self.beepToggleKeyChanges.SetValue(config.conf['beepKeyboard']['beepToggleKeyChanges'])
		# Translators: label for a checkbox option in the settings panel.
		self.announceToggleStatus = sHelper.addItem(wx.CheckBox(self, label=_("&Announce toggle keys changes (if Beep for toggle keys changes is disabled NVDA will have the original behavior)")))
		self.announceToggleStatus.SetValue(config.conf['beepKeyboard']['announceToggleStatus'])

	def onSave(self):
		config.conf['beepKeyboard']['beepUpperWithCapsLock'] = self.beepUpperWithCapsLock.GetValue()
		config.conf['beepKeyboard']['beepCharacterWithShift'] = self.beepCharacterWithShift.GetValue()
		config.conf['beepKeyboard']['beepToggleKeyChanges'] = self.beepToggleKeyChanges.GetValue()
		config.conf['beepKeyboard']['announceToggleStatus'] = self.announceToggleStatus.GetValue()
		if hasattr(config, "post_configProfileSwitch"):
			config.post_configProfileSwitch.notify()
		else:
			config.configProfileSwitched.notify()

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def __init__(self):
		super(globalPluginHandler.GlobalPlugin, self).__init__()
		self.ignoredCharactersForShift = "\t\b\r "
		gui.settingsDialogs.NVDASettingsDialog.categoryClasses.append(BeepKeyboardSettingsPanel)
		self.setExternalReportToggleStatus(config.conf['beepKeyboard']['beepToggleKeyChanges'])
		if hasattr(config, "post_configProfileSwitch"):
			config.post_configProfileSwitch.register(self.handleConfigProfileSwitch)
		else:
			config.configProfileSwitched.register(self.handleConfigProfileSwitch)

	def event_typedCharacter(self, obj, nextHandler, ch):
		nextHandler()
		if config.conf['beepKeyboard']['beepUpperWithCapsLock'] and winUser.getKeyState(winUser.VK_CAPITAL)&1 and ch.isupper():
			tones.beep(3000,40)
		elif config.conf['beepKeyboard']['beepCharacterWithShift'] and (winUser.getKeyState(winUser.VK_LSHIFT) &32768 or winUser.getKeyState(winUser.VK_RSHIFT) &32768) and ch not in self.ignoredCharactersForShift and not (config.conf["keyboard"]["beepForLowercaseWithCapslock"] and ch.islower() and winUser.getKeyState(winUser.VK_CAPITAL)&1):
			tones.beep(6000, 10, 30, 30)

	def setExternalReportToggleStatus(self, flag):
		if flag:
			keyboardHandler.KeyboardInputGesture._reportToggleKey = _reportToggleKey
		else: keyboardHandler.KeyboardInputGesture._reportToggleKey = origReportToggleKey

	def handleConfigProfileSwitch(self):
		self.setExternalReportToggleStatus(config.conf['beepKeyboard']['beepToggleKeyChanges'])

	def terminate(self):
		super(GlobalPlugin, self).terminate()
		self.setExternalReportToggleStatus(False)
		gui.settingsDialogs.NVDASettingsDialog.categoryClasses.remove(BeepKeyboardSettingsPanel)
		if hasattr(config, "post_configProfileSwitch"):
			config.post_configProfileSwitch.unregister(self.handleConfigProfileSwitch)
		else:
			config.configProfileSwitched.unregister(self.handleConfigProfileSwitch)