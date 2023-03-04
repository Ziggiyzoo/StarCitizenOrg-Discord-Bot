"""
BRVNS Discord Bot Logic
"""
import logging

from src.logic import resources_logic

logger = logging.getLogger()
logger.setLevel("INFO")


async def signup_string(author_name: str):
    """
    Return signup string
    """
    message_content: str = resources_logic.get_string("SIGNUP", "signup_string")
    string_value: str = f"Hello {author_name}. {message_content}"
    logger.info("Signup string value:")
    logger.info(string_value)

    return string_value
