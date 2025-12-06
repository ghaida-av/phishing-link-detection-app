# 🎯 Build APK Using Android Studio (Recommended)

Since command-line build has Java version issues, **Android Studio is the easiest way**:

## ✅ Step-by-Step Instructions

### Step 1: Open Project
1. Open **Android Studio**
2. Click **File** → **Open**
3. Navigate to and select the **`android-client`** folder
4. Click **OK**

### Step 2: Wait for Gradle Sync
- Android Studio will automatically sync Gradle
- Wait for "Gradle Sync Finished" message (bottom right)
- This may take 2-5 minutes the first time

### Step 3: Build APK
**Option A - Keyboard Shortcut (Fastest):**
- Press **`Cmd + F9`** (Mac) or **`Ctrl + F9`** (Windows)
- Wait for build to complete

**Option B - Menu:**
- Click **Build** menu at top
- Click **Make Project**
- Wait for build to complete

**Option C - Right-Click:**
- In Project view (left side), right-click on **`app`** folder
- Select **Build** → **Build APK**

### Step 4: Find Your APK
After build completes:

1. **Right-click** on the **`app`** folder in Project view
2. Click **Show in Finder** (Mac) or **Show in Explorer** (Windows)
3. Navigate to: **`build/outputs/apk/debug/`**
4. Your APK file is: **`app-debug.apk`**

### Step 5: Install on Phone
1. **Copy** `app-debug.apk` to your phone (USB, email, or cloud)
2. **Enable** "Install from Unknown Sources" in phone Settings
3. **Open** the APK file on your phone
4. **Tap** Install

---

## 🎉 That's It!

Android Studio handles all the Java/Gradle version issues automatically, so this is the most reliable method.

---

## 📱 Quick Reference

- **Build**: `Cmd + F9` (Mac) or `Ctrl + F9` (Windows)
- **APK Location**: `app/build/outputs/apk/debug/app-debug.apk`
- **Show Folder**: Right-click `app` → Show in Finder/Explorer

