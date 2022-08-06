"""
Server Setup View.

Contains all the view classes for views used in the /server-setup command.
"""
import logging

from os import environ

import discord
from discord.ui import View

from src.logic import database_connection, slash_logic, resources_logic


logger = logging.getLogger(environ['LOGGER_NAME'])

class ServerCreationView(View):
    """
    View for the page that allows the addition/removal of the guild from the DB
    """
    def __init__(self):
        super().__init__()

    @discord.ui.button(label = "Add", style = discord.ButtonStyle.green, row = 2)
    async def add_guild(self, button, interaction):
        """
        Add the guild to the DB
        """
        try:
            await database_connection.add_guild(interaction.guild_id, interaction.guild.name)
            success = True
        except Exception as error:
            logger.error(error)
            success = False

        if success:
            await interaction.response.send_message("Guild Added to the DB")
            button.disable()
        else:
            await interaction.response.send_message(resources_logic.get_string("ERROR_MESSAGES", "add_guild_error"))

    @discord.ui.button(label = "Remove", style = discord.ButtonStyle.red, row = 2)
    async def remove_guild(self, button, interaction: discord.Interaction):
        """
        Remove the guild from the DB
        """
        try:
            await database_connection.remove_guild(interaction.guild_id)
            success = True
        except Exception as error:
            logger.error(error)
            success = False

        if success:
            await interaction.response.send_message("Guild Removed from the DB")
            button.disable()
        else:
            await interaction.response.send_message(resources_logic.get_string("ERROR_MESSAGES", "remove_guild_error"))

        await interaction.response.send_message("Please contact a bot developer to have your guild removed")


class ServerCommandSelectionView(View):
    """
    View for the Server Command Selection
    """
    def __init__(self):
        super().__init__()
        self.selected_commands: list = []

    @discord.ui.select(
        placeholder = "Select the Commands you want enabled in the server",
        min_values = 1,
        max_values = 4,
        options = [
            discord.SelectOption(
                label = "Medical Commands",
                value = "medical_commands"
            ),
            discord.SelectOption(
                label = "Mining Commands",
                value = "mining_commands"
            ),
            discord.SelectOption(
                label = "aUEC Tracking Commands",
                value = "auec_commands"
            ),
            discord.SelectOption(
                label = "Trading Commands",
                value = "trading_commands"
            )
        ],
        row = 0
    )
    async def callback(self, select, interaction: discord.Interaction):
        """
        The Select menu
        """
        if not self.selected_commands:
            for value in select.values:
                if value not in self.selected_commands:
                    self.selected_commands.append(value)
                else:
                    self.selected_commands.remove(value)
            interaction.response.send_message(f"Selected Commands: {self.selected_commands}")
        else:
            for value in select.values:
                if value not in self.selected_commands:
                    self.selected_commands.append(value)
                else:
                    self.selected_commands.remove(value)
            interaction.response.edit_message(f"Selected Commands: {self.selected_commands}")

    @discord.ui.button(label = "Enable", style = discord.ButtonStyle.green, row = 1)
    async def enable_button(self, button, interaction: discord.Interaction):
        """
        Confirm the selection of the above menu.
        """
        await interaction.response.edit_message(f"Confirmed Command Selection. You have selected: {self.selected_commands}")
        try:
            await slash_logic.prepare_commands_to_update(interaction.guild_id, self.selected_commands, True)
            success = True
        except Exception as error:
            logger.error(error)
            success = False

        if success:
            await interaction.response.edit_message(content = "Selected commands have been enabled for this server!")
            button.disable()
        else:
            await interaction.response.edit_message(content = resources_logic.get_string("ERROR_MESSAGES", "add_commands_error"), view = self)

    @discord.ui.button(label = "Disable", style = discord.ButtonStyle.green, row = 1)
    async def disable_button(self, button, interaction: discord.Interaction):
        """
        Disable the selected commands
        """
        await interaction.response.edit_message(f"Disabling the following commands: {self.selected_commands}")
        try:
            await slash_logic.prepare_commands_to_update(interaction.guild_id, self.selected_commands, False)
            success = True
        except Exception as error:
            logger.error(error)
            success = False

        if success:
            await interaction.response.edit_message(content = "Selected commands have been disabled for this server!")
        else:
            await interaction.response.edit_message(content = resources_logic.get_string("ERROR_MESSAGES", "add_commands_error"), view = self)
