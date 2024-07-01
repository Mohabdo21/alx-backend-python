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

    @patch("client.get_json")
    def test_public_repos(self, mocked_get_json: MagicMock):
        """Tests the public_repos method."""
        test_payload = {
            "repos_url": "https://api.github.com/orgs/google/repos",
            "repos": [
                {
                    "id": 7697149,
                    "node_id": "MDEwOlJlcG9zaXRvcnk3Njk3MTQ5",
                    "name": "episodes.dart",
                    "full_name": "google/episodes.dart",
                    "private": False,
                    "forks": 22,
                    "open_issues": 0,
                    "watchers": 12,
                    "default_branch": "master",
                    "permissions": {
                        "admin": False,
                        "push": False,
                        "pull": True
                    }
                },
                {
                    "id": 7776515,
                    "node_id": "MDEwOlJlcG9zaXRvcnk3Nzc2NTE1",
                    "name": "cpp-netlib",
                    "full_name": "google/cpp-netlib",
                    "private": False,
                    "forks": 59,
                    "open_issues": 0,
                    "watchers": 292,
                    "default_branch": "master",
                    "permissions": {
                        "admin": False,
                        "push": False,
                        "pull": True
                    }
                },
            ]
        }
        mocked_get_json.return_value = test_payload["repos"]
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mocked_public_repos_url:
            mocked_public_repos_url.return_value = test_payload["repos_url"]
            self.assertEqual(GithubOrgClient("google").public_repos(), [
                             "episodes.dart", "cpp-netlib"])
            mocked_public_repos_url.assert_called_once()
        mocked_get_json.assert_called_once()

    @parameterized.expand(
        [
            ({"license": {"key": "apache-2.0"}}, "apache-2.0", True),
            ({"license": {"key": "apache-2.0"}}, "bsd-3-clause", False),
        ]
    )
    def test_has_license(self,
                         repo: Dict[str, Dict[str, str]],
                         key: str, expected: bool) -> None:
        """Tests for 'has_license' method."""
        mocked_org_client = GithubOrgClient("google")
        client_has_license = mocked_org_client.has_license(repo, key)
        self.assertEqual(client_has_license, expected)
