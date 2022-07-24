"""
BRVNS Discord Bot Logic
"""

from src.logic import resources_logic

# pylint: disable=too-few-public-methods
class BrvnsLogic():
    """
    BRVNS Bot Logic
    """
    resource = resources_logic

    def signup_string(self, author_name):
        """
        Return signup string
        """
        message_content: str = self.resource.get_resource("STRINGS", "signup_string")
        signup_string: str = f'Hello {author_name}. {message_content}'
        return str(signup_string)
