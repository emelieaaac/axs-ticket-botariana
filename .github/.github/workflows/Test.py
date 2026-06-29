import requests

BOT_TOKEN = "8854359870:AAFUM6dKVVPZZqLSHOxOLHwgufWwtjgGkX0"
CHAT_ID = "8933540965"

def send(msg):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": msg
        }
    )

send("✅ TEST: Telegram werkt")
