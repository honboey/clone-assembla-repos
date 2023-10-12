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
    get_ticket_comments("data/users_tickets.json")


def get_spaces_tickets(lst):
    """
    Given a list of space ids, call the api and create a JSON of the tickets
    """
    # Create empty JSON file
    with open("data/users_tickets.json", "w") as tickets:
        json.dump([], tickets)


    for space_id in lst:
        call_api_for_spaces_tickets = f"curl -H 'X-Api-Key: {api_key}' -H 'X-Api-Secret: {api_secret}' https://api.assembla.com/v1/spaces/{space_id}/tickets.json"
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
    
    return tickets_content


def get_ticket_comments(str):
    """
    Given a JSON file of tickets, create another JSON of each tickets corresponding comments.
    """
    # Open the JSON file of tickets
    with open(str, "r") as tickets:
        tickets_content = json.load(tickets)

    # Create empty JSON file
    with open("data/users_ticket_comments.json", "w") as ticket_comments:
        json.dump([], ticket_comments)


    for space in tickets_content:
        for ticket in space:
            call_api_for_ticket_comments = f"curl -H 'X-Api-Key: {api_key}' -H 'X-Api-Secret: {api_secret}' https://api.assembla.com/v1/spaces/{ticket['space_id']}/tickets/{ticket['number']}/ticket_comments.json"
            output_raw = subprocess.run(
                call_api_for_ticket_comments,
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
    
    return tickets_content



if __name__ == "__main__":
    main()

