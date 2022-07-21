"""
Test to verify that the test framework is running.
"""

import unittest
from src.brvns_bot_logic import BrvnsLogic


class SignupStringTestCase(unittest.TestCase):
    """
    Signup String Testcase Class
    """
    def test_signup_string(self):
        """
        Testcase to validate that the correct string format is returned when sign up command is used
        """
        expected: str = "Hello Ziggiyzoo. To signup to the Blue Ravens Org, visit: https://robertsspaceindustries.com/orgs/BRVNS."
        actual: str = BrvnsLogic.signup_string("Ziggiyzoo")

        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
