"""
BRVNS Admin Only Slash Cog
"""
import logging
import discord

from discord.ext import commands 
from discord.ext.pages  import Paginator, Page

from src.logic import slash_logic, database_connection, resources_logic
from src.views.server_setup_views import  ServerCreationView, ServerCommandSelectionView

from os import environ

logger = logging.getLogger(environ['LOGGER_NAME'])

class SlashAdminOnly(commands.Cog):

    def __init__(self, bot):
        self.bot: commands.Bot = bot
        logger.info("Init Slash Admin Only Cog")

    @commands.has_permissions(administrator=True)
    @commands.slash_command(name = "server-setup", description="Used to set up the server, adding it to the DB.")
    async def server_setup(self, ctx: discord.ApplicationContext):
        """
        Sets up the server!
        """
        setup_pages = [
            Page(content = "Add/Remove Guild", custom_view = ServerCreationView()),
            Page(content = "Select and Enable Commands", custom_view = ServerCommandSelectionView()),
        ]

        paginator = Paginator(pages = setup_pages, default_button_row = 4)
        await paginator.respond(ctx.interaction)
        # Add the guild to the DB
        # register_server: Button = Button(lavel="Register Server", style=discord.ButtonStyle.green)
        # command_view: View =  View(register_server)
        # ctx.send("Server Setup", view=command_view)
        # await database_connection.add_guild(ctx.guild_id, ctx.guild.name)
        # logger.info(f"Added guild: {ctx.guild_id} to the DB ")

def setup(bot):
    """ 
    Add cog to bot
    """
    try:
        bot.add_cog(SlashAdminOnly(bot))
    except Exception as e:
        logger.error(e)