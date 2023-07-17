import json
from clone_assembla_repos import (
    make_list_of_spaces,
    make_json_of_spaces_repos,
)

# Test data
with open("data/test-data/test_spaces.json", "r") as test_spaces_contents:
    test_spaces = json.load(test_spaces_contents)

with open("data/test-data/test_spaces_repos.json", "r") as test_spaces_repos_contents:
    test_spaces_repos = json.load(test_spaces_repos_contents)

test_list_of_spaces_ids = [
        "bHeZE2SX4r3PYIeJe5afGb",
        "a9LKRAvAWr4ir7eJe5cbLA",
        "cXCJzAC5Sr4i7WeJe5cbCb",
    ]

def test_make_list_of_spaces():
    assert make_list_of_spaces(test_spaces) == test_list_of_spaces_ids

def test_make_json_of_spaces_repos():
    assert make_json_of_spaces_repos(test_list_of_spaces_ids) == test_spaces_repos