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
    # Create empty JSON file
    with open("data/users_tickets.json", "w") as tickets:
        json.dump([], tickets)


    for space_id in lst:
        call_api_for_spaces_tickets = f"curl -H 'X-Api-Key: {key}' -H 'X-Api-Secret: {secret}' https://api.assembla.com/v1/spaces/{space_id}/tickets.json"
        output_raw = subprocess.run(
            call_api_for_spaces_tickets,
            shell=True,
            text=True,
            capture_output=True,
        ).stdout

        # Convert raw output to JSON if it is not an empty string
        if output_raw != "":
            output_json = json.loads(output_raw)

        # Open and then add to the JSON file
        with open("data/users_tickets.json", "r") as tickets:
            existing_data = json.load(tickets)
        existing_data.append(output_json)
        with open("data/users_tickets.json", "w") as tickets:
            json.dump(existing_data, tickets, indent=2)

    with open("data/users_tickets.json", "r") as tickets:
        tickets_content = json.load(tickets)


if __name__ == "__main__":
    main()

