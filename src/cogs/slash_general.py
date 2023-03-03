"""
General Slash Cogs
"""
from os import environ

import logging

from discord.ext import commands

logger = logging.getLogger(environ["LOGGER_NAME"])


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
    bot.add_cog(SlashGeneral(bot))
