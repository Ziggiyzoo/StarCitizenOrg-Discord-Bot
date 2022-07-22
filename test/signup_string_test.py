"""
Test to verify that the test framework is running.
"""

import unittest
from src.brvns_bot_logic import BrvnsLogic
from src.brvns_config import BrvnsConfig



class SignupStringTestCase(unittest.TestCase):
    """
    Signup String Testcase Class
    """
    brvns_config = BrvnsConfig()

    def test_signup_string(self):
        """
        Testcase to validate that the correct string format is returned when sign up command is used
        """
        message_content = self.brvns_config.get_config("StringsSection", "string.signup_string")
        expected: str = f"Hello Ziggiyzoo. {message_content}"
        actual: str = BrvnsLogic.signup_string("Ziggiyzoo")

        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
