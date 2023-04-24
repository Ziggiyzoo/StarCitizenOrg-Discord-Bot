"""
Background tasks to loop for the bot.
"""
import logging
import time

import discord
from discord.ext import commands, tasks

from src.logic import database_connection, rsi_lookup

logger = logging.getLogger()
logger.setLevel("INFO")


class BackgroundTasks(commands.Cog):
    """
    Background Tasks
    """

    def __init__(self, bot):
        self.bot: commands.Bot = bot
        logger.info("Init Background Tasks Cog")
        # pylint: disable=E1101
        self.update_membership_and_roles.start()

    # pylint: disable=R0914
    @tasks.loop(hours=6)
    async def update_membership_and_roles(self):
        """
        A background loop to update roles and membership automatically
        """
        logger.info("Running role update task.")
        start = time.time()
        id_list = await database_connection.get_verified_user_list()
        for member_id in id_list:
            user_info = await database_connection.get_user_verification_info(member_id)
            logger.info("Getting user info took " + str(time.time() - start))
            membership = await rsi_lookup.get_user_membership_info(user_info["handle"])
            if membership["main_member"]:
                membership_index = 0
            else:
                membership_index = 1

            rank_index = int(membership["member_rank"]) - 1

            membership_list = ["BRVNS Member", "BRVNS Affiliate"]
            rank_list = [
                "Board Members",
                "Directors",
                "Managers",
                "Senior",
                "Junior",
                "Prospective Employee",
            ]

            # Check the org membership status and rank
            try:
                guild = self.bot.get_guild(997138062381416589)
                member = guild.get_member(int(member_id))
                await member.add_roles(
                    *[
                        discord.utils.get(
                            guild.roles, name=membership_list[membership_index]
                        ),
                        discord.utils.get(guild.roles, name=rank_list[rank_index]),
                    ]
                )
            except AttributeError as error:
                logger.error(error)

        end = time.time()
        time_taken = round(end - start, 2)
        channel = self.bot.get_channel(1071924147501928558)
        await channel.send(
            f"Ranks and Membership have been updated. This took: {time_taken} s"
        )
        logger.info("Ranks and Membership have been updated.")

    @update_membership_and_roles.before_loop
    async def wait_until_ready(self):
        """
        Wait until bot is ready
        """
        await self.bot.wait_until_ready()

    def cog_unload(self):
        """
        Cancel the background tasks if the cog is unloaded.
        """
        # pylint: disable=E1101
        self.update_membership_and_roles.cancel()

    @commands.Cog.listener()
    async def on_ready(self):
        """
        Cog on Ready
        """
        logger.info("Background Tasks Cog: READY")


def setup(bot):
    """
    Add cog to bot
    """
    bot.add_cog(BackgroundTasks(bot))
