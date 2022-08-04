# -*- coding: UTF-8 -*-
# Beep keyboard: This add-on beeps with some keyboard events.
# Copyright (C) 2019 - 2022 David CM
# Author: David CM <dhf360@gmail.com>
# Released under GPL 2
#globalPlugins/beepKeyboard.py

import api, codecs, config, globalPluginHandler, gui, keyboardHandler, tones, ui, winreg, winUser, wx, addonHandler

addonHandler.initTranslation()


from ._configHelper import configSpec, registerConfig
@configSpec('beepKeyboard')
class AppConfig:
	beepUpperWithCapsLock = 'boolean(default=True)'
	beepCharacterWithShift = 'boolean(default=False)'
	beepToggleKeyChanges = 'boolean(default=False)'
	announceToggleStatus = 'boolean(default=True)'
	disableBeepingOnPasswordFields = 'boolean(default=True)'
	ignoredCharactersForShift = "string(default='\\x1b\\t\\b\\r ')"
	beepForCharacters = "string(default='')"
	shiftedCharactersTone = 'int_list(default=list(6000,10,25))'
	customCharactersTone = 'int_list(default=list(6000,10,25))'
	capsLockUpperTone = 'int_list(default=list(3000,40,50))'
	toggleOffTone = 'int_list(default=list(500,40,50))'
	toggleOnTone = 'int_list(default=list(2000, 40, 50))'
AF = registerConfig(AppConfig)


# Constants.
REG_TOGGLE_KEYS = r"Control Panel\Accessibility\ToggleKeys"
REG_KEY = "Flags"
REG_VALUE_ON = 63

# global variables
ignoreToggleKeys = False

def beep(l):
	""" it receives a list with three arguments to beep: [pitch, length, volume]"""
	if not (AF.disableBeepingOnPasswordFields and api.getFocusObject().isProtected):
		tones.beep(*l, right=l[-1])

#saves the original _reportToggleKey function
origReportToggleKey = keyboardHandler.KeyboardInputGesture._reportToggleKey

# alternate function to report state key.
def _reportToggleKey(self):
	global ignoreToggleKeys
	if not ignoreToggleKeys:
		if winUser.getKeyState(self.vkCode) & 1:
			beep(AF.toggleOnTone)
		else: beep(AF.toggleOffTone)
	if ignoreToggleKeys or AF.announceToggleStatus or (AF.disableBeepingOnPasswordFields and api.getFocusObject().isProtected):
		origReportToggleKey(self)

class BeepKeyboardSettingsPanel(gui.SettingsPanel):
	# Translators: This is the label for the beepKeyboard  settings category in NVDA Settings screen.
	title = _("Beep keyboard")

	def makeSettings(self, settingsSizer):
		sHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		# Translators: label for a checkbox option in the settings panel.
		self.beepUpperWithCapsLock = sHelper.addItem(wx.CheckBox(self, label=_("Beep for uppercases  when &caps lock is on")))
		self.beepUpperWithCapsLock.SetValue(AF.beepUpperWithCapsLock)
		# Translators: label for a checkbox option in the settings panel.
		self.beepCharacterWithShift = sHelper.addItem(wx.CheckBox(self, label=_("Beep for typed characters when &shift is pressed")))
		self.beepCharacterWithShift.SetValue(AF.beepCharacterWithShift)
		# Translators: label for a checkbox option in the settings panel.
		self.beepToggleKeyChanges = sHelper.addItem(wx.CheckBox(self, label=_("Beep for &toggle keys changes")))
		self.beepToggleKeyChanges.SetValue(AF.beepToggleKeyChanges)
		# Translators: label for a checkbox option in the settings panel.
		self.announceToggleStatus = sHelper.addItem(wx.CheckBox(self, label=_("&Announce toggle keys changes (if Beep for toggle keys changes is disabled NVDA will have the original behavior)")))
		self.announceToggleStatus.SetValue(AF.announceToggleStatus)
		# Translators: label for a checkbox option in the settings panel.
		self.disableBeepingOnPasswordFields = sHelper.addItem(wx.CheckBox(self, label=_("&disable beeping on password fields")))
		self.disableBeepingOnPasswordFields.SetValue(AF.disableBeepingOnPasswordFields)

		# Translators: label for a button to open advanced settings dialog in the settings panel.
		advancedButton = sHelper.addItem (wx.Button (self, label = _("&Open advanced options")))
		advancedButton.Bind(wx.EVT_BUTTON, self.onAdvanced)

	def onAdvanced(self, evt):
		advanced = AdvancedBeepKeyboardSettingsDialog(self, multiInstanceAllowed=True)
		advanced.ShowModal()

	def onSave(self):
		AF.beepUpperWithCapsLock = self.beepUpperWithCapsLock.GetValue()
		AF.beepCharacterWithShift = self.beepCharacterWithShift.GetValue()
		AF.beepToggleKeyChanges = self.beepToggleKeyChanges.GetValue()
		AF.announceToggleStatus = self.announceToggleStatus.GetValue()
		AF.disableBeepingOnPasswordFields = self.disableBeepingOnPasswordFields.GetValue()
		config.post_configProfileSwitch.notify()

