# 🌐 Phishing Link Checker

A simple Android + Web application that checks if a URL is **Safe ✅** or a **Phishing link ❌**  
Built using **HTML (Web)** and **Python Flask (Backend)**, with an **Android version** for mobile users.

---

## 📱 Features
- Clean blue background with a white “Check URL” button.
- Simple, beginner-friendly UI.
- Connects to a global Flask backend.
- Shows results instantly:
  - ✅ Safe
  - ❌ Phishing link

---

## ⚙️ Prerequisites
Before running the app, make sure you have:
- **Android Studio** (latest version)
- **Android SDK** (API 24 or above)
- **Python 3.9+** installed for the Flask server
- A **global hosting service** for the backend (like Render, Railway, or Ngrok)

---

## 🧩 Installation (Android)
1. **Open Project in Android Studio**
   - Go to `android-client/` and open it.

2. **Sync Gradle**
   - Let Android Studio download dependencies.

3. **Configure Backend URL**
   - Open `MainActivity.kt`  
   - Replace:
     ```kotlin
     private val BACKEND_URL = "https://your-global-backend-host/predict"
     ```
     with your Flask server URL.

4. **Run the App**
   - Click ▶️ **Run** in Android Studio.
   - Enter a URL and press **Check URL**.

---

## 💻 Web App Version
For iPhone or browser access, the same design is available as a simple **HTML + Flask** web app.

- **Blue background**
- **White “Check URL” button**
- Shows: ✅ Safe / ❌ Phishing link

Run it using:
```bash
python app.py


