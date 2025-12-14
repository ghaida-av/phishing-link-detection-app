#!/bin/bash

show_android_studio_help() {
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "📱 Build APK using Android Studio"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    echo "1️⃣ Open Android Studio"
    echo "2️⃣ File → Open → select 'android-client' folder"
    echo "3️⃣ Wait for Gradle sync"
    echo "4️⃣ Press Build → Build APK"
    echo "5️⃣ APK location:"
    echo "   android-client/app/build/outputs/apk/debug/app-debug.apk"
    echo ""
}

echo " Building Phishing Link Detection App (Android APK)"
echo ""

cd "$(dirname "$0")/android-client" || {
    echo "❌ android-client folder not found"
    exit 1
}

# Check Gradle wrapper
if [ ! -f "./gradlew" ]; then
    echo "❌ Gradle wrapper missing"
    show_android_studio_help
    exit 1
fi

chmod +x ./gradlew

echo " Building APK (this may take a few minutes)..."
echo ""

./gradlew assembleDebug

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ APK BUILD SUCCESSFUL"
    echo ""
    echo " APK location:"
    echo "   android-client/app/build/outputs/apk/debug/app-debug.apk"

    # Open folder on macOS
    if [[ "$OSTYPE" == "darwin"* ]]; then
        open app/build/outputs/apk/debug/
    fi

    echo ""
    echo " Install on Android:"
    echo "1. Copy APK to phone"
    echo "2. Enable 'Install unknown apps'"
    echo "3. Tap APK to install"
else
    echo ""
    echo "❌ Build failed"
    show_android_studio_help
fi


