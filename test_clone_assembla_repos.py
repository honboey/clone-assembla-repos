import json
from clone_assembla_repos import (
    make_list_of_spaces,
    make_json_of_spaces_repos,
    make_list_of_github_repos,
)

# Test data
with open("data/test-data/test_spaces.json", "r") as test_spaces_contents:
    test_spaces = json.load(test_spaces_contents)

with open("data/test-data/test_repo_list.json", "r") as test_repos_list_contents:
    test_spaces_repos = json.load(test_repos_list_contents)

test_list_of_spaces_ids = [
    "bHeZE2SX4r3PYIeJe5afGb",
    "a9LKRAvAWr4ir7eJe5cbLA",
    "cXCJzAC5Sr4i7WeJe5cbCb",
]

test_list_of_repo_urls = [
    "git@git.assembla.com:abacus.git",
    "git@git.assembla.com:abc-moma.git",
]


def test_make_list_of_spaces():
    assert make_list_of_spaces(test_spaces) == test_list_of_spaces_ids


def test_make_json_of_spaces_repos():
    assert (
        make_json_of_spaces_repos(
            test_list_of_spaces_ids, "data/test-data/test_repo_list.json"
        )
        == test_spaces_repos
    )


def test_make_list_of_github_repos():
    assert (
        make_list_of_github_repos("data/test-data/test_repo_list.json")
        == test_list_of_repo_urls
    )