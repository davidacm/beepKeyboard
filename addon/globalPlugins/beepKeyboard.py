# -*- coding: UTF-8 -*-
# Beep keyboard: This add-on beeps with some keyboard events.
# Copyright (C) 2019 David CM
# Author: David CM <dhf360@gmail.com>
# Released under GPL 2
#globalPlugins/beepKeyboard.py

import codecs, config, globalPluginHandler, gui, keyboardHandler, tones, winUser, wx, addonHandler
addonHandler.initTranslation()

confspec = {
	"beepUpperWithCapsLock": "boolean(default=True)",
	"beepCharacterWithShift": "boolean(default=False)",
	"beepToggleKeyChanges": "boolean(default=False)",
	"announceToggleStatus": "boolean(default=True)",
	"ignoredCharactersForShift": "string(default='\t\b\r ')",
	"beepForCharacters": "string(default='')",
	"shiftedCharactersPitch": "integer(default=6000)",
	"shiftedCharactersLength": "integer(default=10)",
	"shiftedCharactersVolume": "integer(default=25)",
	"customCharactersPitch": "integer(default=6000)",
	"customCharactersLength": "integer(default=10)",
	"customCharactersVolume": "integer(default=25)",
	"capsLockUpperPitch": "integer(default=3000)",
	"toggleOffPitch": "integer(default=1000)",
	"toggleOnPitch": "integer(default=2000)"
}
config.conf.spec["beepKeyboard"] = confspec

#saves the original _reportToggleKey function
origReportToggleKey = keyboardHandler.KeyboardInputGesture._reportToggleKey
# alternate function to report state key.
def _reportToggleKey(self):
	if winUser.getKeyState(self.vkCode) & 1:
		tones.beep(config.conf['beepKeyboard']['toggleOnPitch'], 40)
	else: tones.beep(config.conf['beepKeyboard']['toggleOffPitch'], 40)
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
		
		self.advancedButton = sHelper.addItem (wx.Button (self, label = _("&Open advanced options")))
		self.advancedButton.Bind(wx.EVT_BUTTON, self.onAdvanced)

	def onAdvanced(self, evt):
		advanced = AdvancedBeepKeyboardSettingsDialog(self, multiInstanceAllowed=True)
		advanced.ShowModal()

	def onSave(self):
		config.conf['beepKeyboard']['beepUpperWithCapsLock'] = self.beepUpperWithCapsLock.GetValue()
		config.conf['beepKeyboard']['beepCharacterWithShift'] = self.beepCharacterWithShift.GetValue()
		config.conf['beepKeyboard']['beepToggleKeyChanges'] = self.beepToggleKeyChanges.GetValue()
		config.conf['beepKeyboard']['announceToggleStatus'] = self.announceToggleStatus.GetValue()
		if hasattr(config, "post_configProfileSwitch"):
			config.post_configProfileSwitch.notify()
		else: config.configProfileSwitched.notify()


