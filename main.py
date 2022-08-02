"""
BRVNS Discord Bot
"""
from os import environ

import logging
import discord

from src.brvns_bot import BrvnsBot

logging.basicConfig()
logger = logging.getLogger(environ['LOGGER_NAME'])
logger.setLevel(environ['LOGGER_LEVEL'])

# Main Method
if __name__ == "__main__":
    try:
        # Check for required environment variables
        if "TOKEN" not in environ or environ['TOKEN'] == "":

            raise ValueError("No value for Environment Variable 'TOKEN' supplied. Exiting...")
        logger.info("Token found, running the bot")

        token: str = environ['TOKEN']
        Bot: BrvnsBot = BrvnsBot(debug_guilds=[997138062381416589])
        try:
            Bot.run(token)
        except discord.ext.commands.errors.MissingPermissions as missing_permissions_error:
            logger.info(missing_permissions_error)

    except ValueError as e:
        logger.error(e)
