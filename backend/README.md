# Phishing Link Detection Backend

Machine Learning-based backend API for detecting phishing URLs .

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


cd backend
python3 -m venv venv
source venv/bin/activate  
pip install -r requirements.txt


### 2. Train the ML Model


python train_model.py



### 3. Run the Server


python app.py


The server will start on `http://0.0.0.0:5000`

## API Endpoints

### GET `/`
Health check endpoint

**output:**
json
{
  "message": "Phishing Link Detection API",
  "version": "2.0",
  "model": "ML-based Random Forest"
}


### POST `/predict`
Predict if a URL is phishing

**input:**
json
{
  "url": "https://example.com"
}
```

**output:**
json
{
  "url": "https://example.com",
  "score": 0.15,
  "verdict": "legitimate",
  "reasons": [
    "URL appears legitimate"
  ],
  "confidence": "high"
}


**Response Fields:**
- `url`: The analyzed URL
- `score`: Phishing probability (0.0 to 1.0, higher = more suspicious)
- `verdict`: "phishing" or "safe"
- `reasons`: Array of analysis reasons
- `confidence`: "high", "medium", or "low"

