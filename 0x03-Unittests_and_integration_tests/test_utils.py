#!/usr/bin/env python3
"""
A Module for testing the utils module.

This module contains tests for the following functions:
- access_nested_map
"""

from typing import Dict, Tuple, Type, Union
from unittest import TestCase

from parameterized import parameterized

from utils import access_nested_map


class TestAccessNestedMap(TestCase):
    """Tests the 'access_nested_map' function."""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(
        self,
        nested_map: Dict[str, Union[Dict, int]],
        path: Tuple[str, ...],
        expected: Union[Dict[str, int], int],
    ) -> None:
        """Test 'access_nested_map' output."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand(
        [
            ({}, ("a",), KeyError),
            ({"a": 1}, ("a", "b"), KeyError),
        ]
    )
    def test_access_nested_map_exception(
        self,
        nested_map: Dict[str, Union[Dict, int]],
        path: Tuple[str, ...],
        exception: Type[BaseException],
    ) -> None:
        """Tests 'access_nested_map' exception raising."""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)
