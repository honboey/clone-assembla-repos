import subprocess
import json
import os
import pprint

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("ASSEMBLA_KEY")
api_secret = os.getenv("ASSEMBLA_SECRET")


def main():
    filepath_of_users_spaces = input("What is the filepath of the JSON file that holds all your spaces? ")
    list_of_space_ids = make_list_of_space_ids(filepath_of_users_spaces)
    filepath_of_repos = input("Where do you want to save the JSON file of all your repos? ")
    make_json_of_spaces_repos(list_of_space_ids, filepath_of_repos)
    print(make_list_of_repo_urls(filepath_of_repos))


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

# Str -> List
# Given a JSON filepath of all the spaces a user belongs to, pull out the ID of each Space
def make_list_of_space_ids(str):
    list_of_space_ids = []
    with open(str, "r") as user_spaces_json:
        user_spaces = json.load(user_spaces_json)
    for space in user_spaces:
        list_of_space_ids.append(space["id"])
    return list_of_space_ids

# Lst, Str -> JSON
# Given a list of space ids and a file path, create a json file of all the repos in those spaces at the given file path
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

        # Convert raw output to JSON if it is not an empty string
        if output_raw != "":
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
# Given a file path of a JSON file which holds the repo information for all the spaces, extract the repo URLs and make a list
def make_list_of_repo_urls(str):
    list_of_repo_urls = []
    with open(str, "r") as repo_list:
        repo_list_content = json.load(repo_list)
    for space_repo in repo_list_content:
        for repo in space_repo:
            if type(repo) is dict:
                list_of_repo_urls .append(repo["ssh_clone_url"])
    return list_of_repo_urls 

# main()
make_json_file_of_users_spaces(api_key, api_secret)