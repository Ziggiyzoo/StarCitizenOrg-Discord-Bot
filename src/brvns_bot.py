"""
BRVNS Bot API
"""
import logging

from discord.ext.commands import Bot

logger = logging.getLogger()
logger.setLevel("INFO")


# pylint: disable=too-many-ancestors
class BrvnsBot(Bot):
    """
    BRVNS Bot
    """

    def __init__(self, debug_guilds):
        super().__init__(self, debug_guilds=debug_guilds)
        self.load_extension("src.cogs", recursive=True)
        logger.info("Cogs added")

    async def on_ready(self):
        """
        Bot On Ready
        """
        logger.info("READY")

    async def on_message(self, message):
        """
        Catch message and do nothing
        """
