from flask import Flask, request
import requests
import os

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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
