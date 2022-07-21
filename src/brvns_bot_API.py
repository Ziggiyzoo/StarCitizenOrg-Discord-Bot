"""
BRVNS Discord Bot Object
"""

from discord import Bot
from src.brvns_bot_logic import BrvnsLogic
from os import environ

class BrvnsBot(Bot):
    """
    BRVNS Discord Client
    """
    bot = Bot()

    @bot.event
    async def on_ready():
        print(f"Bot is ready and online")

    @bot.slash_command()
    async def sign_up(ctx, name: str = None):
        author_name = name or ctx.author.name
        await ctx.respond(BrvnsLogic.signup_string(author_name))


    bot.run(environ['TOKEN'])