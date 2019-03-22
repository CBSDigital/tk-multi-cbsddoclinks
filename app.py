# Copyright (c) 2013 Shotgun Software Inc.
# 
# CONFIDENTIAL AND PROPRIETARY
# 
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit 
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your 
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights 
# not expressly granted therein are reserved by Shotgun Software Inc.


from sgtk.platform import Application

class CbsdDocLinksApp(Application):
    """
    The app entry point. This class is responsible for intializing and tearing down
    the application, handle menu registration etc.
    """

    # keep the Shotgun Starter App Dialog intact, but opt not to use it.
    is_use_dialog = False

    def init_app(self):
        """
        Called as the application is being initialized
        """
        
        # first, we use the special import_module command to access the app module
        # that resides inside the python folder in the app. This is where the actual UI
        # and business logic of the app is kept. By using the import_module command,
        # toolkit's code reload mechanism will work properly.
        app_payload = self.import_module("app")

        # now register a *command*, which is normally a menu entry of some kind on a Shotgun
        # menu (but it depends on the engine). The engine will manage this command and 
        # whenever the user requests the command, it will call out to the callback.

        # Choose whether to use dialog
        if self.is_use_dialog:
            # first, set up our callback, calling out to a method inside the app module contained
            # in the python folder of the app
            menu_callback = lambda : app_payload.dialog.show_dialog(self)
        else:
            # Open the url
            menu_callback = lambda : app_payload.open_cbsd_wiki.open_wiki()

        # now register the command with the engine
        self.engine.register_command("CBSD Docs...", menu_callback)

