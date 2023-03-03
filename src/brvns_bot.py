"""
BRVNS Bot API
"""
import logging
from os import environ

import discord

from discord.ext.commands import Bot

logging.basicConfig(format="| %(asctime)s | %(levelname)-8s | [%(filename)s:%(lineno)d] | %(message)s")
logger = logging.getLogger(environ['LOGGER_NAME'])



# pylint: disable=too-many-ancestors
class BrvnsBot(Bot):
    """
    BRVNS Bot
    """

    def __init__(self, debug_guilds):
        super().__init__(self, debug_guilds=debug_guilds)

        try:
            self.load_extension("src.cogs", recursive=True)
        except discord.ext.commands.errors as discord_error:
            logger.error(f"Error in discord: {discord_error}")

        logger.info("Cogs added")

    async def on_ready(self):
        """
        Bot On Ready
        """
        logger.info(type(self.cogs))
        logger.info("BOT READY")

    async def on_message(self, message):
        """
        Ignore Prefixless Messages
        """
