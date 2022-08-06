"""
General Slash Cogs
"""
import logging
import discord

from os import environ

from discord.ext import commands
from discord.ext.pages import Paginator, Page

logger = logging.getLogger(environ['LOGGER_NAME'])


class SlashGeneral(commands.Cog):
    """
    General Slash Commands
    """

    def __init__(self, bot):
        self.bot: commands.Bot = bot
        logger.info("Init General Slash Command Cog")

    @commands.slash_command(name="ping", description="Return the bot latency.")
    async def ping(self, ctx):
        """
        Send bot ping
        """
        await ctx.respond(f"Pong! Latency is {round(self.bot.latency * 100, 2)} ms")
        logger.info("Sent Ping")

def setup(bot):
    """
    Add cog to bot
    """
    try:
        bot.add_cog(SlashGeneral(bot))
    except Exception as error:
        logger.error(error)
