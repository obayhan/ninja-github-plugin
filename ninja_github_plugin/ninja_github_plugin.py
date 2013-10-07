# -*- coding: UTF-8 -*-

from ninja_ide.core import plugin


class GithubPlugin(plugin.Plugin):

    def initialize(self):
        # Init your plugin
        self.menuApp_s = self.locator.get_service('menuApp')
        self.explorer_s = self.locator.get_service('explorer')

    def finish(self):
        # Shutdown your plugin
        pass

    def get_preferences_widget(self):
        # Return a widget for customize your plugin
        pass
