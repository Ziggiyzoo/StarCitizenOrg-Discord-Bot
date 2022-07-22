"""
BRVNS Discord Bot Logic
"""

import src.brvns_resources

# pylint: disable=too-few-public-methods
class BrvnsLogic():
    """
    BRVNS Bot Logic
    """
    brvns_resources = src.brvns_resources

    def signup_string(self, author_name):
        """
        Return signup string
        """
        message_content: str = self.brvns_resources.get_config("STRINGS", "signup_string")
        signup_string: str = f'Hello {author_name}. {message_content}'
        return str(signup_string)
