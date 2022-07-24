"""
Test to verify that the test framework is running.
"""

import unittest

from src.logic import resources_logic, slash_logic


class SlashLogicTestCase(unittest.TestCase):
    """
    Signup String Testcase Class
    """

    def test_signup_string(self):
        """
        Testcase to validate that the correct string format is returned when sign up command is used
        """
        expected = resources_logic.get_string("TEST_EXPECTED", "string.test_signup_string")
        actual = slash_logic.signup_string("Ziggiyzoo")

        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
