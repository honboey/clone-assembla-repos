import json
import os
from clone_assembla_repos import (
    make_json_file_of_users_spaces,
    make_list_of_space_ids,
    make_json_of_spaces_repos,
    make_list_of_repo_urls,
)
from get_assembla_tickets import get_spaces_tickets, get_ticket_comments
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("ASSEMBLA_KEY")
api_secret = os.getenv("ASSEMBLA_SECRET")

# Test data
with open("data/test-data/test_json_of_spaces.json", "r") as test_json_of_spaces_file:
    test_json_of_spaces = json.load(test_json_of_spaces_file)


test_list_of_spaces_ids = [
    "bHeZE2SX4r3PYIeJe5afGb",
    "a9LKRAvAWr4ir7eJe5cbLA",
    "cXCJzAC5Sr4i7WeJe5cbCb",
]

test_list_of_repo_urls = [
    "https://git.assembla.com/abacus.git",
    "https://git.assembla.com/abc-moma.git",
]

with open(
    "data/test-data/test_repo_list_result.json", "r"
) as test_repo_list_result_json:
    test_spaces_repos = json.load(test_repo_list_result_json)

with open(
    "data/test-data/test_ticket_list.json", "r"
) as test_ticket_list:
    test_tickets = json.load(test_ticket_list)

with open(
    "data/test-data/test_ticket_comments.json", "r"
) as test_ticket_comments:
    test_ticket_comments_content = json.load(test_ticket_comments)


# Tests


def test_make_json_file_of_users_spaces():
    assert make_json_file_of_users_spaces(api_key, api_secret) == test_json_of_spaces


def test_make_list_of_space_ids():
    assert (
        make_list_of_space_ids("data/test-data/test_spaces.json")
        == test_list_of_spaces_ids
    )


def test_make_json_of_spaces_repos():
    assert (
        make_json_of_spaces_repos(
            test_list_of_spaces_ids, "data/test-data/test_repo_list.json"
        )
        == test_spaces_repos
    )


def test_make_list_of_repo_urls():
    assert (
        make_list_of_repo_urls("data/test-data/test_repo_list.json")
        == test_list_of_repo_urls
    )


def test_make_list_of_repo_urls__remove_unwanted_repos():
    assert (
        make_list_of_repo_urls("data/test-data/test_repo_list--unwanted_repos.json")
        == test_list_of_repo_urls
    )


def test_get_spaces_tickets():
    assert (
        get_spaces_tickets(test_list_of_spaces_ids)
        == test_tickets
    )


def test_get_ticket_comments():
    assert (
        get_ticket_comments("data/test-data/test_ticket_list.json")
        == test_ticket_comments_content
    )