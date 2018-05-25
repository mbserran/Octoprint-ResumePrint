# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
import octoprint.events

class ResumePrintPlugin(octoprint.plugin.StartupPlugin,
		       octoprint.plugin.TemplatePlugin,
		       octoprint.plugin.SettingsPlugin,
		       octoprint.plugin.AssetPlugin,
		       octoprint.events.PositionUpdate):

    def __init__(self):
	# Initialize the events 
	self.event.enabled = True
	
	# Events definition here (better for intellisense in IDE)
	# referenced in the settings too.
	self.position = {
			"res_x" : {
				"name" : "Position X",
				"enabled" : True,
				"with_snapshot" : False,
				"message": "This is the X position",
				"value" : 0
			},
			"res_y" : {
				"name" : "Position Y",
				"enabled" : True,
				"with_snapshot" : False,
				"message": "This is the Y position",
				"value" : 0
			},
			"res_z" : {
				"name" : "Position Z",
				"enabled" : True,
				"with_snapshot" : False,
				"message": "This is the Y position",
				"value" : 0
			},
			"res_e" : {
				"name" : "Extruder value",
				"enabled" : True,
				"with_snapshot" : False,
				"message": "This is the E value",
				"value" : 0
			},
			"res_t" : {
				"name" : "Trip value",
				"enabled" : True,
				"with_snapshot" : False,
				"message": "This is the T value",
				"value" : 0
			},
			"res_f" : {
				"name" : "Flow value",
				"enabled" : True,
				"with_snapshot" : False,
				"message": "This is the F value",
				"value" : 0
			}
	}
    
    def on_after_startup(self):
    	self._logger.info("Hello World! (more: %s)" % self._settings.get(["url"]))

    def get_settings_defaults(self):
	return dict(url="https://en.wikipedia.org/wiki/Hello_world",
		    position = {
			    	"res_x" : {
					"name" : "Position X",
					"enabled" : True,
					"with_snapshot" : False,
					"message": "This is the X position",
					"value" : self.event.PositionUpdate.x
				},
				"res_y" : {
					"name" : "Position Y",
					"enabled" : True,
					"with_snapshot" : False,
					"message": "This is the Y position",
					"value" : self.event.PositionUpdate.y
				},
				"res_z" : {
					"name" : "Position Z",
					"enabled" : True,
					"with_snapshot" : False,
					"message": "This is the Y position",
					"value" : self.event.PositionUpdate.z
				},
				"res_e" : {
					"name" : "Extruder value",
					"enabled" : True,
					"with_snapshot" : False,
					"message": "This is the E value",
					"value" : self.event.PositionUpdate.e
				},
				"res_t" : {
					"name" : "Trip value",
					"enabled" : True,
					"with_snapshot" : False,
					"message": "This is the T value",
					"value" : self.event.PositionUpdate.t
				},
				"res_f" : {
					"name" : "Flow value",
					"enabled" : True,
					"with_snapshot" : False,
					"message": "This is the F value",
					"value" : self.event.PositionUpdate.f
				}
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
