"""
BRVNS Slash Cogs
"""
import logging

from discord.ext import commands

from src.logic import slash_logic

logger = logging.getLogger(__name__)


class SlashBrvns(commands.Cog):
    """
    BRVNS Slash Cogs
    """

    def __init__(self, bot):
        self.bot: commands.Bot = bot

        logger.info("Init Brvns Slash Command Cog")

    @commands.slash_command(name="sign-up", description="Display the link to the RSI Org Page.")
    async def sign_up(self, ctx):
        """
        Sign Up string slash command
        """
        author_name: str = ctx.author.name
        await ctx.respond(slash_logic.signup_string(author_name))
        logger.info("Sent sign up string.")


def setup(bot):
    """
    Add cog to bot
    """
    bot.add_cog(SlashBrvns(bot))
