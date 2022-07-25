"""
BRVNS Discord Bot Logic
"""

from src.logic import resources_logic


def signup_string(author_name: str):
    """
    Return signup string
    """
    message_content: str = resources_logic.get_string("SIGNUP", "signup_string")
    string_value: str = f"Hello {author_name}. {message_content}"

    return string_value
