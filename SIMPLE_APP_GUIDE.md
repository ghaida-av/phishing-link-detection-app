#  Phishing Detection App 

## ✅ What I Did

I've simplified your app to make it super easy to use:

### Simplified Features:
- ✨ Clean, simple UI (no complex cards)
- 📝 One input field for URL
- 🔘 One button to check
- 📊 Simple result display
- ⚡ Fast and lightweight

## 🚀 Get Your APK (Download Link)

### **⭐ RECOMMENDED: Android Studio (Easiest & Most Reliable)**

Android Studio handles all Java/Gradle version issues automatically!

1. **Open Android Studio**
2. **File** → **Open** → Select **`android-client`** folder
3. **Wait** for Gradle sync to finish (bottom right)
4. Press **`Cmd + F9`** (Mac) or **`Ctrl + F9`** (Windows)
   - OR click **Build** → **Make Project**
5. **Wait** 1-2 minutes for build
6. **Find APK**: Right-click **`app`** folder → **Show in Finder**
   - Navigate to: **`build/outputs/apk/debug/app-debug.apk`**

**📖 See `BUILD_WITH_ANDROID_STUDIO.md` for detailed step-by-step guide**

### **OR Method 2: Try Build Script (May have Java version issues)**

1. Open Android Studio
2. Open the `android-client` folder
3. Wait for Gradle sync to finish
4. Press **`Cmd + F9`** (Mac) or **`Ctrl + F9`** (Windows)
   - OR click **Build** → **Make Project**
5. Wait 1-2 minutes for build
6. Find APK at: `app/build/outputs/apk/debug/app-debug.apk`
   - Right-click `app` folder → **Show in Finder** → `build/outputs/apk/debug/`

### **OR Method 3: Android Studio Terminal**

1. Open Android Studio
2. Open `android-client` project
3. Click **Terminal** tab at bottom
4. Type: `./gradlew assembleDebug`
5. Press Enter
6. APK will be at: `app/build/outputs/apk/debug/app-debug.apk`

### **Step 2: Transfer to Your Phone**

**Option A - USB:**
- Connect phone via USB
- Copy `app-debug.apk` to your phone
- Open file manager on phone → Tap APK → Install

**Option B - Email/Cloud:**
- Email the APK to yourself
- Open email on phone → Download → Install

**Option C - Direct Download:**
- Upload APK to Google Drive/Dropbox
- Share link → Download on phone → Install

### **Step 3: Enable Installation**

On your Android phone:
- Go to **Settings** → **Security**
- Enable **"Install from Unknown Sources"** or **"Install Unknown Apps"**
- Select the app you'll use to install (Files, Chrome, etc.)

### **Step 4: Install**

- Open the APK file on your phone
- Tap **Install**
- Done! 🎉

## 📱 Using the App

1. **Start Backend First:**
   ```bash
   cd backend
   python app.py
   ```

2. **Open App on Phone**

3. **Enter a URL** (e.g., `https://www.google.com`)

4. **Tap "Check URL"**

5. **See Results:**
   - Verdict: Phishing or Legitimate
   - Risk Score: 0-100%
   - Reasons: Why it's safe or suspicious

## 🔧 For Physical Device (Not Emulator)

Before building APK, update the backend URL:

1. Open `android-client/app/src/main/java/com/example/phishing/MainActivity.kt`
2. Find this line:
   ```kotlin
   private val BACKEND_URL = "http://10.0.2.2:5000/predict"
   ```
3. Change to your computer's IP:
   ```kotlin
   private val BACKEND_URL = "http://192.168.1.XXX:5000/predict"
   ```
4. Find your IP:
   - Mac/Linux: Run `ifconfig` in terminal
   - Windows: Run `ipconfig` in CMD
5. Rebuild APK

## 📋 App Features

- ✅ Simple, clean interface
- ✅ Real-time URL checking
- ✅ ML-powered detection
- ✅ Risk scoring
- ✅ Detailed analysis
- ✅ Works offline (needs backend running)

## 🎯 That's It!

Your simplified app is ready. Just build the APK in Android Studio and install it on your phone!

---

**Need Help?** Check `BUILD_APK.md` for detailed build instructions.

