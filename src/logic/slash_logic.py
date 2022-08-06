"""
BRVNS Discord Bot Logic
"""
import logging

from os import environ

from src.logic import resources_logic, database_connection

logger = logging.getLogger(environ['LOGGER_NAME'])

async def signup_string(author_name: str):
    """
    Return signup string
    """
    message_content: str = resources_logic.get_string("SIGNUP", "signup_string")
    string_value: str = f"Hello {author_name}. {message_content}"

    return string_value

async def prepare_commands_to_update(guild_id:int , commands_to_enable: list, enable: bool):
    """
    Prepare the list of commands
    """
    try:
        current_commands: dict = await database_connection.get_enabled_commands(guild_id)
        skip = False
    except Exception as error:
        logger.warning(error)
        skip = True

    if not skip:
        for each in commands_to_enable:
            current_commands[each] = enable

        await database_connection.update_enabled_commands(guild_id, current_commands)
