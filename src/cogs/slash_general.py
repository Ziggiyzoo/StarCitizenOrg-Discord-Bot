"""
General Slash Cogs
"""
from discord.ext import commands

class SlashGeneral(commands.Cog):
    """
    General Slash Commands
    """

    def __init__(self, bot):
        self.bot: commands.Bot = bot
        print("Init Slash Command Cog.")

    @commands.slash_command(name = "ping", description = "Return the bot latency.")
    async def ping(self, ctx):
        """
        Send bot ping
        """
        await ctx.respond(f"Pong! Latency is {round(self.bot.latency * 100, 2)} ms")
        print("Sent Ping")

def setup(bot):
    """
    Add cog to bot
    """
    bot.add_cog(SlashGeneral(bot))
