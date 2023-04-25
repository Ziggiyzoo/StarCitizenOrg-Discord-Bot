"""
BRVNS Discord Bot Logic
"""
import logging
import time

import discord

from src.logic import database_connection, rsi_lookup, resources_logic

logger = logging.getLogger()
logger.setLevel("INFO")


async def signup_string(author_name: str):
    """
    Return signup string
    """
    message_content: str = resources_logic.get_string("SIGNUP", "signup_string")
    string_value: str = f"Hello {author_name}. {message_content}"
    logger.info("Signup string value:")
    logger.info(string_value)

    return string_value


async def update_users_roles(id_list, bot, ctx):
    """
    Update a users roles
    """
    for member_id in id_list:
        user_info = await database_connection.get_user_verification_info(member_id)
        if user_info["verification_step"] == "VERIFIED":
            membership = await rsi_lookup.get_user_membership_info(user_info["handle"])
            if membership["main_member"] is not None:
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

                # Update Org Membership and Ranks
                start2 = time.time()
                try:
                    guild = bot.get_guild(997138062381416589)
                    member = guild.get_member(int(member_id))
                    await member.add_roles(
                        *[
                            discord.utils.get(
                                guild.roles, name=membership_list[membership_index]
                            ),
                            discord.utils.get(guild.roles, name=rank_list[rank_index]),
                        ]
                    )
                    await member.remove_roles(
                        discord.utils.get(
                            guild.roles, name=membership_list[membership_index - 1]
                        )
                    )
                    for i in [1, 2, 3, 4, 5]:
                        await member.remove_roles(
                            discord.utils.get(
                                guild.roles, name=rank_list[rank_index - i]
                            )
                        )
                except AttributeError as error:
                    logger.error(error)

                logger.info(time.time() - start2)
                time.sleep(5)

        if ctx is not None:
            ctx.respond("Roles have been updated.")
