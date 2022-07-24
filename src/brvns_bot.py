"""
BRVNS Bot API
"""
from discord.ext.commands import Bot

# pylint: disable=too-many-ancestors
class BrvnsBot(Bot):
    """
    BRVNS Bot
    """
    def __init__(self, debug_guilds):
        super().__init__(self, debug_guilds=debug_guilds)
        self.add_cogs()
        print("Init the bot")

    def add_cogs(self):
        """
        Import cogs for the bot.
        """
        self.load_extension("src.cogs", recursive=True)
        print("Cogs added.")

    async def on_ready(self):
        """
        Bot On Ready
        """
        print(f"____ READY ____\nBot: {self.user.name} \nGuilds: {self.guilds} \nCogs: {self.cogs}")
