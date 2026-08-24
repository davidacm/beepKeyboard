from site_scons.site_tools.NVDATool.utils import _

class Config:
	VERSION = "26.8.0"
	MIN_NVDA = "2018.3.0"
	LAST_TESTED = "2026.2"
	# Essential Metadata
	ID = "beepKeyboard"
	# Translators: Summary/title for this add-on
	SUMMARY = _("Beep keyboard")
	# Translators: Long description to be shown for this add-on on add-on information from add-on store
	DESCRIPTION = _("""This add-on beeps with some keyboard events.""")
	# Translators: what's new content for the add-on version to be shown in the add-on store
	CHANGELOG = _("""Capital letter beeps are now more accurate, only sound in edit fields, and no longer duplicate NVDA's own beep for capitals.""")
	author="David CM <dhf360@gmail.com>"
	URL = "https://github.com/david-acm/beepKeyboard"

from site_scons.site_tools.NVDATool.typings import AddonInfo, BrailleTables, SymbolDictionaries, SpeechDictionaries


addon_info = AddonInfo(
	addon_name=Config.ID,
	addon_summary=Config.SUMMARY,
	addon_description=Config.DESCRIPTION,
	addon_version=Config.VERSION,
	addon_changelog=Config.CHANGELOG,
	addon_author=Config.author,
	addon_url=Config.URL,
	addon_sourceURL=Config.URL,
	addon_docFileName="readme.html",
	addon_minimumNVDAVersion=Config.MIN_NVDA,
	addon_lastTestedNVDAVersion=Config.LAST_TESTED,
	# Add-on update channel (default is None, denoting stable releases,
	# and for development releases, use "dev".)
	# Do not change unless you know what you are doing!
	addon_updateChannel=None,
	# Add-on license such as GPL 2
	addon_license="GPL 2",
	# URL for the license document the ad-on is licensed under
	addon_licenseURL="https://www.gnu.org/licenses/old-licenses/gpl-2.0.html",
)

pythonSources: list[str] = ["addon/globalPlugins/beepKeyboard/*.py"]

i18nSources: list[str] = pythonSources + ["buildVars.py"]

# Files that will be ignored when building the nvda-addon file
# Paths are relative to the addon directory, not to the root directory of your addon sources.
# You can either list every file (using ""/") as a path separator,
# or use glob expressions.
excludedFiles: list[str] = []

baseLanguage: str = "en"

markdownExtensions: list[str] = []

brailleTables: BrailleTables = {}

symbolDictionaries: SymbolDictionaries = {}
speechDictionaries: SpeechDictionaries = {}
