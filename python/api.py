import requests     # Allows to send HTTP requests using Python
import json
from pprint import pprint



#############
### API's ###
#############



# GITHUB API #

# Making an API call and storing response:
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"

headers = {"Accept":"application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")      # 200: success, request processed. 404: not found. 500: server error.

# Storing API response in a dict as JSON:
response_dict = r.json()

# Processing results:
print(response_dict.keys())
print(f"\nTotal repositories: {response_dict['total_count']}")

# Exploring info about repos:
repo_dicts = response_dict['items']
print(f"Repositories returned {len(repo_dicts)}")

# Examining the first dictionary (key)
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)

# Print out selected info about each repository
print("\nSelected info about each repo")
for repo_dict in repo_dicts:
    print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Language: {repo_dict['language']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Description: {repo_dict['description']}")
print("\n\n\n")


# CURRENCY API #

# Requesting:
url = "https://api.coincap.io/v2/rates"
r = requests.get(url)
print(f"Status code = {r.status_code}")
print()

currency_rates = r.json()
print(currency_rates)

print(currency_rates.keys())
print()

pprint(currency_rates)
print()

# Making a timestamp:
print("Retrieved currencies from Coincap at: ",
      currency_rates['timestamp'])
print("Number of currencies: ", len(currency_rates['data']))
print()

# Looping over each currency, printing the symbol, name, and conversion against the USD:
for c in currency_rates['data']:
    print(f'{c["symbol"]} {c["id"]} {c["rateUsd"]}')