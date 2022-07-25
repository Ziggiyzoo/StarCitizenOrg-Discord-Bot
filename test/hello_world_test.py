"""
Test to verify that the test framework is running.
"""

import unittest


class HelloWorldTestCase(unittest.TestCase):
    """
    Hello World Testcase Class
    """

    def test_hello_world(self):
        """
        Testcase to validate that the Tests are running
        """
        expected: str = "Hello, World!"
        actual: str = "Hello, World!"

        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
