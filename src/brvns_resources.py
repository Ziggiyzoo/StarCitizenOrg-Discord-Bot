"""
BRVNS Config Utilities
Use this class to return resources form the resources.ini file.
"""

import configparser
import os

config = configparser.ConfigParser()

thisfolder = os.path.dirname(os.path.abspath(__file__))
inifile = os.path.join(thisfolder, "resources/resources.ini")
config.read(inifile)

def get_config( section, key):
    """
    Get the config from the .ini file
    """
    return config.get(section, key)
