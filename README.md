# Clone all Assembla repos

(WIP) This is a Python script that clones all your available Assembla repos

## Setup 

### Get your Assembla keys
1. Register a new personal key in Assembla. Make sure you enable API and Repository access.
   blah blah blah 

3. Use this script to access the api
```
curl -H "X-Api-Key: <key>" -H "X-Api-Secret: <secret>" https://api.assembla.com/<path to resource>.json
```
3. We need to get a list of all the spaces you are a member of:
```
curl -H "X-Api-Key: <key>" -H "X-Api-Secret: <secret>" https://api.assembla.com/v1/spaces.json
```
4. Do more stuff and then voila
