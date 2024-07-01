#!/usr/bin/env python3
"""
A module for testing the client module.

This module contains unit and integration tests for the
GithubOrgClient class.
"""

from typing import Dict
from unittest import TestCase
from unittest.mock import MagicMock, PropertyMock, patch

from parameterized import parameterized

from client import GithubOrgClient


class TestGithubOrgClient(TestCase):
    """Tests the githubOrgClient class."""

    @parameterized.expand(
        [
            ("google", {"login": "google"}),
            ("abc", {"login": "abc"}),
        ]
    )
    @patch("client.get_json")
    def test_org(
        self, org: str, response: Dict[str, str], mocked_org_method: MagicMock
    ) -> None:
        """Tests the 'org' method."""
        mocked_org_method.return_value = response
        get_org_client = GithubOrgClient(org)
        self.assertEqual(get_org_client.org, response)
        mocked_org_method.assert_called_once_with(
            f"https://api.github.com/orgs/{org}")

    def test_public_repos_url(self):
        """Tests the _public_repos_url property."""
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock) as mocked_property:
            mocked_property.return_value = {
                "repos_url": "https://api.github.com/orgs/google/repos"
            }
            self.assertEqual(GithubOrgClient(
                "google")._public_repos_url,
                "https://api.github.com/orgs/google/repos",)
