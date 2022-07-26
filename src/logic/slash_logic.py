"""
BRVNS Discord Bot Logic
"""
import logging

import firebase_admin

from firebase_admin import credentials, firestore

from os import environ

from src.logic import resources_logic

logger = logging.getLogger(environ['LOGGER_NAME'])

cred = credentials.Certificate(environ['FIRESTORE_SECRET'])
firebase_admin.initialise_app(cred)
db = firestore.client()
logger.info("DB Connection created")

def signup_string(author_name: str):
    """
    Return signup string
    """
    message_content: str = resources_logic.get_string("SIGNUP", "signup_string")
    string_value: str = f"Hello {author_name}. {message_content}"

    return string_value
