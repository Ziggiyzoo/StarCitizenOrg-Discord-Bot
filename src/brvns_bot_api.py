"""
BRVNS Discord Bot Object
"""
from discord import Bot
from src.brvns_bot_logic import BrvnsLogic

class BrvnsBot():
    """
    BRVNS Discord Client
    """
    bot = Bot()
    brvns_logic = BrvnsLogic()

    @bot.event
    async def on_ready(self):
        """
        Bot Ready
        """
        print(f"{self.bot.name} is ready and online")

    @bot.slash_command()
    async def sign_up(self, ctx, name: str = None):
        """
        Sign Up string slash command
        """
        author_name = name or ctx.author.name
        await ctx.respond(self.brvns_logic.signup_string(author_name))
