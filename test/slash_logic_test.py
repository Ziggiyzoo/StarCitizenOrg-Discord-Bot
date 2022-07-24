"""
Test to verify that the test framework is running.
"""

import unittest
from src.logic.slash_logic import BrvnsLogic
from src.logic import resources_logic



class SlashLogicTestCase(unittest.TestCase):
    """
    Signup String Testcase Class
    """
    resource = resources_logic
    logic: BrvnsLogic =  BrvnsLogic()

    def test_signup_string(self):
        """
        Testcase to validate that the correct string format is returned when sign up command is used
        """
        expected = self.resource.get_resource("TEST_EXPECTED", "string.test_signup_string")
        actual = self.logic.signup_string("Ziggiyzoo")

        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
