import requests

url = "https://www.axs.com/events/1141607/ariana-grande-extra-date-added-tickets"

r = requests.get(url)
text = r.text.lower()

if "choose from the map" in text or "find tickets" in text:
    print("TICKETS MOGELIJK")
else:
    print("no tickets")
