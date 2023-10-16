import os
import json
import subprocess
from turtle import down
import requests

from clone_assembla_repos import make_json_file_of_users_spaces, make_list_of_space_ids
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("ASSEMBLA_KEY")
api_secret = os.getenv("ASSEMBLA_SECRET")


def main():
    make_json_file_of_users_spaces(api_key, api_secret)
    list_of_space_ids = make_list_of_space_ids("data/users_spaces.json")
    make_json_of_spaces_documents(list_of_space_ids, "data/users_documents.json")
    download_documents("data/users_documents.json")


def make_json_of_spaces_documents(list, str):
    """
    Given a list of space ids and a file path, create a json file of all the documents in those spaces at the given file path
    """
    # Create empty JSON file
    with open(str, "w") as document_list:
        json.dump([], document_list)

    for space in list:
        # Run terminal command to access Assembla API and request the repo information of the Space
        get_documents = f"curl -H 'X-Api-Key: {api_key}' -H 'X-Api-Secret: {api_secret}' https://api.assembla.com/v1/spaces/{space}/documents.json"
        output_raw = subprocess.run(
            get_documents,
            shell=True,
            text=True,
            capture_output=True,
        ).stdout

        # Convert raw output to JSON if it is not an empty string
        if output_raw != "":
            output_json = json.loads(output_raw)

        # Open and then add to the JSON file
        with open(str, "r") as document_list:
            existing_data = json.load(document_list)
        existing_data.append(output_json)
        with open(str, "w") as document_list:
            json.dump(existing_data, document_list, indent=2)

    with open(str, "r") as document_list:
        document_list_content = json.load(document_list)
    return document_list_content


def download_documents(str):
    """
    Given a file path of a JSON file of document information, download all the docs into a folder
    """
    with open(str, "r") as document_list_json:
        document_list = json.load(document_list_json)

    headers = {"X-Api-Key": f"{api_key}", "X-Api-Secret": f"{api_secret}"}

    for space in document_list:
        for document in space:
            try:
                download_url = f"https://api.assembla.com/v1/spaces/{document['space_id']}/documents/{document['id']}/download"
            except:
                print(f"{document['id']}")
                pass

        response = requests.get(download_url, headers=headers)

        if response.status_code == 200:
            # Check the response headers to determine the file type and extension
            content_type = response.headers["Content-Type"]
            if content_type:
                # Extract the file extension from the content type
                file_extension = content_type.split("/")[-1]
                file_name = document["name"]

                # Save the file to your local directory
                with open(f"{file_name}.{file_extension}", "wb") as file:
                    file.write(response.content)
                print(f"File downloaded as {file_name}.{file_extension}")
            else:
                print("Unable to determine file type. Check the response headers.")
        else:
            print(f"Failed to download file. Status code: {response.status_code}")


if __name__ == "__main__":
    main()
