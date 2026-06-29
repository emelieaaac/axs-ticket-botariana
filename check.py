import requests

url = "https://www.axs.com/events/1141607/ariana-grande-extra-date-added-tickets"

headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get(url, headers=headers)
text = r.text.lower()

signals = [
    "choose from the map",
    "pick your tickets",
    "buy tickets",
    "select seats",
    "available",
    "tickets"
]

if any(s in text for s in signals):
    print("🚨 TICKETS MOGELIJK")
else:
    print("no tickets")
