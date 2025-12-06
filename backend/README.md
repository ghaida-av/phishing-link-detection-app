# Phishing Link Detection Backend

Machine Learning-based backend API for detecting phishing URLs using Random Forest classifier.

## Features

- **ML-Based Detection**: Uses scikit-learn Random Forest classifier
- **Feature Extraction**: Analyzes 14+ URL features including:
  - URL length
  - IP address detection
  - Subdomain analysis
  - Suspicious keywords
  - HTTPS usage
  - And more...
- **RESTful API**: Simple JSON-based API
- **Fallback System**: Falls back to heuristic scoring if ML model is unavailable

## Setup

### 1. Install Dependencies

```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Train the ML Model

```bash
python train_model.py
```

This will:
- Generate training data
- Train a Random Forest classifier
- Save the model as `phishing_model.pkl`
- Display model accuracy and classification report

### 3. Run the Server

```bash
python app.py
```

The server will start on `http://0.0.0.0:5000`

## API Endpoints

### GET `/`
Health check endpoint

**Response:**
```json
{
  "message": "Phishing Link Detection API",
  "version": "2.0",
  "model": "ML-based Random Forest"
}
```

### POST `/predict`
Predict if a URL is phishing

**Request:**
```json
{
  "url": "https://example.com"
}
```

**Response:**
```json
{
  "url": "https://example.com",
  "score": 0.15,
  "verdict": "legitimate",
  "reasons": [
    "URL appears legitimate"
  ],
  "confidence": "high"
}
```

**Response Fields:**
- `url`: The analyzed URL
- `score`: Phishing probability (0.0 to 1.0, higher = more suspicious)
- `verdict`: "phishing" or "legitimate"
- `reasons`: Array of analysis reasons
- `confidence`: "high", "medium", or "low"

## Model Training

The model is trained on synthetic data. For production use, consider:

1. Using a larger, real-world dataset
2. Collecting labeled phishing URLs from sources like:
   - PhishTank
   - OpenPhish
   - Your own security logs
3. Fine-tuning hyperparameters
4. Using ensemble methods

## Testing

Test the API with curl:

```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.google.com"}'
```

## Notes

- The model file (`phishing_model.pkl`) should be in the backend directory
- If the model file is missing, the API falls back to heuristic-based detection
- For Android emulator: Use `http://10.0.2.2:5000`
- For physical device: Use your computer's IP address (e.g., `http://192.168.1.100:5000`)
