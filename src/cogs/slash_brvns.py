"""
BRVNS Slash Cogs
"""
from discord.ext import commands
from src import BrvnsLogic

class SlashBrvns(commands.Cog):
    """
    BRVNS Slash Cogs
    """

    def __init__(self, bot):
        self.bot: commands.Bot = bot
        self.logic: BrvnsLogic =  BrvnsLogic()
        print("Init Slash Command Cog.")

    @commands.slash_command(name = "sign-up", description = "Display the link to the RSI Org Page.")
    async def sign_up(self, ctx):
        """
        Sign Up string slash command
        """
        author_name: str = ctx.author.name
        await ctx.respond(self.logic.signup_string(author_name))
        print("Sent sign up string.")

def setup(bot):
    """
    Add cog to bot
    """
    bot.add_cog(SlashBrvns(bot))
