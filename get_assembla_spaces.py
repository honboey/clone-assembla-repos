import subprocess
import json
import os

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("ASSEMBLA_KEY")
api_secret = os.getenv("ASSEMBLA_SECRET")


def main():
    make_json_file_of_users_spaces(api_key, api_secret)


def make_json_file_of_users_spaces(key, secret):
    call_api_for_json_of_spaces = f"curl -H 'X-Api-Key: {key}' -H 'X-Api-Secret: {secret}' https://api.assembla.com/v1/spaces.json"
    output_raw = subprocess.run(
        call_api_for_json_of_spaces,
        shell=True,
        text=True,
        capture_output=True,
    ).stdout

    # Remove all the `\\r\\n` from output_raw
    parsed_data = json.loads(output_raw)
    with open("data/users_spaces.json", "w") as json_of_users_spaces:
        json.dump(parsed_data, json_of_users_spaces, indent=4)
    return parsed_data


# Str -> List
def make_list_of_space_ids(str):
    """
    Given a JSON filepath of all the spaces a user belongs to, pull out the ID of each Space
    """
    list_of_space_ids = []
    with open(str, "r") as user_spaces_json:
        user_spaces = json.load(user_spaces_json)
    for space in user_spaces:
        list_of_space_ids.append(space["id"])
    return list_of_space_ids


if __name__ == "__main__":
    main()