class AdvancedBeepKeyboardSettingsDialog(gui.SettingsDialog):
	# Translators: This is the label for the beep keyboard advanced settings dialog
	title = _("Advanced settings - Keyboard beep")

	def makeSettings(self, settingsSizer):
		sHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		# Translators: label for an edit text control option in the advanced settings dialog.
		self.ignoredCharactersForShift  = sHelper.addLabeledControl(_("Ignored characters with shift pressed"), wx.TextCtrl)
		self.ignoredCharactersForShift.SetValue(config.conf['beepKeyboard']['ignoredCharactersForShift'])
		# Translators: label for an edit text control option in the advanced settings dialog.
		self.beepForCharacters  = sHelper.addLabeledControl(_("beep always for the following characters"), wx.TextCtrl)
		self.beepForCharacters.SetValue(config.conf['beepKeyboard']['beepForCharacters'])
		# Translators: label for an edit text control option in the advanced settings dialog.
		self.shiftedCharactersPitch  = sHelper.addLabeledControl(_("shifted characters tone pitch"), wx.TextCtrl)
		self.shiftedCharactersPitch.SetValue(str(config.conf['beepKeyboard']['shiftedCharactersPitch']))
		# Translators: label for an edit text control option in the advanced settings dialog.
		self.shiftedCharactersLength  = sHelper.addLabeledControl(_("shifted characters tone length"), wx.TextCtrl)
		self.shiftedCharactersLength.SetValue(str(config.conf['beepKeyboard']['shiftedCharactersLength']))
		# Translators: label for an edit text control option in the advanced settings dialog.
		self.shiftedCharactersVolume  = sHelper.addLabeledControl(_("shifted characters tone volume"), wx.TextCtrl)
		self.shiftedCharactersVolume.SetValue(str(config.conf['beepKeyboard']['shiftedCharactersVolume']))
		# Translators: label for an edit text control option in the advanced settings dialog.
		self.customCharactersPitch  = sHelper.addLabeledControl(_("Custom characters tone pitch"), wx.TextCtrl)
		self.customCharactersPitch.SetValue(str(config.conf['beepKeyboard']['customCharactersPitch']))
		# Translators: label for an edit text control option in the advanced settings dialog.
		self.customCharactersLength  = sHelper.addLabeledControl(_("Custom characters tone length"), wx.TextCtrl)
		self.customCharactersLength.SetValue(str(config.conf['beepKeyboard']['customCharactersLength']))
		# Translators: label for an edit text control option in the advanced settings dialog.
		self.customCharactersVolume  = sHelper.addLabeledControl(_("Custom characters tone volume"), wx.TextCtrl)
		self.customCharactersVolume.SetValue(str(config.conf['beepKeyboard']['customCharactersVolume']))
		# Translators: label for an edit text control option in the advanced settings dialog.
		self.capsLockUpperPitch  = sHelper.addLabeledControl(_("Caps lock on typed characters tone pitch"), wx.TextCtrl)
		self.capsLockUpperPitch.SetValue(str(config.conf['beepKeyboard']['capsLockUpperPitch']))
		# Translators: label for an edit text control option in the advanced settings dialog.
		self.toggleOffPitch  = sHelper.addLabeledControl(_("toggle off tone pitch"), wx.TextCtrl)
		self.toggleOffPitch.SetValue(str(config.conf['beepKeyboard']['toggleOffPitch']))
		# Translators: label for an edit text control option in the advanced settings dialog.
		self.toggleOnPitch  = sHelper.addLabeledControl(_("toggle on tone pitch"), wx.TextCtrl)
		self.toggleOnPitch.SetValue(str(config.conf['beepKeyboard']['toggleOnPitch']))

	def postInit(self):
		# ensure that focus is on the ignoredCharactersForShift
		self.ignoredCharactersForShift.SetFocus()

	def onOk(self, evt):
		config.conf['beepKeyboard']['ignoredCharactersForShift'] = self.ignoredCharactersForShift.GetValue()
		config.conf['beepKeyboard']['beepForCharacters'] = self.beepForCharacters.GetValue()
		config.conf['beepKeyboard']['shiftedCharactersPitch'] = self.shiftedCharactersPitch.GetValue()
		config.conf['beepKeyboard']['shiftedCharactersLength'] = self.shiftedCharactersLength.GetValue()
		config.conf['beepKeyboard']['shiftedCharactersVolume'] = self.shiftedCharactersVolume.GetValue()
		config.conf['beepKeyboard']['customCharactersPitch'] = self.customCharactersPitch.GetValue()
		config.conf['beepKeyboard']['"customCharactersLength'] = self.customCharactersLength.GetValue()
		config.conf['beepKeyboard']['"customCharactersVolume'] = self.customCharactersVolume.GetValue()
		config.conf['beepKeyboard']['capsLockUpperPitch'] = self.capsLockUpperPitch.GetValue()
		config.conf['beepKeyboard']['toggleOffPitch'] = self.toggleOffPitch.GetValue()
		config.conf['beepKeyboard']['toggleOnPitch'] = self.toggleOnPitch.GetValue()
		if hasattr(config, "post_configProfileSwitch"):
			config.post_configProfileSwitch.notify()
		else: config.configProfileSwitched.notify()
		super(AdvancedBeepKeyboardSettingsDialog, self).onOk(evt)


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def __init__(self):
		super(globalPluginHandler.GlobalPlugin, self).__init__()
		self.handleConfigProfileSwitch()
		gui.settingsDialogs.NVDASettingsDialog.categoryClasses.append(BeepKeyboardSettingsPanel)
		if hasattr(config, "post_configProfileSwitch"):
			config.post_configProfileSwitch.register(self.handleConfigProfileSwitch)
		else:
			config.configProfileSwitched.register(self.handleConfigProfileSwitch)

	def event_typedCharacter(self, obj, nextHandler, ch):
		nextHandler()
		if config.conf['beepKeyboard']['beepUpperWithCapsLock'] and winUser.getKeyState(winUser.VK_CAPITAL)&1 and ch.isupper():
			tones.beep(config.conf['beepKeyboard']['capsLockUpperPitch'], 40)
		elif config.conf['beepKeyboard']['beepCharacterWithShift'] and not winUser.getKeyState(winUser.VK_CONTROL) &32768 and winUser.getKeyState(winUser.VK_SHIFT) &32768 and ch not in self.ignoredCharactersForShift and not (config.conf["keyboard"]["beepForLowercaseWithCapslock"] and ch.islower() and winUser.getKeyState(winUser.VK_CAPITAL)&1):
			v = config.conf['beepKeyboard']['shiftedCharactersVolume']
			tones.beep(config.conf['beepKeyboard']['shiftedCharactersPitch'], config.conf['beepKeyboard']['shiftedCharactersLength'], v, v)
		elif ch in self.beepForCharacters:
			v = config.conf['beepKeyboard']['customCharactersVolume']
			tones.beep(config.conf['beepKeyboard']['customCharactersPitch'], config.conf['beepKeyboard']['customCharactersLength'], v, v)

	def setExternalReportToggleStatus(self, flag):
		if flag:
			keyboardHandler.KeyboardInputGesture._reportToggleKey = _reportToggleKey
		else: keyboardHandler.KeyboardInputGesture._reportToggleKey = origReportToggleKey

	def handleConfigProfileSwitch(self):
		self.setExternalReportToggleStatus(config.conf['beepKeyboard']['beepToggleKeyChanges'])
		self.ignoredCharactersForShift = codecs.decode(config.conf['beepKeyboard']['ignoredCharactersForShift'], 'unicode_escape')
		self.beepForCharacters = codecs.decode(config.conf['beepKeyboard']['beepForCharacters'], 'unicode_escape')

	def terminate(self):
		super(GlobalPlugin, self).terminate()
		self.setExternalReportToggleStatus(False)
		gui.settingsDialogs.NVDASettingsDialog.categoryClasses.remove(BeepKeyboardSettingsPanel)
		if hasattr(config, "post_configProfileSwitch"):
			config.post_configProfileSwitch.unregister(self.handleConfigProfileSwitch)
		else:
			config.configProfileSwitched.unregister(self.handleConfigProfileSwitch)