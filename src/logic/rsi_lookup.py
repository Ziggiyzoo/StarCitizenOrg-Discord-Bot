"""
BRVNS RSI Lookup

Use this class to look up information from the RSI website wirh webscraping
"""
import logging
import requests

from bs4 import BeautifulSoup
from urllib.request import urlopen

RSI_CITIZENS_LINK = "https://robertsspaceindustries.com/citizens/"
RSI_ORG_MEMBERS_LINK = "https://robertsspaceindustries.com/orgs/BRVNS/members"

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
    url = RSI_CITIZENS_LINK + rsi_handle
    soup = await open_page(url)
    bio = soup.find("div", {"class": "entry bio"})
    if verification_code in bio.text:
        return True

    logger.info("Incorrect verification code.")
    return False


async def get_user_membership(rsi_handle):
    """
    Check if the user is a member, and check if they are a affilliate or main member.
    """
    href_id = "/citizens/" + rsi_handle
    soup = await open_page(RSI_ORG_MEMBERS_LINK)

    member = soup.find("a", href=href_id)
    if member is not None:
        title = member.find("span", {"class": "title"})
        if title.text == "Roles":
            return "Org Member"
        return "Org Affiliate"
    return "ERROR: Org Member Missing"


async def get_user_rank(rsi_handle):
    """
    Check of the user is a member, and if they are get their rank.
    """
    href_id = "/citizens/" + rsi_handle
    soup = await open_page(RSI_ORG_MEMBERS_LINK)

    member = soup.find("a", href=href_id)
    if member is not None:
        rank = member.find("span", {"class": "rank"})
        return rank.text
    return "ERROR: Org Member Missing"


async def open_page(page_url):
    """
    Open the page and make it into soup
    """
    page = urlopen(page_url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    return BeautifulSoup(html, "html.parser")
