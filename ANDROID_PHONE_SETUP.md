# 📱 Android Phone Setup Guide

Complete guide to run the app on a physical Android phone.

---

## ⚠️ Current Issue

The app shows: **"Network error. Make sure backend is running on port 5000"**

This happens because the app is trying to connect to `10.0.2.2` (emulator address) but you're using a **physical Android phone**.

---

## 🔧 Fix: Update Backend URL for Physical Device

### Step 1: Find Your Computer's IP Address

**On Mac:**
```bash
ifconfig | grep "inet " | grep -v 127.0.0.1
```
Look for something like: `inet 192.168.1.100`

**On Windows:**
```bash
ipconfig
```
Look for "IPv4 Address" under your WiFi adapter

**Copy this IP address!** (e.g., `192.168.1.100`)

---

### Step 2: Update MainActivity.kt

1. Open: `android-client/app/src/main/java/com/example/phishing/MainActivity.kt`

2. Find this line (around line 16):
   ```kotlin
   private val BACKEND_URL = "http://10.0.2.2:5000/predict"
   ```

3. **Change it to your computer's IP:**
   ```kotlin
   private val BACKEND_URL = "http://192.168.1.100:5000/predict"
   ```
   (Replace `192.168.1.100` with YOUR actual IP address)

4. **Save the file**

---

### Step 3: Rebuild the APK

**Option A: Using Android Studio**
1. Open Android Studio
2. Open `android-client` project
3. Press `Cmd + F9` (Mac) or `Ctrl + F9` (Windows)
4. Wait for build to complete
5. APK is at: `app/build/outputs/apk/debug/app-debug.apk`

**Option B: Using GitHub Actions**
1. Commit and push the change:
   ```bash
   git add android-client/app/src/main/java/com/example/phishing/MainActivity.kt
   git commit -m "Update backend URL for physical Android device"
   git push origin main
   ```
2. Go to GitHub → Actions → Build APK
3. Download new APK

**Option C: Using Terminal**
```bash
cd android-client
./gradlew assembleDebug
```
APK at: `app/build/outputs/apk/debug/app-debug.apk`

---

### Step 4: Install Updated APK on Phone

1. **Uninstall** the old app from your phone (if installed)
2. **Transfer** the new APK to your phone
3. **Install** the new APK
4. **Open** the app

---

### Step 5: Start Backend Server

1. On your computer, open Terminal
2. Navigate to backend:
   ```bash
   cd /Users/ghaidaa/Phishing-Link-Detection-App/backend
   ```
3. Start server:
   ```bash
   python app.py
   ```
4. You should see: `Running on http://0.0.0.0:5000`
5. **Keep this running** while using the app

---

### Step 6: Connect Phone to Same WiFi

1. On Android phone: **Settings** → **Wi-Fi**
2. Make sure phone is connected to the **same WiFi network** as your computer
3. Check WiFi name matches

---

### Step 7: Test the App

1. Open the app on your phone
2. Enter a URL: `https://www.google.com`
3. Tap **"CHECK URL"**
4. It should work now! ✅

---

## 🆘 Troubleshooting

### Still Getting "Network error"?

**Check these:**

1. ✅ **Backend is running**
   - Terminal shows: `Running on http://0.0.0.0:5000`
   - No errors in terminal

2. ✅ **IP address is correct**
   - Double-check the IP in `MainActivity.kt`
   - Format: `http://192.168.1.100:5000/predict`
   - No `localhost` or `10.0.2.2`

3. ✅ **Phone and computer on same WiFi**
   - Check WiFi names match
   - Both connected to same network

4. ✅ **Firewall not blocking**
   - Mac: System Settings → Network → Firewall (allow Python)
   - Windows: Allow Python through firewall

5. ✅ **APK is updated**
   - Make sure you installed the NEW APK with updated URL
   - Uninstall old app first

---

### Test Backend Connection

**On your phone's browser:**
1. Open Chrome on Android
2. Go to: `http://YOUR_IP:5000`
   - Example: `http://192.168.1.100:5000`
3. You should see: `{"message": "Phishing Link Detection API", ...}`
4. If this works, backend is reachable!

---

### "Connection refused" Error

**This means:**
- Backend is not running, OR
- Firewall is blocking, OR
- Wrong IP address

**Fix:**
1. Make sure `python app.py` is running
2. Check firewall settings
3. Verify IP address is correct

---

### "Timeout" Error

**This means:**
- Backend is too slow, OR
- Network is slow

**Fix:**
1. Check internet connection
2. Make sure backend is running
3. Try again

---

## 📋 Quick Checklist

Before testing on Android phone:
- [ ] Found computer's IP address
- [ ] Updated BACKEND_URL in MainActivity.kt
- [ ] Rebuilt APK
- [ ] Installed new APK on phone
- [ ] Backend server is running (`python app.py`)
- [ ] Phone and computer on same WiFi
- [ ] Firewall allows connections

---

## 🎯 Quick Reference

**For Emulator:**
```kotlin
private val BACKEND_URL = "http://10.0.2.2:5000/predict"
```

**For Physical Android Phone:**
```kotlin
private val BACKEND_URL = "http://192.168.1.100:5000/predict"
```
(Use your computer's actual IP)

---

## 💡 Pro Tips

1. **Save your IP address** - Write it down for future use
2. **Check IP if you change WiFi** - IP changes when you switch networks
3. **Keep backend running** - Don't close the terminal while using app
4. **Test in browser first** - Use phone's browser to test backend connection

---

## ✅ That's It!

Once you update the BACKEND_URL and rebuild, your Android app will work perfectly! 🚀

