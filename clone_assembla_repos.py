import subprocess
import json
import os

api_key = os.getenv("ASSEMBLA_KEY")
api_secret = os.getenv("ASSEMBLA_SECRET")


# JSON -> List
# Given a JSON file of Space information, pull out the ID of each Space


def make_list_of_spaces(json):
    list_of_spaces = []
    for space in json:
        list_of_spaces.append(space["id"])
    return list_of_spaces


# Lst, Str -> JSON
# Given a list of space ids and a file path, create a json file of all the repos in those spaces
# ["space-id-1", "space-id-2", "space-id-3"], "file/path" -> JSON
def make_json_of_spaces_repos(list, str):
    # Create empty JSON file
    repo_list_file = str
    with open(repo_list_file, "w") as repo_list:
        json.dump([], repo_list)

    for space in list:
        # Run terminal command to access Assembla API and request the repo information of the Space
        get_repos = f"curl -H 'X-Api-Key: {api_key}' -H 'X-Api-Secret: {api_secret}' https://api.assembla.com/v1/spaces/{space}/repos.json"
        output_raw = subprocess.run(
            get_repos,
            shell=True,
            text=True,
            capture_output=True,
        ).stdout

        # Convert raw output to JSON
        output_json = json.loads(output_raw)

        # Open and then add to the JSON file
        with open(repo_list_file, "r") as repo_list:
            existing_data = json.load(repo_list)
        existing_data.append(output_json)
        with open(repo_list_file, "w") as repo_list:
            json.dump(existing_data, repo_list, indent=2)

    with open(repo_list_file, "r") as repo_list:
        repo_list_content = json.load(repo_list)
    return repo_list_content

