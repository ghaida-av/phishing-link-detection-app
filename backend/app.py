from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/detect', methods=['POST'])
def detect():
    # Get data from request
    data = request.json
    # Placeholder for detection logic
    # e.g., process image data
    result = {"status": "success", "message": "Detection completed"}
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)





