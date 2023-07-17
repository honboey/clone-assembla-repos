# JSON -> List
# Given a JSON file of Space information, pull out the ID of each Space


def make_list_of_spaces(json):
    list_of_spaces = []
    for space in json:
        list_of_spaces.append(space["id"])
    return list_of_spaces


# List -> JSON 
# Given a list of space ids, create a list of all the repos in those spaces
# ["space-id-1", "space-id-2", "space-id-3"] -> [""]
def make_json_of_spaces_repos(list):
    ...
    