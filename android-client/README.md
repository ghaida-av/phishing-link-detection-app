# Phishing Link Detection Android App

Modern Android application for detecting phishing URLs using Machine Learning.

## Features

- 🎨 **Modern Material Design UI**
- 🔍 **Real-time URL Analysis**
- 📊 **Detailed Risk Scoring**
- 📝 **Analysis Reasons Display**
- ⚡ **Loading States & Error Handling**
- 🤖 **ML-Powered Detection**

## Setup

### Prerequisites

- Android Studio (latest version)
- Android SDK (API 24+)
- Backend server running (see backend README)

### Installation

1. **Open Project in Android Studio**
   - Open Android Studio
   - Select "Open an Existing Project"
   - Navigate to `android-client` folder
   - Click OK

2. **Sync Gradle**
   - Android Studio will automatically sync Gradle
   - Wait for dependencies to download

3. **Configure Backend URL**

   For **Android Emulator** (default):
   - The URL is already set to `http://10.0.2.2:5000/predict`
   - This maps to `localhost:5000` on your computer

   For **Physical Device**:
   - Find your computer's IP address:
     - Mac/Linux: `ifconfig` or `ip addr`
     - Windows: `ipconfig`
   - Update `BACKEND_URL` in `MainActivity.kt`:
     ```kotlin
     private val BACKEND_URL = "http://YOUR_IP_ADDRESS:5000/predict"
     ```

4. **Run the App**
   - Connect device or start emulator
   - Click Run button (▶️) in Android Studio
   - Or press `Shift + F10`

## Usage

1. Enter a URL in the input field
2. Click "Check URL" button
3. View the analysis results:
   - **Verdict**: Phishing or Legitimate
   - **Risk Score**: Percentage score
   - **Confidence**: High/Medium/Low
   - **Analysis Details**: List of reasons

## Project Structure

```
android-client/
├── app/
│   ├── src/
│   │   └── main/
│   │       ├── java/com/example/phishing/
│   │       │   └── MainActivity.kt
│   │       ├── res/
│   │       │   ├── layout/
│   │       │   │   └── activity_main.xml
│   │       │   └── values/
│   │       │       └── strings.xml
│   │       └── AndroidManifest.xml
│   └── build.gradle
└── README.md
```

## Dependencies

- **OkHttp**: HTTP client for API calls
- **Material Components**: Modern UI components
- **AndroidX**: Android support libraries

## Troubleshooting

### Network Error
- Ensure backend server is running
- Check backend URL is correct
- Verify device/emulator can reach the server
- Check firewall settings

### Build Errors
- Clean and rebuild: `Build > Clean Project`, then `Build > Rebuild Project`
- Invalidate caches: `File > Invalidate Caches / Restart`
- Sync Gradle: `File > Sync Project with Gradle Files`

### App Crashes
- Check Logcat for error messages
- Ensure all permissions are granted
- Verify backend is responding correctly

## Building APK

1. **Build > Generate Signed Bundle / APK**
2. Select **APK**
3. Create or select keystore
4. Choose build variant (release)
5. Click Finish

The APK will be generated in `app/release/`

## Notes

- Minimum SDK: 24 (Android 7.0)
- Target SDK: 34 (Android 14)
- Requires Internet permission (already configured)
