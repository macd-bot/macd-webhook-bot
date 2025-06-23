from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json

    if not data or 'signal' not in data:
        return jsonify({"status": "error", "message": "Invalid payload"}), 400

    print("📩 New Webhook Signal Received:")
    print("Signal:", data.get('signal'))
    print("Symbol:", data.get('symbol'))
    print("Price:", data.get('price'))
    print("Time:", data.get('time'))

    return jsonify({"status": "ok", "message": "Signal received"}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
