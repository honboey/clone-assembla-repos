# Clone all Assembla repos

There are two python scripts in this repo:
1. `clone_assembla_repos.py`: This is a Python script that clones all your available Assembla repos. 
2. `get_assembla_tickets.py`: This is a Python script that grabs all the tickets in your Assembla spaces.

### Cloning Assembla repos
### How to use this script

#### 1. Install all the requirements
In your terminal run `pip install -r requirements.txt`. It may also be a good idea to setup a virtual environment before doing so.

#### 2. Register a new personal key in Assembla. 
To register a personal key in Assembla you will need to sign into your account and then go to `Account Information > Security > API Application & Sessions`. As of 9 Aug 2023, the direct link is https://app.assembla.com/user/edit/manage_clients.
Under "Register new personal key", give your key a description and tick "API access" and "Repository access"

#### 3. Add your API credentials to the Python script
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

#### 4. Run the script
Run the script by running `python clone_assembla_repos.py`. This will then clone all your repos into your directory.


### How the script works

1. The script grabs the JSON list of your spaces and spits out a list of all the Space IDs.
2. It then takes that list of Space IDs and for each space it makes a call to the Assembla API to get the repos for that space.
3. It then compiles a JSON file of all the repos that is has gathered.
4. That list of repos has a lot of information we don't need so the next step is to pull out just the repo URLs.
5. It then prints out that list of repo URLs in the terminal.

## Get Assembla tickets

### How to use this script

#### 1. Follow steps 1–3 in the above

#### 2. Run the script
Run the script by running `python get_assembla_tickets.py`. This will then create a JSON file of all your tickets in `/data`.
