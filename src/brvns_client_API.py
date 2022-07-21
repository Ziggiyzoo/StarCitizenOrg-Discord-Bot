"""
BRVNS Discord Bot Object
"""

from discord import Bot, Client
from src.brvns_bot_logic import BrvnsLogic
from os import environ

class BrvnsClient(Client):
    """
    BRVNS Discord Client
    """
    bot = Bot()

    @bot.event
    async def on_ready(bot):
        print(f"We have logged in as {bot.user}")

    @bot.slash_command()
    async def sign_up(ctx, name: str = None):
        author_name = name or ctx.author.name
        await ctx.respond(str(BrvnsLogic.signup_string(author_name)))

    bot.run(environ['TOKEN'])