# 🎯 Quick APK Build Guide

Since the "Build APK" menu option isn't showing, here are **3 EASY ways** to build:

---

## ✅ Method 1: Use the Build Script (Easiest!)

I've created a script for you. Just run:

```bash
cd /Users/ghaidaa/Phishing-Link-Detection-App
./build_apk.sh
```

That's it! The script will build your APK automatically.

---

## ✅ Method 2: Android Studio - Make Project

1. **Open Android Studio**
2. **Open** the `android-client` folder
3. **Wait** for Gradle sync to finish (bottom right)
4. Press **`Cmd + F9`** (Mac) or **`Ctrl + F9`** (Windows)
   - OR click **Build** → **Make Project**
5. **Wait** for build to complete
6. **Find APK** at: `app/build/outputs/apk/debug/app-debug.apk`

**To find it:**
- Right-click `app` folder → **Show in Finder** (Mac)
- Navigate to: `build/outputs/apk/debug/`

---

## ✅ Method 3: Android Studio Terminal

1. **Open Android Studio**
2. **Open** the `android-client` project  
3. Click **Terminal** tab at bottom (or View → Tool Windows → Terminal)
4. Type:
```bash
./gradlew assembleDebug
```
5. Press **Enter**
6. Wait for "BUILD SUCCESSFUL"
7. APK is at: `app/build/outputs/apk/debug/app-debug.apk`

---

## 📱 After Building - Install on Phone

1. **Copy** `app-debug.apk` to your phone (USB, email, or cloud)
2. **Enable** "Install from Unknown Sources" in phone Settings
3. **Open** the APK file on your phone
4. **Tap** Install

---

## 🎯 Which Method Should I Use?

- **Method 1** if you're comfortable with terminal
- **Method 2** if you prefer using Android Studio menus
- **Method 3** if you want to see the build process

**All methods create the same APK file!**

---

## ⚠️ Still Having Issues?

If nothing works:
1. Make sure Android Studio is fully opened
2. Wait for "Gradle Sync" to complete (check bottom status bar)
3. Try **File** → **Invalidate Caches / Restart**
4. Then try Method 2 again

---

**Your APK will be ready in 2-5 minutes!** 🚀

