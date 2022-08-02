"""
BRVNS Database Connection
Use this file to read and write from the database.
"""
import logging

import firebase_admin

import os

from firebase_admin import credentials, firestore

from os import environ

logger = logging.getLogger(environ['LOGGER_NAME'])

cred = credentials.Certificate( os.path.join(
                                    os.path.dirname(
                                        os.path.abspath(__file__)
                                    ),
                                    "../../.env/firebase_secret.json"
                                )
                            )

firebase_admin.initialize_app(cred)
db = firestore.client()
logger.info("DB Connection created")

guild_col = db.collection("discord_guilds")

async def add_guild(guild_id: int, guild_name: str):
    """
    Adds a guild to the DB
    """
    guild_ref = guild_col.document(f"{guild_id}")

    guild_ref.set({
        "guild_name" : guild_name,
        "enabled_commands" : {
            "mining_commands" : False,
            "medical_commands" : False,
            "auec_commands" : False,
            "trading_commands" : False
        },
        "guild_bank" : [], # Total Value, User, Change, Time/Date
        "member_info" : {
            "verified_members" : 0,
            "members" : 0,
            "affiliates" : 0
        }
    })

async def update_enabled_commands(guild_id: int, command_states: dict):
    """
    Updates the enabled commands
    """

    doc_ref = guild_col.document(f"{guild_id}")
    doc_ref.update({
        "enabled_commands" : {
            "mining_commands" : command_states["mining_commands"],
            "medical_commands" : command_states["medical_commands"],
            "auec_commands" : command_states["auec_commands"],
            "trading_commands" : command_states["trading_commands"]
        }
    })

async def get_enabled_commands(guild_id: int):
    """
    Get a list of enabled commands
    """

    doc_ref = guild_col.document(f"{guild_id}")
    doc = doc_ref.get()
    if doc.exists:
        doc_obj: dict = doc.to_dict()
        return doc_obj.get("enabled_commands")
    else:
        raise Exception(f"Guild Doc {guild_id} does not Exist")
