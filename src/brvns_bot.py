"""
BRVNS Bot API
"""
import logging

import discord.ext.commands as ext_commands

logging.basicConfig(
    format="| %(asctime)s | %(levelname)-8s | [%(filename)s:%(lineno)d] | %(message)s"
)
logger = logging.getLogger()
logger.setLevel("INFO")


# pylint: disable=too-many-ancestors
class BrvnsBot(ext_commands.Bot):
    """
    BRVNS Bot
    """

    def __init__(self, debug_guilds):
        super().__init__(self, debug_guilds=debug_guilds)

    async def on_ready(self):
        """
        Bot On Ready
        """
        logger.info("READY")

    async def on_message(self, message):
        """
        Catch message and do nothing
        """
