#!/usr/bin/env python3
""" Unittests for utils.py """


from utils import access_nested_map
import unittest
import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """ class to test access_nested_map """

    @parameterized.expand([
        ({"a": 1}, ("a",)), 1,
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, result):
        """ Test access_nested_map """
        self.assertEqual(access_nested_map(nested_map, path), result)
