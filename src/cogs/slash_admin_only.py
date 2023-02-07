"""
BRVNS Admin Only Slash Cog
"""
import logging

from os import environ

import discord

from discord.ext import commands

from src.logic import database_connection, resources_logic
logger = logging.getLogger(environ['LOGGER_NAME'])

class SlashAdminOnly(commands.Cog):
    """
    Commands for admin use only
    """
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        logger.info("Init Slash Admin Only Cog")

    @commands.has_permissions(administrator=True)
    @commands.slash_command(name = "add-guild", description="Used to set up the server, adding it to the DB.")
    async def add_guild(self, ctx, spectrum_id: discord.Option(str)):
        """
        Add the guild to the DB
        """

        success = await database_connection.add_guild(ctx.guild_id, ctx.guild.name, spectrum_id)

        if success:
            await ctx.response.send_message("Guild Added to the DB", ephemeral = True)
        else:
            await ctx.response.send_message(resources_logic.get_string("ERROR_MESSAGES", "add_guild_error"), ephemeral = True)

    @commands.has_permissions(administrator=True)
    @commands.slash_command(name = "remove-guild", description="Used to remove the server, removing it to the DB.")
    async def remove_guild(self, ctx):
        """
        Remove the guild from the DB
        """

        success = await database_connection.remove_guild(ctx.guild_id)

        if success:
            await ctx.response.send_message("Guild Removed from the DB", ephemeral = True)
        else:
            await ctx.response.send_message(resources_logic.get_string("ERROR_MESSAGES", "remove_guild_error"), ephemeral = True)



def setup(bot):
    """
    Add cog to bot
    """

    bot.add_cog(SlashAdminOnly(bot))
    
