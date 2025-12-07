from flask import Flask, request, jsonify
from flask_cors import CORS
from detector import ml_score

app = Flask(__name__)
CORS(app) 

@app.route('/')
def index():
    return jsonify({
        "message": "Phishing Link Detection API", 
        "version": "2.0",
        "model": "ML-based Random Forest"
    })

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(silent=True)
        if not data or 'url' not in data:
            return jsonify({"error": "send JSON with field 'url'"}), 400

        url = data['url'].strip()
        if not url:
            return jsonify({"error": "URL cannot be empty"}), 400
        
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
        
        score, reasons = ml_score(url)
        verdict = "phishing" if score >= 0.5 else "legitimate"
        
        return jsonify({
            "url": url,
            "score": score,
            "verdict": verdict,
            "reasons": reasons,
            "confidence": "high" if abs(score - 0.5) > 0.3 else "medium"
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)




