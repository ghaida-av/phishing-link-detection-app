# Quick Start Guide

Get your Phishing Detection App up and running in minutes!

## ⚡ 5-Minute Setup

### Step 1: Backend Setup (2 minutes)

```bash
cd backend
./setup.sh
```

Or manually:
```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python train_model.py
python app.py
```

✅ Backend is now running on `http://localhost:5000`

### Step 2: Android Setup (3 minutes)

1. **Open Android Studio**
   - File → Open → Select `android-client` folder

2. **Wait for Gradle Sync**
   - Android Studio will automatically download dependencies
   - Wait for "Gradle sync finished" message

3. **Start Emulator or Connect Device**
   - Tools → Device Manager → Create/Start emulator
   - OR connect your Android device via USB

4. **Run the App**
   - Click the green ▶️ Run button
   - Or press `Shift + F10`

✅ App is now running!

## 🧪 Test It Out

1. Open the app on your device/emulator
2. Enter a test URL:
   - **Legitimate**: `https://www.google.com`
   - **Suspicious**: `http://192.168.1.1/login.php`
3. Click "Check URL"
4. View the results!

## 🔧 Troubleshooting

### Backend won't start?
- Check if port 5000 is available
- Make sure Python 3.7+ is installed
- Verify all dependencies installed: `pip list`

### Android app shows network error?
- **Emulator**: Make sure backend URL is `http://10.0.2.2:5000`
- **Physical Device**: 
  1. Find your computer's IP: `ifconfig` (Mac/Linux) or `ipconfig` (Windows)
  2. Update `BACKEND_URL` in `MainActivity.kt`
  3. Make sure phone and computer are on same WiFi network
  4. Check firewall isn't blocking port 5000

### Model not found error?
- Run `python train_model.py` in the backend directory
- Make sure `phishing_model.pkl` exists in backend folder

## 📱 For Physical Android Device

1. Find your computer's IP address:
   ```bash
   # Mac/Linux
   ifconfig | grep "inet "
   
   # Windows
   ipconfig
   ```

2. Update `MainActivity.kt`:
   ```kotlin
   private val BACKEND_URL = "http://YOUR_IP:5000/predict"
   ```

3. Make sure both devices are on the same WiFi network

4. Restart the app

## 🎉 You're All Set!

Your Phishing Detection App is ready to use. Try checking different URLs and see how the ML model analyzes them!

