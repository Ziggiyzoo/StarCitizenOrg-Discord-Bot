"""
BRVNS Discord Bot Object
"""
import discord
from src.brvns_bot_logic import BrvnsLogic

class BrvnsBot(discord.Bot):
    """
    BRVNS Discord Bot
    """
    brvns_logic = BrvnsLogic()

    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()

    async def on_ready(self):
        """
        Bot Ready
        """
        print(f"The Bot, {self.user.name}, {self.user.id} is ready and online!")
        print(f"Bot Guilds: {self.guilds}")
        print(f"Guild Ids: {self.guild_id_list}")

    @discord.slash_command(name = "sign-up", description = "Display the link to the RSI Org Page.")
    async def sign_up(self, ctx):
        """
        Sign Up string slash command
        """
        author_name: str = ctx.author.name
        await ctx.respond(self.brvns_logic.signup_string(author_name))

    @discord.slash_command(name = "ping", description = "Return the bot latency.")
    async def ping(self, ctx):
        """
        Send bot ping
        """
        await ctx.respond(f"Pong! Latency is {self.user.latency}")
