from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# 🔑 Apna Telegram bot token aur chat ID yahan daalo
BOT_TOKEN = "7248495973:AAE3e0fhebpiSFpBN1IGJeddSlEOmfZKaww"
CHAT_ID = "548712345"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if not data or 'signal' not in data:
        return jsonify({"status": "error", "message": "Invalid payload"}), 400

    text = f"🚨 {data['signal'].upper()} signal detected!\n\n" \
           f"Symbol: {data.get('symbol', 'N/A')}\n" \
           f"Price: {data.get('price', 'N/A')}\n" \
           f"Time: {data.get('time', 'N/A')}"

    try:
        requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", params={
            "chat_id": CHAT_ID,
            "text": text
        }).raise_for_status()
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

    return jsonify({"status": "ok", "message": "Alert sent", "received": data})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
