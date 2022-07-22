"""
BRVNS Config Object
"""

import configparser

class BrvnsConfig():
    """
    Brvns Config
    """
    config = configparser.RawConfigParser()
    config.read("~/../config/ConfigFile.ini")

    def get_config(self, section, key):
        """
        Get the config from the .ini file
        """
        return self.config.get(section, key)
