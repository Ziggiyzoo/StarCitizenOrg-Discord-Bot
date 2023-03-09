"""
BRVNS Config Utilities
Use this method to return resources form the strings.ini file.
"""

import configparser
import os
import string
import random

config = configparser.ConfigParser()

present_directory = os.path.dirname(os.path.abspath(__file__))


def get_resource(file: str, section: str, key: str, testing: bool = False) -> str:
    """
    Get a resource from the resources directory
    """
    if testing:
        inifile: str = os.path.join(
            present_directory, f"../../test/resources/{file}.ini"
        )
    else:
        inifile: str = os.path.join(present_directory, f"../resources/{file}.ini")
    config.read(inifile)

    value: str = config.get(section, key)

    if value is not None and value != "":
        return value

    return "VALUE_NOT_FOUND"


def get_string(section: str, key: str, testing: bool = False):
    """
    Get a String from the resources/strings.ini file
    """

    if testing:
        return get_resource("strings", section, key, testing)

    return get_resource("strings", section, key)


def create_random_string():
    """
    Create a randomg string for verification
    """

    return "".join([random.choice(string.ascii_letters) for n in range(10)])
