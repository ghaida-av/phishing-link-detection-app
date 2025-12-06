# 🚀 Build APK - SUPER EASY METHOD

## ✅ Method 1: Using Terminal (Recommended - Works Everywhere!)

### Step 1: Open Terminal
- **Mac**: Press `Cmd + Space`, type "Terminal", press Enter
- **Windows**: Press `Win + R`, type "cmd", press Enter

### Step 2: Copy and Paste These Commands

```bash
cd /Users/ghaidaa/Phishing-Link-Detection-App/android-client
./gradlew assembleDebug
```

### Step 3: Wait for Build
- Takes 2-5 minutes first time (downloads dependencies)
- Shows "BUILD SUCCESSFUL" when done

### Step 4: Find Your APK
After build completes, your APK is here:
```
/Users/ghaidaa/Phishing-Link-Detection-App/android-client/app/build/outputs/apk/debug/app-debug.apk
```

**To open the folder:**
- **Mac**: `open app/build/outputs/apk/debug/`
- **Windows**: Navigate to that folder in File Explorer

---

## ✅ Method 2: Using Android Studio Terminal

1. Open Android Studio
2. Open the `android-client` project
3. Click **View** → **Tool Windows** → **Terminal** (or click Terminal icon at bottom)
4. Type:
```bash
./gradlew assembleDebug
```
5. Press Enter
6. Wait for "BUILD SUCCESSFUL"
7. Right-click `app` folder → **Show in Finder/Explorer**
8. Go to: `build/outputs/apk/debug/`
9. Copy `app-debug.apk`!

---

## ✅ Method 3: Android Studio Menu (Different Options)

Try these menu options (varies by version):

### Option A:
- **Build** → **Make Project** (or press `Ctrl+F9` / `Cmd+F9`)
- Then look for APK in `app/build/outputs/apk/debug/`

### Option B:
- Right-click on **app** folder in Project view
- Select **Build** → **Build APK**

### Option C:
- **Build** → **Generate Signed Bundle / APK**
- Choose **APK** → **Next**
- Choose **debug** → **Next**
- Click **Finish**

---

## 📱 After Building - Install on Phone

1. **Transfer APK to phone** (USB, email, or cloud)
2. **Enable Unknown Sources**:
   - Settings → Security → Install Unknown Apps
3. **Open APK file** on phone
4. **Tap Install**

---

## ⚠️ Troubleshooting

### "gradlew: command not found"
- Make sure you're in the `android-client` folder
- Try: `chmod +x gradlew` first

### "JAVA_HOME not set"
- Android Studio should handle this
- Or set JAVA_HOME to your JDK path

### Build Fails
- Make sure Android Studio has synced Gradle
- Try: **File** → **Sync Project with Gradle Files**
- Wait for sync to complete, then try again

---

## 🎯 Quick Command Summary

```bash
# Navigate to project
cd /Users/ghaidaa/Phishing-Link-Detection-App/android-client

# Build APK
./gradlew assembleDebug

# Open APK folder (Mac)
open app/build/outputs/apk/debug/

# Open APK folder (Windows - in File Explorer)
# Navigate to: android-client/app/build/outputs/apk/debug/
```

**That's it! Your APK will be ready in 2-5 minutes!** 🎉

