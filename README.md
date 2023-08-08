# Clone all Assembla repos

(WIP) This is a Python script that clones all your available Assembla repos

## Setup 

1. Register a new personal key in Assembla. Make sure you enable API and Repository access.

2. Export a JSON list of all the spaces you are a member of.
In your terminal, the following command is the template to access the Assembla API.
```
curl -H "X-Api-Key: <key>" -H "X-Api-Secret: <secret>" https://api.assembla.com/<path to resource>.json
```
We need to get a list of all the spaces you are a member of. By using the above template we can use this command to do so:
```
curl -H "X-Api-Key: <key>" -H "X-Api-Secret: <secret>" https://api.assembla.com/v1/spaces.json
```

3. Run the python script

## How the script works

1. The script grabs the JSON list of your spaces and spits out a list of all the Space IDs.
2. It then takes that list of Space IDs and creates a JSON file of all the GitHub repos in those spaces
3. That list of GitHub repos has a lot of information we don't need so the next step is to pull out the repo URLs.
4. It then uses that list of GitHub repo URLs and clones them to your computer.
