"""
Test to verify that the test framework is running.
"""

import unittest
from src.brvns_bot_logic import BrvnsLogic
from src.brvns_resources import BrvnsResources



class SignupStringTestCase(unittest.TestCase):
    """
    Signup String Testcase Class
    """
    brvns_resources = BrvnsResources()
    brvns_logic = BrvnsLogic()

    def test_signup_string(self):
        """
        Testcase to validate that the correct string format is returned when sign up command is used
        """
        expected = self.brvns_resources.get_config("STRINGS", "string.test_signup_string")
        actual = self.brvns_logic.signup_string("Ziggiyzoo")

        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
