"""
BRVNS Config Object
"""

import configparser
import os

class BrvnsResources():
    """
    Brvns Config

    Currently this is going to a harcoded file in the project. Though it should talk to a DB, this will allow admins to set their own responses.. I will 
    need to look up how to properly create a DB connection etc..
    """
    config = configparser.ConfigParser()

    thisfolder = os.path.dirname(os.path.abspath(__file__))
    inifile = os.path.join(thisfolder, "resources/resources.ini")
    config.read(inifile)
    
    def get_config(self, section, key):
        """
        Get the config from the .ini file
        """
        return self.config.get(section, key)

    #Allow discord mod to create their own hardcoded 
    #This needs to actually check if it was successful. I cannot be bothered to add a test for it not. Do this tomorrow david
    def set_config(self, section, key, value):
        self.config.set(section, key, value)

