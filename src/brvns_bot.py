"""
BRVNS Bot API
"""
import logging

from discord.ext.commands import Bot

logger = logging.getLogger(__name__)


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
