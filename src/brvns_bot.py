"""
BRVNS Bot API
"""
import logging
from os import environ

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
        except Exception as e:
            logger.error(e)

        logger.info("Cogs added")

    async def on_ready(self):
        """
        Bot On Ready
        """
        logger.info(type(self.cogs))
        logger.info(f""" ____ READY ____
                                                         | Bot: {self.user.name}
                                                         | Guilds: {self.guilds}
                                                         | Cogs: {self.cogs}""".strip()
                        )

    async def on_message(self, ctx):
        logger.debug("Catching those annoying command prefix errors")
        pass
