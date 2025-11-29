from flask import Flask, request, jsonify
from detector import heuristic_score

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"message": "Phishing Link Detection API", "version":"1.0"})

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(silent=True)
    if not data or 'url' not in data:
        return jsonify({"error":"send JSON with field 'url'"}), 400

    url = data['url']
    score, reasons = heuristic_score(url)
    verdict = "phishing" if score >= 0.5 else "legitimate"  # threshold 0.5, tweakable
    return jsonify({
        "url": url,
        "score": score,
        "verdict": verdict,
        "reasons": reasons
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

