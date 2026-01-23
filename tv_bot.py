from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "8360583315:AAEhW6-lrrkQc6UReF7rV23MYxnGNj2QSjk"
CHAT_ID = "5418700144"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    msg = data.get("message", "Signal Triggered")

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

    return "OK", 200

app.run(port=5000)
