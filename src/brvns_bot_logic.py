"""
BRVNS Discord Bot Logic
"""

class BrvnsLogic():
    """
    BRVNS Bot Logic
    """

    def signup_string(self, author_name):
        """
        Return signup string
        """
        signup_string = f"Hello {author_name}. "
        signup_string += "To signup to the Blue Ravens Org, visit: https://robertsspaceindustries.com/orgs/BRVNS."
        return str(signup_string)
    
    def add_extra_public_method(self):
        """
        Satisfy pylints desire for control
        """
        return "We love you pylint"