class AdvancedBeepKeyboardSettingsDialog(gui.SettingsDialog):
	# Translators: This is the label for the beep keyboard advanced settings dialog
	title = _("Advanced settings - Keyboard beep")

	def makeSettings(self, settingsSizer):
		sHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		# Translators: label for an edit text control option in the advanced settings dialog.
		self.ignoredCharactersForShift  = sHelper.addLabeledControl(_("&Ignored characters with shift pressed"), wx.TextCtrl)
		self.ignoredCharactersForShift.SetValue(AF.ignoredCharactersForShift)
		# Translators: label for an edit text control option in the advanced settings dialog.
		self.beepForCharacters  = sHelper.addLabeledControl(_("Beep &always for the following characters"), wx.TextCtrl)
		self.beepForCharacters.SetValue(AF.beepForCharacters)		
		self.tonesParameters = [AF.shiftedCharactersTone, AF.customCharactersTone, AF.capsLockUpperTone, AF.toggleOffTone, AF.toggleOnTone]
		# Translators: label for a combo box control in the advanced settings dialog.
		self.toneOptionsList = sHelper.addLabeledControl(_("&Select tone to configure"), wx.Choice, choices=[
			# Translators: label for an option of a combo box control.
			_("Typed characters with shift pressed"),
			# Translators: label for an option of a combo box control.
			_("Custom characters"),
			# Translators: label for an option of a combo box control.
			_("Typed characters when  caps lock is on"),
			# Translators: label for an option of a combo box control.
			_("Toggle key goes off"),
			# Translators: label for an option of a combo box control.
			_("Toggle key goes on")])
		self.toneOptionsList.SetSelection(0)
		self.curSelection=0
		self.toneOptionsList.Bind(wx.EVT_CHOICE, self.onToneOptionChange)
		# Translators: label for an edit text control option in the advanced settings dialog.
		self.tonePitch = sHelper.addLabeledControl(_("Tone &pitch"), wx.TextCtrl)
		self.tonePitch.SetValue(str(self.tonesParameters[0][0]))
		# Translators: label for an edit text control option in the advanced settings dialog.
		self.toneLength = sHelper.addLabeledControl(_("Tone &length"), wx.TextCtrl)
		self.toneLength.SetValue(str(self.tonesParameters[0][1]))
		# Translators: label for an edit text control option in the advanced settings dialog.
		self.toneVolume = sHelper.addLabeledControl(_("Tone &volume"), wx.TextCtrl)
		self.toneVolume.SetValue(str(self.tonesParameters[0][2]))
		# Translators: label for a button to play demo tone in advanced settings dialog.
		testButton = sHelper.addItem (wx.Button (self, label = _("&Test tone")))
		testButton.Bind(wx.EVT_BUTTON, self.onTest)

	def postInit(self):
		# ensure that focus is on the ignoredCharactersForShift
		self.ignoredCharactersForShift.SetFocus()

	def updateCurrentToneValues(self):
		try:
			l = [int(self.tonePitch.GetValue()), int(self.toneLength.GetValue()), int(self.toneVolume.GetValue())]
			if True in [k<0 for k in l]: raise ValueError
			self.tonesParameters[self.curSelection] = l
		except ValueError:
			tones.beep(100,160)
			# Translators: an error message sent to ve spoken by NVDA.
			ui.message(_("You entered a wrong value. Please correct it or discard changes."))
			raise ValueError

	def onTest(self, evt):
		self.updateCurrentToneValues()
		beep(self.tonesParameters[self.curSelection])

	def onToneOptionChange(self, evt):
		try:
			self.updateCurrentToneValues()
		except ValueError:
			self.toneOptionsList.SetSelection(self.curSelection)
			return
		self.curSelection = self.toneOptionsList.GetCurrentSelection()
		co = self.tonesParameters[self.curSelection][0:3]
		beep(co)
		self.tonePitch.SetValue(str(co[0]))
		self.toneLength.SetValue(str(co[1]))
		self.toneVolume.SetValue(str(co[2]))

	def onOk(self, evt):
		self.updateCurrentToneValues()
		AF.ignoredCharactersForShift = self.ignoredCharactersForShift.GetValue()
		AF.beepForCharacters = self.beepForCharacters.GetValue()
		AF.shiftedCharactersTone, AF.customCharactersTone, AF.capsLockUpperTone, AF.toggleOffTone, AF.toggleOnTone = self.tonesParameters
		config.post_configProfileSwitch.notify()
		super(AdvancedBeepKeyboardSettingsDialog, self).onOk(evt)


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def __init__(self):
		super(globalPluginHandler.GlobalPlugin, self).__init__()
		self.handleConfigProfileSwitch()
		gui.settingsDialogs.NVDASettingsDialog.categoryClasses.append(BeepKeyboardSettingsPanel)
		config.post_configProfileSwitch.register(self.handleConfigProfileSwitch)

	def checkEaseAccessToggleKeys(self):
		global ignoreToggleKeys
		# disables sounds for toggle keys if native system toggle keys is enabled.
		try:
			r = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_TOGGLE_KEYS, 0, winreg.KEY_READ)
			v, _ = winreg.QueryValueEx(r, REG_KEY)
			if int(v) == REG_VALUE_ON: ignoreToggleKeys = True
			else: ignoreToggleKeys = False
		except:
			ignoreToggleKeys = False

	def event_typedCharacter(self, obj, nextHandler, ch):
		nextHandler()
		if AF.beepUpperWithCapsLock and winUser.getKeyState(winUser.VK_CAPITAL)&1 and ch.isupper():
			beep(AF.capsLockUpperTone)
		elif AF.beepCharacterWithShift and not winUser.getKeyState(winUser.VK_CONTROL) &32768 and winUser.getKeyState(winUser.VK_SHIFT) &32768 and ch not in self.ignoredCharactersForShift and not (config.conf["keyboard"]["beepForLowercaseWithCapslock"] and ch.islower() and winUser.getKeyState(winUser.VK_CAPITAL)&1):
			beep(AF.shiftedCharactersTone)
		elif ch in self.beepForCharacters: beep(AF.customCharactersTone)

	def setExternalReportToggleStatus(self, flag):
		global ignoreToggleKeys
		if flag:
			self.checkEaseAccessToggleKeys()
			if not ignoreToggleKeys:
				keyboardHandler.KeyboardInputGesture._reportToggleKey = _reportToggleKey
				return
		keyboardHandler.KeyboardInputGesture._reportToggleKey = origReportToggleKey

	def handleConfigProfileSwitch(self):
		self.setExternalReportToggleStatus(AF.beepToggleKeyChanges)
		self.ignoredCharactersForShift = codecs.decode(AF.ignoredCharactersForShift, 'unicode_escape')
		self.beepForCharacters = codecs.decode(AF.beepForCharacters, 'unicode_escape')

	def terminate(self):
		super(GlobalPlugin, self).terminate()
		self.setExternalReportToggleStatus(False)
		gui.settingsDialogs.NVDASettingsDialog.categoryClasses.remove(BeepKeyboardSettingsPanel)
		config.post_configProfileSwitch.unregister(self.handleConfigProfileSwitch)
