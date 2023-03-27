"""
BRVNS Database Connection
Use this file to read and write from the database.
"""
import logging

import os

import firebase_admin
from firebase_admin import credentials, firestore, exceptions

logger = logging.getLogger()
logger.setLevel("INFO")

cred = credentials.Certificate(
    os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "../../.env/firebase_secret.json"
    )
)

firebase_admin.initialize_app(cred)
db = firestore.client()
logger.info("DB Connection created")

guild_col = db.collection("discord_guilds")
bound_col = db.collection("bound_users")


async def add_guild(guild_id: int, guild_name: str, spectrum_id: str):
    """
    Adds a guild to the DB
    """
    try:
        guild_ref = guild_col.document(f"{guild_id}")

        guild_ref.set(
            {
                "guild_name": guild_name,
                "guild_spectrum_id": spectrum_id,
                "guild_bank": [],  # Total Value, User, Change, Time/Date
                "member_info": {"verified_members": 0, "members": 0, "affiliates": 0},
            }
        )
        return True
    except exceptions.FirebaseError as exc:
        logger.warning("Failure in adding guild to DB")
        logger.warning(exc)
        return False


async def remove_guild(guild_id: int):
    """
    Remove the guild from the DB
    """
    try:
        doc_ref = guild_col.document(f"{guild_id}")
        doc_ref.delete()
        return True
    except exceptions.FirebaseError as exc:
        logger.warning("Failure in removing the guild from DB")
        logger.warning(exc)
        return False


async def get_user_verification_info(user_id):
    """
    Check the status of the users verification.
    """
    ref = bound_col.document(str(user_id))

    try:
        user_doc = ref.get().to_dict()
    except exceptions.FirebaseError as exc:
        logger.warning("Failure finding user information in Firebase")
        logger.warning(exc)

    if user_doc is not None:
        return user_doc

    return {"verification_step": "NOT STARTED"}


async def update_bound_user(user_id, new_value):
    """
    Update the info of the bound users verification info.
    """
    bound_user_ref = bound_col.document(f"{user_id}")
    bound_user_ref.update({"verification_step": new_value})


async def add_user_to_bound(author_id, rsi_handle, validation_string):
    """
    Add user to the bound users col.
    """
    bound_user_ref = bound_col.document(f"{author_id}")
    bound_user_ref.set(
        {
            "handle": rsi_handle,
            "verification_code": validation_string,
            "verification_step": "IN PROGRESS",
        }
    )


async def get_verified_user_list():
    ref = db.collection("bound_users")
    items = ref.select(field_paths=[]).get()
    ids = [item.id for item in items]
    return ids
