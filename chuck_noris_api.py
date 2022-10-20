import requests

def get_new_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)

    joke_data = response.json()

    return {
        "id": joke_data["id"],
        "joke": joke_data["value"]
    } 

