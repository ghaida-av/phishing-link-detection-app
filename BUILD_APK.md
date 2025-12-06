# How to Build APK - Simple Guide

## Option 1: Using Android Studio (Easiest)

1. **Open Android Studio**
2. **Open Project**: File → Open → Select `android-client` folder
3. **Wait for Gradle Sync** (automatic)
4. **Build APK**: 
   - Click `Build` → `Build Bundle(s) / APK(s)` → `Build APK(s)`
   - Wait for build to complete
5. **Find APK**: 
   - Click "locate" in the notification, OR
   - Go to: `android-client/app/build/outputs/apk/debug/app-debug.apk`

## Option 2: Using Command Line

```bash
cd android-client

# Make gradlew executable (if exists)
chmod +x gradlew

# Build debug APK
./gradlew assembleDebug

# APK will be at:
# android-client/app/build/outputs/apk/debug/app-debug.apk
```

## Install APK on Your Phone

1. **Transfer APK** to your phone (via USB, email, or cloud storage)
2. **Enable Unknown Sources**:
   - Settings → Security → Enable "Install from Unknown Sources"
   - OR Settings → Apps → Special Access → Install Unknown Apps
3. **Open APK file** on your phone
4. **Tap Install**

## Important Notes

- **Backend Required**: The app needs the backend server running
- **For Emulator**: Use `http://10.0.2.2:5000/predict` (already set)
- **For Physical Device**: 
  1. Find your computer's IP: `ifconfig` (Mac) or `ipconfig` (Windows)
  2. Update `BACKEND_URL` in `MainActivity.kt` before building
  3. Make sure phone and computer are on same WiFi

## Quick Test

After installing:
1. Start backend: `cd backend && python app.py`
2. Open app on phone
3. Enter URL: `https://www.google.com`
4. Click "Check URL"

---

**The APK file will be ready to download once you build it!**

