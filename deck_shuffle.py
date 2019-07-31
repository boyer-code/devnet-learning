import requests

url = "https://deckofcardsapi.com/api/deck/new/shuffle/"

querystring = {"deck_count":"6"}

headers = {
    'cache-control': "no-cache",
    'Postman-Token': "f72a5ebf-4fb9-4ef9-aab1-ce675dd4e864"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

deck = response.json()
deck_id = deck['deck_id']
print(deck_id, "is the deck id")

for k, v in fruit_inventory.items():
    print("You have {} {}.".format(v, k))