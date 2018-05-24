# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
import octoprint.events

class ResumePrintPlugin(octoprint.plugin.StartupPlugin,
		       octoprint.plugin.TemplatePlugin,
		       octoprint.plugin.SettingsPlugin,
		       octoprint.plugin.AssetPlugin):

    def __init__(self):
	# Events definition here (better for intellisense in IDE)
	# referenced in the settings too.
	self.position = {
			"res_x" : 0,
			"res_y" : 0,
			"res_z" : 0,
			"res_e" : 0,
			"res_t" : 0,
			"res_f" : 0
	}
    
    def on_after_startup(self):
    	self._logger.info("Hello World! (more: %s)" % self._settings.get(["url"]))

    def get_settings_defaults(self):
	return dict(url="https://en.wikipedia.org/wiki/Hello_world",
		    position = {
			    	"res_x" : octoprint.events.PositionUpdate.x,
				"res_y" : octoprint.events.PositionUpdate.y,
				"res_z" : octoprint.events.PositionUpdate.z,
				"res_e" : octoprint.events.PositionUpdate.e,
				"res_t" : octoprint.events.PositionUpdate.t,
				"res_f" : octoprint.events.PositionUpdate.f
		    }
		   )

    def get_template_configs(self):
	return [
		dict(type="navbar", custom_bindings=False),
		dict(type="settings", custom_bindings=False)
	]

    def get_assets(self):
	return dict(js=["js/resumeprint.js"],
		    css=["css/resumeprint.css"],
		    less=["less/resumeprint.less"])

##~~ Softwareupdate hook
    def get_version(self):
		return self._plugin_version
		
    def get_update_information(self):
	return dict(
		resumeprint=dict(
			displayName="Resume Print",
			displayVersion=self._plugin_version,

			# version check: github repository
			type="github_release",
			user="mbserran",
			repo="OctoPrint-ResumePrint",
			current=self._plugin_version,

			# update method: pip
			pip="https://github.com/mbserran/OctoPrint-ResumePrint/archive/{target_version}.zip"
		)
    	)

__plugin_name__ = "Resume Print"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = ResumePrintPlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}
