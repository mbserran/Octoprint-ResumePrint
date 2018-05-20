# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class ResumePrintPlugin(octoprint.plugin.StartupPlugin,
		       octoprint.plugin.TemplatePlugin,
		       octoprint.plugin.SettingsPlugin,
		       octoprint.plugin.AssetPlugin):

    def on_after_startup(self):
        self._logger.info("Hello World! (more: %s)" % self._settings.get(["url"]))

    def get_settings_defaults(self):
	return dict(url="https://en.wikipedia.org/wiki/Hello_world")

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

    def get_update_information(self):
	return dict(resumeprint=dict(
		    displayName="ResumePrint Plugin",
		    displayVersion=self._plugin_version,

		    # version check: github repository
		    type="github_release",
		    user="mbserran",
		    repo="OctoPrint-ResumePrint",
		    current=self._plugin_version,

		    # update method: pip
		    pip="https://github.com/OctoPrint/OctoPrint-ResumePrint/archive/{target_version}.zip"
		    )
    	       )

__plugin_name__ = "Resume Print"
__plugin_implementation__ = ResumePrintPlugin()
