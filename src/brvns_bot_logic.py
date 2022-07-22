"""
BRVNS Discord Bot Logic
"""

from src.brvns_resources import BrvnsResources


class BrvnsLogic():
    """
    BRVNS Bot Logic
    """
    brvns_config = BrvnsResources()

    def signup_string(self, author_name):
        """
        Return signup string
        """
        message_content = self.brvns_config.get_config("STRINGS", "signup_string")
        signup_string = f'Hello {author_name}. {message_content}'
        return str(signup_string)

    def add_extra_public_method(self):
        """
        Satisfy pylints desire for control
        """
        return "We love you pylint"
