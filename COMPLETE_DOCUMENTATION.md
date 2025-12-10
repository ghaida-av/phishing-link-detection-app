# 📚 Complete Project Documentation

## Table of Contents
1. [Project Overview](#project-overview)
2. [Backend Implementation](#backend-implementation)
3. [Android App Implementation](#android-app-implementation)
4. [GitHub Actions Setup](#github-actions-setup)
5. [Commands Used](#commands-used)
6. [File Structure](#file-structure)
7. [Why Each Component Was Used](#why-each-component-was-used)

---

## Project Overview

 **Phishing Link Detection App**  uses **Machine Learning** to  determine if URL is phishing  or safe websites.

### Architecture
- **Backend**: Flask API with ML model 
- **Frontend**: Android app (Kotlin)
- **Build System**: GitHub Actions for automated APK building

---

## Backend Implementation

### 1. Machine Learning Model (`backend/detector.py`)

#### Purpose
Analyzes URLs and extracts features to predict if they are phishing .

#### Key Functions

**`extract_features_vector(url)`**
```python
def extract_features_vector(url):
    """Extract features as a vector for ML model"""
    parsed = urlparse(url)
    netloc = parsed.netloc.lower()
    path = parsed.path or ''
    query = parsed.query or ''
    full_url = url.lower()
    
    features = []
    features.append(len(url))  # URL length
    features.append(1 if re.match(ip_pattern, netloc_clean) else 0)  # Has IP
    features.append(netloc.count('.'))  # Number of dots
    features.append(1 if '@' in url else 0)  # Has @ symbol
    features.append(1 if parsed.scheme.lower() == 'https' else 0)  # HTTPS
    features.append(len(parts))  # Number of subdomains
    # ... more features
    
    return np.array(features)
```

**Why**: Extracts  features from URLs that ML models use to detect phishing patterns.

**`ml_predict(url)`**
```python
def ml_predict(url):
    """Use ML model to predict phishing probability"""
    if ml_model is None:
        return None
    
    features = extract_features_vector(url)
    features = features.reshape(1, -1)
    proba = ml_model.predict_proba(features)[0]
    phishing_prob = proba[1] if len(proba) > 1 else proba[0]
    prediction = ml_model.predict(features)[0]
    
    return float(phishing_prob), int(prediction)
```

**Why**: Uses  to predict phishing probability (0.0 to 1.0).

**`ml_score(url)`**
```python
def ml_score(url):
    """Return ML-based score and reasons"""
    ml_result = ml_predict(url)
    if ml_result is not None:
        score, prediction = ml_result
        reasons = get_reasons(url, score)
        return round(score, 3), reasons
    else:
        return heuristic_score(url)  # Fallback
```

**Why**: Provides a fallback to heuristic scoring if ML model isn't available.

---

### 2. Model Training (`backend/train_model.py`)

#### Purpose
Trains a Random Forest classifier on URL features.

#### Key Code

```python
def train_model():
    """Train the ML model"""
    urls, labels = generate_training_data()
    X = np.array([extract_features_vector(url) for url in urls])
    y = np.array(labels)
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=10,
        random_state=42,
        n_jobs=-1
    )
    
    model.fit(X_train, y_train)
    joblib.dump(model, 'phishing_model.pkl')
```

**Why Random Forest?**
- Handles non-linear relationships well
- Provides feature importance
- Less prone to overfitting than single decision trees
- Fast training and prediction

**Why 100 estimators?**
- Good balance between accuracy and speed
- More estimators = better accuracy but slower

**Why test_size=0.2?**
- 80% for training, 20% for validation
- Standard practice in ML

---

### 3. Flask API (`backend/app.py`)

#### Purpose
RESTful API endpoint that receives URLs and returns phishing analysis.

#### Key Code

```python
from flask import Flask, request, jsonify
from flask_cors import CORS
from detector import ml_score

app = Flask(__name__)
CORS(app)  # Enable CORS for Android app

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(silent=True)
    if not data or 'url' not in data:
        return jsonify({"error": "send JSON with field 'url'"}), 400

    url = data['url'].strip()
    if not url:
        return jsonify({"error": "URL cannot be empty"}), 400
    
    # Add http:// if no scheme is present
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
```

**Why Flask?**
- Lightweight and simple
- Easy to deploy
- Good for REST APIs

**Why CORS?**
- Android app makes requests from different origin
- CORS allows cross-origin requests

**Why POST method?**
- Sending data (URL) to server
- More secure than GET (URLs in query string)

**Why add http:// automatically?**
- User convenience
- Ensures URL is parseable

**Why threshold 0.5?**
- Balanced decision point
- Score >= 0.5 = phishing, < 0.5 = legitimate

---

## Android App Implementation

### 1. Main Activity (`android-client/app/src/main/java/com/example/phishing/MainActivity.kt`)

#### Purpose
Main UI and logic for the Android app.

#### Key Code

**Network Client Setup**
```kotlin
private val client = OkHttpClient()

private val BACKEND_URL = "http://10.0.2.2:5000/predict"
// For emulator: 10.0.2.2 maps to localhost
// For physical device: Use computer's IP address
```

**Why OkHttp?**
- Popular HTTP client for Android
- Handles async requests well
- Good error handling

**Why 10.0.2.2?**
- Android emulator special IP
- Maps to host machine's localhost
- Allows emulator to access local server

**URL Checking Function**
```kotlin
private fun checkUrl(url: String) {
    errorText.visibility = android.view.View.GONE
    resultText.text = ""
    progressBar.visibility = android.view.View.VISIBLE
    checkButton.isEnabled = false
    checkButton.text = "Checking..."

    val json = JSONObject()
    json.put("url", url)
    val body = RequestBody.create(
        MediaType.get("application/json; charset=utf-8"),
        json.toString()
    )

    val request = Request.Builder()
        .url(BACKEND_URL)
        .post(body)
        .build()

    client.newCall(request).enqueue(object : Callback {
        override fun onFailure(call: Call, e: IOException) {
            runOnUiThread {
                // Handle error
            }
        }

        override fun onResponse(call: Call, response: Response) {
            // Handle response
        }
    })
}
```

**Why enqueue()?**
- Async network call
- Doesn't block UI thread
- Android requires network on background thread

**Why runOnUiThread()?**
- Network callbacks run on background thread
- UI updates must be on main thread
- Prevents crashes

**Why JSONObject?**
- Standard way to create JSON in Android
- Easy to use
- Built into Android SDK

---

### 2. Layout (`android-client/app/src/main/res/layout/activity_main.xml`)

#### Purpose
Defines the UI structure.

#### Key Components

```xml
<EditText
    android:id="@+id/urlInput"
    android:hint="Enter URL here"
    android:inputType="textUri" />
```

**Why inputType="textUri"?**
- Shows appropriate keyboard
- Validates URL format
- Better UX

```xml
<Button
    android:id="@+id/checkButton"
    android:text="Check URL" />
```

**Why Button?**
- Standard Android component
- Handles clicks
- Accessible

```xml
<ProgressBar
    android:id="@+id/progressBar"
    android:visibility="gone" />
```

**Why visibility="gone"?**
- Hidden by default
- Shown only when loading
- Better UX

---

### 3. Android Manifest (`android-client/app/src/main/AndroidManifest.xml`)

#### Purpose
Declares app permissions and components.

#### Key Code

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

**Why INTERNET permission?**
- Required for network requests
- Android security model
- Must be declared

**Why ACCESS_NETWORK_STATE?**
- Check if network is available
- Better error handling
- Optional but recommended

```xml
<application
    android:usesCleartextTraffic="true">
```

**Why usesCleartextTraffic?**
- Allows HTTP (not just HTTPS)
- Needed for localhost testing
- Remove in production (use HTTPS)

---

## GitHub Actions Setup

### Workflow File (`.github/workflows/build-apk.yml`)

#### Purpose
Automatically builds APK when code is pushed to GitHub.

#### Complete Code with Explanations

```yaml
name: Build APK
```
**Why**: Name shown in GitHub Actions UI.

```yaml
on:
  workflow_dispatch:
  push:
    branches:
      - main
```
**Why**:
- `workflow_dispatch`: Manual trigger from GitHub UI
- `push`: Automatic build on code push
- `branches: main`: Only on main branch

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
```
**Why ubuntu-latest?**
- Free on GitHub Actions
- Has all tools needed
- Fast and reliable

```yaml
    steps:
    - name: Checkout code
      uses: actions/checkout@v4
```
**Why**: Downloads repository code to runner.

```yaml
    - name: Set up JDK
      uses: actions/setup-java@v4
      with:
        java-version: '17'
        distribution: 'temurin'
```
**Why Java 17?**
- Required by Android Gradle Plugin 8.1.0
- LTS version (Long Term Support)
- Stable

**Why temurin?**
- OpenJDK distribution
- Free and reliable
- Good performance

```yaml
    - name: Setup Android SDK
      uses: android-actions/setup-android@v3
```
**Why**: Installs Android SDK and build tools needed for compilation.

```yaml
    - name: Grant execute permission for gradlew
      run: chmod +x android-client/gradlew
      working-directory: ${{ github.workspace }}
```
**Why chmod +x?**
- Makes gradlew executable
- Required to run build script
- Linux/Unix requirement

```yaml
    - name: Build APK
      run: ./gradlew assembleDebug
      working-directory: android-client
```
**Why assembleDebug?**
- Builds debug APK (faster, no signing)
- For testing
- Release uses `assembleRelease`

**Why working-directory?**
- Changes to android-client folder
- Gradle needs to run from project root

```yaml
    - name: Upload APK
      uses: actions/upload-artifact@v4
      with:
        name: app-debug
        path: android-client/app/build/outputs/apk/debug/app-debug.apk
```
**Why upload-artifact?**
- Saves APK file
- Available for download after build
- Stored for 90 days

**Why v4?**
- Latest version
- v3 was deprecated
- Better performance

---

## Commands Used

### Git Commands

```bash
git init
```
**Purpose**: Initialize git repository  
**Why**: Track code changes, version control

```bash
git add .
```
**Purpose**: Stage all files for commit  
**Why**: Prepare changes to be saved

```bash
git commit -m "message"
```
**Purpose**: Save changes with message  
**Why**: Create snapshot of code at this point

```bash
git remote add origin https://github.com/username/repo.git
```
**Purpose**: Connect local repo to GitHub  
**Why**: Enable pushing code to cloud

```bash
git push origin main
```
**Purpose**: Upload code to GitHub  
**Why**: Make code available online, trigger Actions

```bash
git status
```
**Purpose**: Check what files changed  
**Why**: See current state of repository

---

### Python Commands

```bash
python3 -m venv venv
```
**Purpose**: Create virtual environment  
**Why**: Isolate project dependencies

```bash
source venv/bin/activate
```
**Purpose**: Activate virtual environment  
**Why**: Use project-specific Python packages

```bash
pip install -r requirements.txt
```
**Purpose**: Install dependencies  
**Why**: Get all required libraries

```bash
python train_model.py
```
**Purpose**: Train ML model  
**Why**: Create `phishing_model.pkl` file

```bash
python app.py
```
**Purpose**: Start Flask server  
**Why**: Run API on port 5000

---

### Gradle Commands

```bash
./gradlew assembleDebug
```
**Purpose**: Build debug APK  
**Why**: Create installable Android app

```bash
chmod +x gradlew
```
**Purpose**: Make gradlew executable  
**Why**: Required to run build script

---

### File System Commands

```bash
cd /path/to/directory
```
**Purpose**: Change directory  
**Why**: Navigate to project folder

```bash
mkdir -p path/to/dir
```
**Purpose**: Create directory  
**Why**: Make folder structure

```bash
ls -la
```
**Purpose**: List files  
**Why**: See directory contents

---

## File Structure

```
Phishing-Link-Detection-App/
├── backend/
│   ├── app.py                 # Flask API server
│   ├── detector.py            # ML model and detection logic
│   ├── train_model.py         # Model training script
│   ├── requirements.txt       # Python dependencies
│   ├── phishing_model.pkl     # Trained ML model (generated)
│   └── venv/                  # Python virtual environment
│
├── android-client/
│   ├── app/
│   │   ├── build.gradle       # App dependencies
│   │   └── src/main/
│   │       ├── AndroidManifest.xml    # App permissions
│   │       ├── java/com/example/phishing/
│   │       │   └── MainActivity.kt    # Main app code
│   │       └── res/
│   │           ├── layout/
│   │           │   └── activity_main.xml  # UI layout
│   │           └── values/
│   │               └── strings.xml        # App strings
│   ├── build.gradle           # Project build config
│   ├── settings.gradle        # Repository config
│   └── gradlew                # Gradle wrapper script
│
└── .github/
    └── workflows/
        └── build-apk.yml       # GitHub Actions workflow
```

---

## Why Each Component Was Used

### Backend Technologies

**Flask**
- Simple and lightweight
- Easy to learn
- Good for REST APIs
- Fast development

**scikit-learn**
- Industry standard ML library
- Random Forest implementation
- Easy to use
- Well documented

**Random Forest**
- Good accuracy
- Handles mixed data types
- Less overfitting
- Fast prediction

**joblib**
- Efficient model serialization
- Faster than pickle for large models
- Standard in scikit-learn

**numpy**
- Fast numerical operations
- Required by scikit-learn
- Efficient arrays

**flask-cors**
- Enable cross-origin requests
- Required for Android app
- Simple to use

---

### Android Technologies

**Kotlin**
- Modern Android language
- Safer than Java
- Concise syntax
- Official Android language

**OkHttp**
- Popular HTTP library
- Handles async well
- Good error handling
- Maintained by Square

**Material Components**
- Modern UI design
- Consistent look
- Better UX
- Google's design system

**AndroidX**
- Latest Android libraries
- Backward compatible
- Active development

---

### Build & Deployment

**Gradle**
- Standard Android build tool
- Handles dependencies
- Fast builds
- Flexible

**GitHub Actions**
- Free for public repos
- Automatic builds
- No local setup needed
- Cloud-based

**Git**
- Version control
- Track changes
- Collaboration
- Industry standard

---

## Key Design Decisions

### 1. Why ML Instead of Just Rules?

**ML Approach:**
- Learns patterns from data
- Adapts to new threats
- More accurate
- Can improve with more data

**Rule-Based (Heuristic):**
- Simple and fast
- Easy to understand
- Good fallback
- Used when ML unavailable

**Decision**: Use ML with heuristic fallback for reliability.

---

### 2. Why Random Forest?

**Alternatives Considered:**
- **Logistic Regression**: Too simple, linear
- **Neural Networks**: Overkill, slow
- **SVM**: Slower, harder to tune
- **Decision Tree**: Overfits easily

**Random Forest Chosen:**
- Good accuracy
- Fast training
- Handles features well
- Less overfitting

---

### 3. Why Flask Instead of Django?

**Flask:**
- Lightweight
- Simple API
- Fast setup
- Less overhead

**Django:**
- Too heavy for simple API
- More features than needed
- Slower startup

**Decision**: Flask for simplicity and speed.

---

### 4. Why GitHub Actions?

**Alternatives:**
- **Local Build**: Requires Android Studio
- **CI/CD Services**: Cost money
- **Manual Build**: Time consuming

**GitHub Actions:**
- Free for public repos
- Integrated with GitHub
- Automatic
- No setup needed

---

## Security Considerations

### Backend

1. **Input Validation**
   - Check URL format
   - Sanitize input
   - Prevent injection attacks

2. **CORS**
   - Only allow specific origins in production
   - Current: allows all (for development)

3. **HTTPS**
   - Use HTTPS in production
   - Current: HTTP for local testing

### Android

1. **Network Security**
   - Uses cleartext traffic (development only)
   - Should use HTTPS in production

2. **Permissions**
   - Only requests necessary permissions
   - INTERNET only

3. **Data Handling**
   - No sensitive data stored
   - URLs sent to server only

---

## Performance Optimizations

### Backend

1. **Model Loading**
   - Load once at startup
   - Cache in memory
   - Fast predictions

2. **Feature Extraction**
   - Efficient algorithms
   - Minimal computation
   - Fast response

### Android

1. **Async Network**
   - Non-blocking UI
   - Background threads
   - Smooth UX

2. **Simple UI**
   - Minimal components
   - Fast rendering
   - Low memory

---

## Future Improvements

1. **Larger Training Dataset**
   - More phishing examples
   - Better accuracy
   - Real-world data

2. **HTTPS in Production**
   - Secure communication
   - Encrypted data

3. **Rate Limiting**
   - Prevent abuse
   - Fair usage

4. **Caching**
   - Cache results
   - Faster responses

5. **Better UI**
   - More features
   - Better design
   - Animations

---

## Troubleshooting Guide

### Backend Issues

**Model not found:**
```bash
cd backend
python train_model.py
```

**Port already in use:**
```bash
# Change port in app.py
app.run(host='0.0.0.0', port=5001)
```

**Dependencies missing:**
```bash
pip install -r requirements.txt
```

### Android Issues

**Network error:**
- Check backend is running
- Verify URL is correct
- Check firewall

**Build fails:**
- Sync Gradle
- Clean project
- Invalidate caches

### GitHub Actions Issues

**Workflow fails:**
- Check logs
- Verify file paths
- Check permissions

**APK not found:**
- Check build succeeded
- Look in Artifacts section
- Wait for build to complete

---

## Conclusion

This project demonstrates:
- ML model training and deployment
- RESTful API development
- Android app development
- CI/CD with GitHub Actions
- End-to-end application development

All code is documented, tested, and ready for use!

---

**Last Updated**: December 2024  
**Version**: 1.0  
**Author**: AI Assistant

