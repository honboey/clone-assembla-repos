import subprocess
import json
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("ASSEMBLA_KEY")
api_secret = os.getenv("ASSEMBLA_SECRET")


# Str -> List
# Given a JSON filepath of all the spaces a user belongs to, pull out the ID of each Space
def make_list_of_spaces(str):
    list_of_spaces = []
    with open(str, "r") as user_spaces_json:
        user_spaces = json.load(user_spaces_json)
    for space in user_spaces:
        list_of_spaces.append(space["id"])
    return list_of_spaces


# Lst, Str -> JSON
# Given a list of space ids and a file path, create a json file of all the repos in those spaces
# ["space-id-1", "space-id-2", "space-id-3"], "file/path" -> JSON
def make_json_of_spaces_repos(list, str):
    # Create empty JSON file
    with open(str, "w") as repo_list:
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
        with open(str, "r") as repo_list:
            existing_data = json.load(repo_list)
        existing_data.append(output_json)
        with open(str, "w") as repo_list:
            json.dump(existing_data, repo_list, indent=2)

    with open(str, "r") as repo_list:
        repo_list_content = json.load(repo_list)
    return repo_list_content


# Str -> List
# Given a file path of a JSON file, extract the repo URLs and make a list
def make_list_of_github_repos(str):
    list_of_github_repos = []
    with open(str, "r") as repo_list:
        repo_list_content = json.load(repo_list)
    for space_repo in repo_list_content:
        for repo in space_repo:
            if type(repo) is dict:
                list_of_github_repos.append(repo["ssh_clone_url"])
    return list_of_github_repos
