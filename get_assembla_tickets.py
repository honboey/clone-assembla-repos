import subprocess
import json
import os

from dotenv import load_dotenv

from clone_assembla_repos import make_json_file_of_users_spaces,  make_list_of_space_ids

load_dotenv()

api_key = os.getenv("ASSEMBLA_KEY")
api_secret = os.getenv("ASSEMBLA_SECRET")


def main():
    make_json_file_of_users_spaces(api_key, api_secret)
    list_of_space_ids = make_list_of_space_ids("data/users_spaces.json")
    get_spaces_tickets(list_of_space_ids, api_key, api_secret)


def get_spaces_tickets(lst, key, secret):
    """
    Given a list of space ids and your Assembla api key and secret, call the api and create a JSON of the tickets
    """

    for space_id in lst:
        call_api_for_spaces_tickets = f"curl -H 'X-Api-Key: {key}' -H 'X-Api-Secret: {secret}' https://api.assembla.com/v1/spaces/{space_id}/tickets.json"



