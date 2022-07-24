"""
For each type of data in the resource.ini file. Test.
"""

import unittest

from src.logic import resources_logic


class ResourcesLogicTestCase(unittest.TestCase):
    """
    Signup String Testcase Class
    """

    def test_get_string_resource(self):
        """
        Testcase to validate that the correct string format is returned
        """
        expected: str = "This is the test string."
        actual: str = resources_logic.get_string("TEST", "string.string_test", testing=True)

        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
