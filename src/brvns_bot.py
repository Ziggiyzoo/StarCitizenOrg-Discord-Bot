"""
BRVNS Bot API
"""
import logging
from os import environ

from discord.ext.commands import Bot

logger = logging.getLogger(environ['LOGGER_NAME'])


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
        logger.info(f"""
            ____ READY ____
            Bot: {self.user.name}
            Guilds: {self.guilds}
            Cogs: {self.cogs}""".strip())

    async def on_message(self, ctx):
        logger.info("Catching those annoying command prefix errors")
