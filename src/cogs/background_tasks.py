"""
Background tasks to loop for the bot.
"""
import logging
import time

from discord.ext import commands, tasks

from src.logic import slash_logic, database_connection

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
        user_list = []
        for member_id in id_list:
            user_list.append(
                await database_connection.get_user_verification_info(member_id)
            )
        await slash_logic.update_users_roles(user_list, self.bot, None)
        end = time.time()
        time_taken = round(end - start, 2)
        channel = self.bot.get_channel(1071924147501928558)
        await channel.send(
            f"Ranks and Membership have been updated. This took: {time_taken} s"
        )
        logger.info("@silent Ranks and Membership have been updated.")

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
