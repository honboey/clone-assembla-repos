# Clone all Assembla repos

This is a Python script that clones all your available Assembla repos. It is currently a work in progress.

## How to use this script

### 1. Install all the requirements
In your terminal run `pip install -r requirements.txt`. It may also be a good idea to setup a virtual environment before doing so.

### 2. Register a new personal key in Assembla. 
To register a personal key in Assembla you will need to sign into your account and then go to `Account Information > Security > API Application & Sessions`. As of 9 Aug 2023, the direct link is https://app.assembla.com/user/edit/manage_clients.
Under "Register new personal key", give your key a description and tick "API access" and "Repository access"

### 3. Add your API credentials to the Python script
Create a `.env` file in the root directory of the project. In this file paste the following lines:
```
ASSEMBLA_KEY="<key>"
ASSEMBLA_SECRET="<secret>"
```
where `<key>` is your key and `secret` is your secret.

For example, if your key was `1234` and your secret was `5678` then your code would like like this:
```
ASSEMBLA_KEY="1234"
ASSEMBLA_SECRET="5678"
```

### 4. Get a list of all the spaces you are a member of.
We now need to create a JSON file of all the spaces that you are a member of. 

In your terminal, the following command is the template to access the Assembla API.
```
curl -H "X-Api-Key: <key>" -H "X-Api-Secret: <secret>" https://api.assembla.com/<path to resource>.json
```
We need to get a list of all the spaces you are a member of. By using the above template we can use this command to do so:
```
curl -H "X-Api-Key: <key>" -H "X-Api-Secret: <secret>" https://api.assembla.com/v1/spaces.json
```

Run the above command, remembering to replace `<key>` and `<secret>` with your Assembla key and secret that you got in step 1.

### 5. Save this list of spaces as a JSON file
Running the above command should spit out a JSON formatted list of all the spaces you are a member of. Copy and paste this into a document and save it as a `.json` file.

### 6. Run the python script
Run the python script using `python close-assembla-repos.py`.

### 7. Follow the prompts
The first prompt the script will ask is:
>What is the filepath of the JSON file that holds all your spaces?

Answer this by inputting the filepath of the JSON file you just created in step 5

The second prompt is:
>Where do you want to save the JSON file of all your repos?

The script is creating a new JSON file and needs to know where to put it. Give it a filepath and filename, for example `path/to/json/file.json`. Make sure to end the filename in `.json`.


## How the script works

1. The script grabs the JSON list of your spaces and spits out a list of all the Space IDs.
2. It then takes that list of Space IDs and creates a JSON file of all the repos in those spaces
3. That list of repos has a lot of information we don't need so the next step is to pull out just the repo URLs.
4. It then prints out that list in the terminal for you.
