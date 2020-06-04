"""
Program: test_programmer_toolkit.py
Author: Michael Skyberg, mskyberg@dmacc.edu
Last date modified: June 2020

Purpose: Test the programmer toolkit levels
"""


import unittest
import unittest.mock as mock
from main import programmer_toolkit as ptkit


class MyTestCase(unittest.TestCase):
    def test_sign_up_for_platinum(self):
        self.assertEqual("$60.00", ptkit.return_string_cost_of_box("Platinum"))

    def test_sign_up_user_input(self):
        # mock input from a user
        with mock.patch('builtins.input', side_effect=["Bronze"]):
            assert ptkit.sign_up_for_toolkit_box() == \
                   "Toolkit: Bronze cost: $30.00"


if __name__ == '__main__':
    pass
