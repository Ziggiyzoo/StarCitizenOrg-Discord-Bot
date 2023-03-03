"""
BRVNS RSI Lookup

Use this class to look up information from the RSI website wirh webscraping
"""

import requests, json, logging

from os import environ

rsi_citizens = "https://robertsspaceindustries.com/citizens/"

logger = logging.getLogger(environ['LOGGER_NAME'])

async def check_rsi_handle(rsi_handle):
    """
    Check if the given RSI handle is valid
    """
    response = requests.get(rsi_citizens + rsi_handle)
    if response.status_code == 200:
        return True
    else:
        logger.info("RSI Handle Lookup returned code: " + response.status_code)
        return False

async def get_rsi_handle_info(rsi_handle, verification_code):
    """
    Get the info on the RSI Users About me.
    """
    response = requests.get(rsi_citizens + rsi_handle)
    if verification_code in response.text:
        return True
    else:
        logger.info("Incorrect verification code.")
        return False
