"""
BRVNS Slash Cogs
"""
import logging

import discord
from discord.ext import commands

from src.logic import slash_logic, database_connection, rsi_lookup, resources_logic

logger = logging.getLogger()
logger.setLevel("INFO")


class SlashBrvns(commands.Cog):
    """
    BRVNS Slash Cogs
    """

    def __init__(self, bot):
        self.bot: commands.Bot = bot
        logger.info("Init Brvns Slash Command Cog")

    @commands.slash_command(
        name="sign-up", description="Display the link to the RSI Org Page."
    )
    async def sign_up(self, ctx):
        """
        Sign Up string slash command
        """
        author_name: str = ctx.author.name
        await ctx.respond(await slash_logic.signup_string(author_name))

    # pylint: disable=no-member
    @commands.slash_command(
        name="verify-discord", descriptions="Bind discord user to RSI Account."
    )
    async def verify_discord(self, ctx, rsi_handle: discord.Option(str)):
        """
        Verify if the discord member is a member of the RSI Org.
        """
        author_id: int = ctx.author.id
        await ctx.defer()
        # Check if this is the first time the user has done this.
        user_info = await database_connection.get_user_verification_info(author_id)

        if user_info["verification_step"] == "VERIFIED":
            await ctx.followup.send(
                "Your RSI Handle and Discord are already bound.",
                ephemeral=True,
            )

        elif user_info["verification_step"] == "IN PROGRESS":
            success = await rsi_lookup.get_rsi_handle_info(
                user_info["handle"], user_info["verification_code"]
            )
            if success:
                await ctx.followup.send(
                    "Thank you for binding your RSI and Discord accounts."
                    + "Please use /update-roles to get your roles update in the server.",
                    ephemeral=True,
                )
                await ctx.author.add_roles(
                    discord.utils.get(ctx.guild.roles, name="Verified")
                )
                await ctx.author.remove_roles(
                    discord.utils.get(ctx.guild.roles, name="Unverified")
                )
                try:
                    await ctx.author.edit(nick=user_info["handle"])
                except discord.errors.Forbidden as error:
                    logger.error(error)
                await database_connection.update_bound_user(author_id, "VERIFIED")
            else:
                await ctx.followup.send(
                    "Please Make sure that you have added the verification code to your RSI Profile BIO."
                    + "\nYour code is "
                    + user_info["verification_code"],
                    ephemeral=True,
                )
        else:
            valid_handle = await rsi_lookup.check_rsi_handle(rsi_handle)

            if valid_handle is not None:
                validation_string = str(resources_logic.create_random_string())
                await database_connection.add_user_to_bound(
                    author_id, valid_handle, validation_string
                )
                await ctx.followup.send(
                    "Your RSI Handle is Valid, please put the following in your Bio: "
                    + validation_string
                    + "\n\nPlease run this command again after you have done this.",
                    ephemeral=True,
                )

            else:
                await ctx.followup.send(
                    "The RSI Handle you entered is invalid, please try again.",
                    ephemeral=True,
                )

    @commands.slash_command(
        name="update-roles",
        descriptions="Update your roles and rank in the discord if any changes have been made.",
    )
    async def update_roles(self, ctx):
        """
        Verify if the user is a member of the BRVNS Org and assign roles accordingly.
        """
        author_id: int = ctx.author.id
        user_info = await database_connection.get_user_verification_info(author_id)
        await slash_logic.update_users_roles([user_info], self.bot)

    @commands.slash_command(name="ping", description="Return the bot latency.")
    async def ping(self, ctx):
        """
        Send bot ping
        """
        await ctx.respond(f"Pong! Latency is {round(self.bot.latency * 100, 2)} ms")
        logger.info("Sent Ping")

    @commands.Cog.listener()
    async def on_ready(self):
        """
        Cog on Ready
        """
        logger.info("BRVNS Cogs: READY")


def setup(bot):
    """
    Add cog to bot
    """
    bot.add_cog(SlashBrvns(bot))
