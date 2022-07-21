"""
BRVNS Discord Bot Object
"""

from os import environ
from discord import Bot
from src.brvns_bot_logic import BrvnsLogic

class BrvnsBot(Bot):
    """
    BRVNS Discord Client
    """
    bot = Bot()

    @bot.event
    async def on_ready(self):
        """
        Bot Ready
        """
        print(f"{self.bot.name} is ready and online")

    @bot.slash_command()
    async def sign_up(self, ctx, name: str = None):
        """
        Sign Up ling slash command
        """
        author_name = name or ctx.author.name
        await ctx.respond(BrvnsLogic.signup_string(author_name))


    bot.run(environ['TOKEN'])
