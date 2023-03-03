"""
BRVNS Discord Bot
"""
from os import environ

import logging

from src.brvns_bot import BrvnsBot

logging.basicConfig()
logger = logging.getLogger(environ["LOGGER_NAME"])
logger.setLevel(environ["LOGGER_LEVEL"])

# Main Method
if __name__ == "__main__":
    # Check for required environment variables
    if "TOKEN" not in environ or environ["TOKEN"] == "":
        raise ValueError(
            "No value for Environment Variable 'TOKEN' supplied. Exiting..."
        )
    logger.info("Token found, running the bot")

    token: str = environ["TOKEN"]
    Bot: BrvnsBot = BrvnsBot(debug_guilds=[997138062381416589])
    Bot.run(token)
