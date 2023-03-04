"""
BRVNS RSI Lookup

Use this class to look up information from the RSI website wirh webscraping
"""
import logging
import requests

RSI_CITIZENS_LINK = "https://robertsspaceindustries.com/citizens/"

logger = logging.getLogger()
logger.setLevel("INFO")


async def check_rsi_handle(rsi_handle):
    """
    Check if the given RSI handle is valid
    """
    response = requests.get(RSI_CITIZENS_LINK + rsi_handle, timeout=30)
    logger.info("RSI Handle Lookup returned code:")
    logger.info(response.status_code)
    if response.status_code == 200:
        return True

    return False


async def get_rsi_handle_info(rsi_handle, verification_code):
    """
    Get the info on the RSI Users About me.
    """
    response = requests.get(RSI_CITIZENS_LINK + rsi_handle, timeout=30)
    if verification_code in response.text:
        return True

    logger.info("Incorrect verification code.")
    return False
