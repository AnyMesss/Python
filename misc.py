import requests

response = requests.get("https://dog.ceo/api/breeds/image/random")

if response.status_code == 200:
    print("Success! Here's a random dog picture:")
    print(response.json()['message'])
else:
    print("Oops! Something went wrong.")

