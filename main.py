"""
BRVNS Discord Bot
"""
import logging
from os import environ

from src.brvns_bot import BrvnsBot

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel("INFO")

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
    Bot.load_extensions("src.cogs", recursive=True)
    Bot.run(token)
