"""
BRVNS RSI Lookup

Use this class to look up information from the RSI website wirh webscraping
"""
import logging

import httpx

from os import environ

RSI_CITIZENS_LINK = "https://robertsspaceindustries.com/citizens/"
RSI_ORG_MEMBERS_LINK = "https://robertsspaceindustries.com/orgs/BRVNS/members"

API_KEY = environ["API_KEY"]

logger = logging.getLogger()
logger.setLevel("INFO")


async def check_rsi_handle(rsi_handle):
    """
    Check if the given RSI handle is valid
    """
    url = f"https://api.starcitizen-api.com/{API_KEY}/v1/live/user/{rsi_handle}"
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
    except Exception as e:
        logger.error(e)

    if response == "<Response [200 OK]>":
        return True

    return False


async def get_rsi_handle_info(rsi_handle, verification_code):
    """
    Get the info on the RSI Users About me.
    """
    url = f"https://api.starcitizen-api.com/{API_KEY}/v1/live/user/{rsi_handle}"
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
        contents = response.json()

        if verification_code in contents["data"]["profile"]["bio"]:
            return True

    except Exception as e:
        logger.error(e)

    return False


async def get_user_membership_info(rsi_handle):
    """
    Check if the user is a member, and check if they are a affilliate or main member.
    """
    url = f"https://api.starcitizen-api.com/{API_KEY}/v1/live/user/{rsi_handle}"
    membership = {"main_member": None, "member_rank": None}
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)

        contents = response.json()
        # Check if BRVNS is the main ORG
        if contents["data"]["organization"]["name"] == "Blue Ravens Inc":
            membership["main_member"] = True
            membership["member_rank"] = contents["data"]["organization"]["stars"]
        else:
            membership["main_member"] = False
            membership["member_rank"] = contents["data"]["organization"]["stars"]
    except Exception as e:
        logger.error(e)

    return membership
