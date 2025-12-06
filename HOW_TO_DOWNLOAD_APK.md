# 📱 How to Download Your APK from GitHub Actions - Step by Step

Complete guide to download your built APK file from GitHub.

---

## Step 1: Go to Your GitHub Repository

1. Open your web browser
2. Go to: **https://github.com/ghaida-av/phishing-link-detection-app**
3. You should see your repository page

---

## Step 2: Open the Actions Tab

1. Look at the **top menu** of your repository
2. You'll see tabs: **Code**, **Issues**, **Pull requests**, **Actions**, etc.
3. Click on **"Actions"** tab
4. You'll see a list of workflow runs

---

## Step 3: Find Your Build Workflow

1. In the **left sidebar**, you'll see **"Workflows"**
2. Click on **"Build APK"** workflow
3. You'll see a list of all build runs

**OR**

1. Look at the main area - you'll see workflow runs listed
2. Find the one that says **"Build APK"** or **"workflow_dispatch"**
3. Click on it

---

## Step 4: Open the Completed Workflow Run

1. Look for a workflow run with a **green checkmark** ✅ (successful)
   - If it's still running, you'll see a yellow circle ⏳
   - Wait until it shows a green checkmark ✅

2. **Click on the workflow run** (the title/name of the run)
   - Example: "Build APK" or "workflow_dispatch"

3. This opens the detailed view of that run

---

## Step 5: Scroll to the Artifacts Section

1. On the workflow run page, **scroll down**
2. Look for a section called **"Artifacts"**
   - It's usually near the bottom of the page
   - Below all the job steps

3. You should see a box that says:
   ```
   Artifacts
   app-debug
   ```

---

## Step 6: Download the Artifact

1. In the **Artifacts** section, you'll see **"app-debug"**
2. **Click on "app-debug"**
3. A ZIP file will start downloading
   - File name: `app-debug.zip`
   - Size: Usually 5-15 MB

---

## Step 7: Extract the ZIP File

### On Mac:
1. **Double-click** the downloaded `app-debug.zip` file
2. It will automatically extract
3. You'll see a folder or the APK file directly

### On Windows:
1. **Right-click** on `app-debug.zip`
2. Select **"Extract All..."**
3. Choose where to extract
4. Click **"Extract"**

### On Linux:
```bash
unzip app-debug.zip
```

---

## Step 8: Find Your APK File

1. After extracting, look for a file named: **`app-debug.apk`**
2. This is your Android app file!
3. File size: Usually 3-10 MB

---

## Step 9: Transfer to Your Phone

### Option A: Email
1. **Email the APK** to yourself
2. Open email on your phone
3. **Download** the attachment
4. **Open** the downloaded file

### Option B: Google Drive / Dropbox
1. **Upload** `app-debug.apk` to Google Drive or Dropbox
2. **Share** the file (or make it accessible)
3. Open Drive/Dropbox app on phone
4. **Download** the APK

### Option C: USB Cable
1. **Connect** phone to computer via USB
2. **Copy** `app-debug.apk` to your phone
3. Use file manager on phone to find it

### Option D: AirDrop (Mac + iPhone)
1. **Right-click** on `app-debug.apk`
2. Select **"Share"** → **"AirDrop"**
3. Choose your phone
4. Accept on phone

---

## Step 10: Enable Unknown Sources (Android)

Before installing, you need to allow installation from unknown sources:

1. Go to **Settings** on your Android phone
2. Go to **Security** (or **Privacy** on newer Android)
3. Find **"Install unknown apps"** or **"Install apps from unknown sources"**
4. **Enable** it for the app you'll use:
   - If using **Files** app → Enable for "Files"
   - If using **Chrome** → Enable for "Chrome"
   - If using **Email** → Enable for "Gmail" or your email app

**Note**: On Android 8.0+, you enable it per app, not globally.

---

## Step 11: Install the APK

1. **Open** the APK file on your phone
   - Tap the downloaded file
   - Or use a file manager to find it

2. You'll see an **"Install"** button
3. **Tap "Install"**
4. Wait a few seconds
5. You'll see **"App installed"** or **"Open"** button
6. **Tap "Open"** to launch the app!

---

## ✅ Success!

Your Phishing Detection App is now installed on your phone! 🎉

---

## 🆘 Troubleshooting

### "Artifacts section not showing"
- **Wait longer** - Artifacts appear after build completes
- **Refresh the page** (F5 or Cmd+R)
- Make sure the build was **successful** (green checkmark)

### "Can't download artifact"
- **Try a different browser** (Chrome, Firefox, Safari)
- **Check your internet connection**
- **Clear browser cache** and try again

### "APK won't install on phone"
- Make sure **"Unknown sources"** is enabled
- Check if you have **enough storage** space
- Try **downloading again** (file might be corrupted)

### "Can't find the APK after extracting"
- Look in your **Downloads** folder
- Check the **extracted folder** contents
- The file is named **`app-debug.apk`**

### "Build is still running"
- **Wait** - Builds take 5-10 minutes
- Check the progress in the workflow run
- You'll see steps like "Set up JDK", "Build APK", etc.
- Wait for **"BUILD SUCCESSFUL"** message

---

## 📋 Quick Checklist

- [ ] Opened GitHub repository
- [ ] Clicked "Actions" tab
- [ ] Found "Build APK" workflow
- [ ] Opened completed workflow run (green checkmark ✅)
- [ ] Scrolled to "Artifacts" section
- [ ] Clicked "app-debug" to download
- [ ] Extracted the ZIP file
- [ ] Found `app-debug.apk` file
- [ ] Transferred to phone
- [ ] Enabled "Unknown sources" in Settings
- [ ] Installed APK on phone
- [ ] App is working! 🎉

---

## 🎯 Visual Guide (What You'll See)

```
GitHub Repository Page
├── Top Menu: [Code] [Issues] [Pull requests] [Actions] ...
│
└── Actions Tab (after clicking)
    ├── Left Sidebar: Workflows
    │   └── Build APK ← Click this
    │
    └── Main Area: Workflow Runs
        └── ✅ Build APK (workflow_dispatch) ← Click this
            │
            └── Scroll Down
                └── Artifacts Section
                    └── app-debug ← Click to download
                        └── Downloads as: app-debug.zip
                            └── Extract → app-debug.apk
```

---

## 💡 Pro Tips

1. **Bookmark** your repository Actions page for quick access
2. **Keep** the APK file as backup (save it somewhere safe)
3. **Check** the build logs if something goes wrong
4. **Download** immediately - Artifacts are kept for 90 days

---

## 📞 Need Help?

If you're stuck at any step:
1. Check the **Troubleshooting** section above
2. Look at the **workflow logs** for error messages
3. Make sure the build was **successful** (green checkmark)

---

**That's it! You now have your APK installed on your phone!** 🚀

