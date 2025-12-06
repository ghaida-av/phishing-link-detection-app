# How to Build APK - Easy Methods

## Method 1: Using Terminal/Command Line (Easiest!)

### Step 1: Open Terminal
- Mac: Press `Cmd + Space`, type "Terminal"
- Windows: Press `Win + R`, type "cmd"

### Step 2: Navigate to Project
```bash
cd /Users/ghaidaa/Phishing-Link-Detection-App/android-client
```

### Step 3: Build APK
```bash
# If you have gradle installed globally:
gradle assembleDebug

# OR if Android Studio is installed, use its gradle:
# Mac:
~/Library/Android/sdk/tools/bin/sdkmanager --version
# Then use the gradle wrapper (if it exists) or install gradle
```

### Step 4: Find Your APK
After build completes, your APK will be at:
```
android-client/app/build/outputs/apk/debug/app-debug.apk
```

---

## Method 2: Using Android Studio Menu (Different Versions)

### For Android Studio 2023+:
1. Click **Build** menu at top
2. Look for:
   - **Build APK(s)** - Click this
   - OR **Generate Signed Bundle / APK** → Choose **APK**

### For Older Android Studio:
1. Click **Build** menu
2. Click **Make Project** (or press `Ctrl+F9` / `Cmd+F9`)
3. Then click **Build** → **Build APK**

### Alternative:
1. Right-click on **app** folder in Project view
2. Select **Build** → **Build APK**

---

## Method 3: Create Gradle Wrapper (If Needed)

If gradle commands don't work, create a wrapper:

```bash
cd android-client

# Install gradle wrapper
gradle wrapper --gradle-version 8.0

# Then build
./gradlew assembleDebug
```

---

## Method 4: Use Android Studio's Terminal

1. In Android Studio, click **View** → **Tool Windows** → **Terminal**
2. Type:
```bash
./gradlew assembleDebug
```
(If gradlew doesn't exist, see Method 3)

---

## Quick Check: Is Gradle Working?

Test if gradle is available:
```bash
gradle --version
```

If not installed, you can:
- Install via Homebrew (Mac): `brew install gradle`
- Or use Android Studio's built-in gradle

---

## After Building - Find Your APK

The APK will be located at:
```
android-client/app/build/outputs/apk/debug/app-debug.apk
```

**To find it easily:**
1. In Android Studio, right-click on **app** folder
2. Click **Show in Finder** (Mac) or **Show in Explorer** (Windows)
3. Navigate to: `build/outputs/apk/debug/`
4. Copy `app-debug.apk` to your phone!

---

## Still Having Issues?

Try this simple approach:
1. Open Android Studio
2. Open the `android-client` project
3. Wait for "Gradle Sync" to finish
4. Look at the bottom toolbar for a **Terminal** icon
5. Click it and type: `./gradlew assembleDebug`
6. Press Enter
7. Wait for "BUILD SUCCESSFUL"
8. Your APK is ready!

