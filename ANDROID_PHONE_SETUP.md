# 📱 Android Phone Setup Guide

App ro run on a  Android phone.

---

## ⚠️ Current Issue

error msj: **"Network error. Make sure backend is running on port 5000"**

 happens because  app  trying to connect to `10.0.2.2` (emulator address) but  using a Android phone.

---

## 🔧 Fix: Update Backend URL for  Device

### Step 1:  Computer's IP Address



ifconfig | grep "inet " | grep -v 127.0.0.1

output : inet 172.16.40.113 netmask 0xfffff800 broadcast 172.16.47.255


---

### Step 2: Update MainActivity.kt

1. Open: `android-client/app/src/main/java/com/example/phishing/MainActivity.kt`

2. line 16:
   kotlin
   private val BACKEND_URL = "http://10.0.2.2:5000/predict"
  

3. **Change it to  computer's IP:**
   kotlin
   private val BACKEND_URL = "http://192.168.1.100:5000/predict"
  
   Replace `192.168.1.100` with  computer's IP address

4. **Save the file**

---

### Step 3: Rebuild the APK



**Using GitHub Actions**
1. Commit and push  change:
   
   git add android-client/app/src/main/java/com/example/phishing/MainActivity.kt
   git commit -m "Update backend URL for physical Android device"
   git push origin main
   
2.  GitHub → Actions → Build APK
3. Download new APK

### Step 4: Install Updated APK on Phone

1. Uninstall the old app  
2. Transfer the new APK 
3. Install the new APK
4. Open the app

---

### Step 5: Start Backend Server

1. On  Terminal
2. Navigate to backend:
  
   cd /Users/ghaidaa/Phishing-Link-Detection-App/backend
  
3. Start server:
   
   python app.py
   
4. output will be : `Running on http://0.0.0.0:5000`
5. should be running while using the app

---

### Step 6: Connect Phone to Same WiFi as computer

1. On Android phone: Settings → Wi-Fi
2. connect phon to same WiFi network as  computer


---

### Step 7: Test the App

1. Open the app 
2. Enter a URL:for example `https://www.google.com`
3. click **"CHECK URL"**


---


