from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow Android + Web + iPhone access

# Simple phishing check (NO ML)
def check_url(url):
    phishing_words = ["login", "verify", "bank", "secure", "update", "account"]
    for word in phishing_words:
        if word in url.lower():
            return "Phishing link ❌"
    return "Safe ✅"

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Phishing Link Checker API"})

@app.route("/check", methods=["POST"])
def check():
    data = request.get_json()

    if not data or "url" not in data:
        return jsonify({"result": "Phishing link ❌"})

    url = data["url"].strip()

    if not url:
        return jsonify({"result": "Phishing link ❌"})

    if not url.startswith(("http://", "https://")):
        url = "http://" + url

    result = check_url(url)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)





