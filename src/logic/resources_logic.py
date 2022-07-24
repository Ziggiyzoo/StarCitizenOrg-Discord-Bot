"""
BRVNS Config Utilities
Use this method to return resources form the resources.ini file.
"""

import configparser
import os

config = configparser.ConfigParser()

thisfolder = os.path.dirname(os.path.abspath(__file__))

def get_resource(file, section, key):
    """
    Get the config from the .ini file
    """
    inifile = os.path.join(thisfolder, f"../resources/{file}.ini")
    config.read(inifile)
    return config.get(section, key)
