#!/bin/bash

show_android_studio_instructions() {
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "💡  Use Android Studio "
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    echo "📋 Simple Steps:"
    echo "   1. Open Android Studio"
    echo "   2. File → Open → Select 'android-client' folder"
    echo "   3. Wait for Gradle sync to finish"
    echo "   4. Press Cmd+F9 (Mac) "
    echo "   5. Find APK: Right-click 'app' folder → Show in Finder"
    echo "      Navigate to: build/outputs/apk/debug/app-debug.apk"
    echo ""
    echo "📖 See ANDROID_PHONE_SETUP.md for detailed instructions"
    echo ""
}

echo "🚀 Building Phishing Detection App APK..."
echo ""

cd "$(dirname "$0")/android-client"

# Check if gradlew exists and is executable
if [ ! -f "./gradlew" ]; then
    echo "❌ Gradle wrapper not found."
    echo ""
    show_android_studio_instructions
    exit 1
fi

# Make gradlew executable
chmod +x ./gradlew

echo "📦 Building APK  may take a few minutes"
echo ""

# Build the APK
./gradlew assembleDebug 2>&1 | tee /tmp/gradle_build.log

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ BUILD SUCCESSFUL!"
    echo ""
    echo "📱  APK is located at:"
    echo "   $(pwd)/app/build/outputs/apk/debug/app-debug.apk"
    echo ""
    
    # Try to open the folder (Mac)
    if [[ "$OSTYPE" == "darwin"* ]]; then
        echo "📂 Opening APK folder..."
        open app/build/outputs/apk/debug/ 2>/dev/null || true
    fi
    
    echo "📲 To install on your phone:"
    echo "   1. Copy app-debug.apk to  phone"
    echo "   2. Enable 'Install from Unknown Sources' in Settings"
    echo "   3. Open the APK file and install"
else
    echo ""
    echo "❌ Command-line build failed "
    echo ""
    show_android_studio_instructions
fi

