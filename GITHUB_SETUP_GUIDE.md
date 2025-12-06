# 🚀 Complete GitHub Setup Guide - Step by Step

Follow these steps to set up GitHub and build your APK automatically!

---

## Step 1: Create GitHub Account (If You Don't Have One)

1. Go to **https://github.com**
2. Click **Sign up** (top right)
3. Enter your:
   - Username
   - Email address
   - Password
4. Click **Create account**
5. Verify your email (check inbox)

**✅ Done! You now have a GitHub account!**

---

## Step 2: Create a New Repository

1. After logging in, click the **+** icon (top right)
2. Click **New repository**
3. Fill in:
   - **Repository name**: `phishing-link-detection-app` (or any name you like)
   - **Description**: "Phishing Link Detection App with ML"
   - **Visibility**: Choose **Public** (free) or **Private**
   - **DO NOT** check "Initialize with README" (we already have files)
4. Click **Create repository**

**✅ Repository created!**

---

## Step 3: Push Your Code to GitHub

### Option A: Using Terminal (Recommended)

Open Terminal and run these commands one by one:

```bash
# Navigate to your project
cd /Users/ghaidaa/Phishing-Link-Detection-App

# Initialize git (if not already done)
git init

# Add all files
git add .

# Create first commit
git commit -m "Initial commit: Phishing Detection App"

# Add your GitHub repository (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/phishing-link-detection-app.git

# Push to GitHub
git branch -M main
git push -u origin main
```

**When prompted:**
- **Username**: Your GitHub username
- **Password**: Use a **Personal Access Token** (see Step 4 below)

### Option B: Using GitHub Desktop (Easier)

1. Download **GitHub Desktop**: https://desktop.github.com
2. Install and sign in with your GitHub account
3. Click **File** → **Add Local Repository**
4. Select `/Users/ghaidaa/Phishing-Link-Detection-App`
5. Click **Publish repository**
6. Choose your repository name
7. Click **Publish**

**✅ Code is now on GitHub!**

---

## Step 4: Create Personal Access Token (For Terminal Method)

If using Terminal, you'll need a token instead of password:

1. Go to GitHub.com → Click your **profile picture** (top right)
2. Click **Settings**
3. Scroll down → Click **Developer settings** (left sidebar)
4. Click **Personal access tokens** → **Tokens (classic)**
5. Click **Generate new token** → **Generate new token (classic)**
6. Fill in:
   - **Note**: "APK Build"
   - **Expiration**: Choose 90 days (or longer)
   - **Scopes**: Check **repo** (all repo permissions)
7. Click **Generate token**
8. **COPY THE TOKEN** (you won't see it again!)
9. Use this token as your password when pushing code

---

## Step 5: Enable GitHub Actions

1. Go to your repository on GitHub
2. Click the **Actions** tab (top menu)
3. If you see "Workflows aren't being run on this forked repository", click:
   - **I understand my workflows, go ahead and enable them**
4. You should see **"Build APK"** workflow listed

**✅ GitHub Actions is enabled!**

---

## Step 6: Build Your APK

### Automatic Build (After Push):
- The workflow will run automatically when you push code
- Go to **Actions** tab to see it running

### Manual Build:
1. Go to **Actions** tab
2. Click **Build APK** workflow (left sidebar)
3. Click **Run workflow** (right side)
4. Click the green **Run workflow** button
5. Wait 5-10 minutes for build to complete

**✅ Build started!**

---

## Step 7: Download Your APK

1. Go to **Actions** tab
2. Click on the latest workflow run (the one with a checkmark ✅ or in progress ⏳)
3. Scroll down to **Artifacts** section
4. Click **app-debug** to download
5. Extract the ZIP file
6. Your **app-debug.apk** is inside!

**🎉 APK Ready!**

---

## Step 8: Install on Your Phone

1. **Transfer APK** to your phone:
   - Email it to yourself
   - Upload to Google Drive/Dropbox
   - Transfer via USB

2. **Enable Unknown Sources**:
   - Settings → Security → Install Unknown Apps
   - Enable for the app you'll use (Files, Chrome, etc.)

3. **Install**:
   - Open the APK file
   - Tap **Install**
   - Done! 🎉

---

## 🆘 Troubleshooting

### "Repository not found"
- Check your repository name is correct
- Make sure you're logged into GitHub

### "Authentication failed"
- Use Personal Access Token instead of password
- Make sure token has **repo** permissions

### "Workflow not running"
- Make sure `.github/workflows/build-apk.yml` exists
- Check Actions tab is enabled
- Try clicking "I understand my workflows"

### Build Fails
- Check the workflow logs in Actions tab
- Look for error messages
- Common issues: Missing files, syntax errors

---

## 📋 Quick Command Reference

```bash
# Check if git is initialized
git status

# Add all files
git add .

# Commit
git commit -m "Your message"

# Push to GitHub
git push origin main

# Check remote
git remote -v
```

---

## ✅ Checklist

- [ ] GitHub account created
- [ ] Repository created
- [ ] Code pushed to GitHub
- [ ] GitHub Actions enabled
- [ ] Workflow run successfully
- [ ] APK downloaded
- [ ] APK installed on phone

---

## 🎯 Next Steps After Setup

1. **Start Backend Server**:
   ```bash
   cd backend
   python app.py
   ```

2. **Open App on Phone**
3. **Enter URL** to check
4. **Enjoy your app!**

---

**Need help with any step? Just ask!** 😊

