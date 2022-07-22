"""
BRVNS Discord Bot Object
"""
from discord import Bot
from src.brvns_bot_logic import BrvnsLogic

class BrvnsBot(Bot):
    """
    BRVNS Discord Client
    """

    __slots__ = ("bot", "brvns_logic")
    def __init__(self):
        super().__init__()
        self.brvns_logic = BrvnsLogic()
        self.bot = Bot()


    def run(self, token):
        """
        Run the bot
        """
        self.bot.run(token)

    @bot.event
    async def on_ready(self):
        """
        Bot Ready
        """
        print(f"{self.bot.name} is ready and online")

    @bot.slash_command()
    async def sign_up(self, ctx):
        """
        Sign Up string slash command
        """
        author_name: str = ctx.author.name
        await ctx.respond(self.brvns_logic.signup_string(author_name))

    @bot.command()
    async def ping(self, ctx):
        """
        Send bot ping
        """
        await ctx.respond(f"Pong! Latency is {self.bot.latency}")
        