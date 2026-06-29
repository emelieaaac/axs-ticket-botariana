import requests

BOT_TOKEN = "8854359870:AAFUM6dKVVPZZqLSHOxOLHwgufWwtjgGkX0"
CHAT_ID = "8933540965"

URL = "https://www.axs.com/events/1141607/ariana-grande-extra-date-added-tickets"

def send(msg):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": msg
        }
    )

headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get(URL, headers=headers)
text = r.text.lower()

signals = [
    "choose from the map",
    "pick your tickets",
    "buy tickets",
    "select seats",
    "available"
]

if any(s in text for s in signals):
    send("🚨 TICKETS MOGELIJK!\n" + URL)
    print("alert sent")
else:
    print("no tickets")
