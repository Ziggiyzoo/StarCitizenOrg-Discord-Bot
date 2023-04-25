"""
BRVNS Discord Bot Logic
"""
import logging
import time

import discord

from src.logic import rsi_lookup, resources_logic

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


async def update_users_roles(user_list, bot):
    """
    Update a users roles
    """
    for user_info in user_list:
        if user_info["verification_step"] == "VERIFIED":
            membership = await rsi_lookup.get_user_membership_info(user_info["handle"])
            if membership["main_member"] is not None:
                if membership["main_member"]:
                    membership_index = 0
                else:
                    membership_index = 1

                rank_index = int(membership["member_rank"])

                membership_list = ["BRVNS Member", "BRVNS Affiliate"]
                rank_list = [
                    "Prospective Employee",
                    "Junior",
                    "Senior",
                    "Managers",
                    "Directors",
                    "Board Members",
                ]

                # Update Org Membership and Ranks
                try:
                    guild = bot.get_guild(997138062381416589)
                    member = guild.get_member(int(user_info["user_id"]))
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
                time.sleep(5)
