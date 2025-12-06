# Phishing Link Detection App

A complete Machine Learning-based solution for detecting phishing URLs, consisting of a Flask backend API and an Android mobile application.

## 🎯 Features

- **ML-Powered Detection**: Uses Random Forest classifier trained on URL features
- **Real-time Analysis**: Instant URL checking via REST API
- **Modern Android UI**: Material Design interface with intuitive UX
- **Detailed Reports**: Risk scores, confidence levels, and analysis reasons
- **Robust Error Handling**: Comprehensive error messages and loading states

## 📁 Project Structure

```
Phishing-Link-Detection-App/
├── backend/                 # Flask API server
│   ├── app.py              # Flask application
│   ├── detector.py         # ML model and detection logic
│   ├── train_model.py      # Model training script
│   ├── requirements.txt    # Python dependencies
│   └── README.md           # Backend documentation
│
├── android-client/          # Android application
│   ├── app/
│   │   └── src/main/
│   │       ├── java/com/example/phishing/
│   │       │   └── MainActivity.kt
│   │       ├── res/
│   │       │   ├── layout/activity_main.xml
│   │       │   └── values/strings.xml
│   │       └── AndroidManifest.xml
│   └── README.md           # Android documentation
│
└── README.md               # This file
```

## 🚀 Quick Start

### Backend Setup

1. **Navigate to backend directory**
   ```bash
   cd backend
   ```

2. **Create virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Train the ML model**
   ```bash
   python train_model.py
   ```

5. **Start the server**
   ```bash
   python app.py
   ```

The API will be available at `http://localhost:5000`

### Android Setup

1. **Open Android Studio**
   - Open the `android-client` folder as a project

2. **Sync Gradle**
   - Android Studio will automatically sync dependencies

3. **Configure Backend URL** (if needed)
   - For emulator: Already configured (`http://10.0.2.2:5000`)
   - For physical device: Update `BACKEND_URL` in `MainActivity.kt` with your computer's IP

4. **Run the App**
   - Connect device or start emulator
   - Click Run (▶️)

## 🔧 How It Works

### Machine Learning Model

The system uses a **Random Forest Classifier** that analyzes 14+ URL features:

1. URL length
2. IP address detection
3. Number of dots in domain
4. Presence of @ symbol
5. HTTPS usage
6. Number of subdomains
7. Suspicious keywords count
8. Path and query lengths
9. Special characters count
10. And more...

### Detection Flow

```
User Input URL
    ↓
Android App → HTTP POST → Flask Backend
    ↓
Feature Extraction → ML Model Prediction
    ↓
Risk Score + Reasons → JSON Response
    ↓
Android App → Display Results
```

## 📊 API Usage

### Predict Endpoint

```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com"}'
```

**Response:**
```json
{
  "url": "https://example.com",
  "score": 0.15,
  "verdict": "legitimate",
  "reasons": ["URL appears legitimate"],
  "confidence": "high"
}
```

## 🛠️ Technologies Used

### Backend
- **Flask**: Web framework
- **scikit-learn**: Machine Learning library
- **Random Forest**: ML algorithm
- **numpy**: Numerical computing
- **joblib**: Model serialization

### Android
- **Kotlin**: Programming language
- **OkHttp**: HTTP client
- **Material Components**: UI library
- **AndroidX**: Support libraries

## 📱 Screenshots

The Android app features:
- Clean, modern Material Design interface
- Real-time URL analysis
- Color-coded risk indicators
- Detailed analysis breakdown
- Loading states and error handling

## 🔒 Security Notes

- This is a demonstration project
- For production use, consider:
  - Using HTTPS for API communication
  - Implementing authentication
  - Using a larger, real-world training dataset
  - Adding rate limiting
  - Implementing caching

## 📝 License

See LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Support

For issues or questions, please open an issue on GitHub.

---

**Built with ❤️ using Machine Learning**
