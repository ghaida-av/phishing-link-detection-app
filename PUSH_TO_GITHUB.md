# 🚀 Push Your Code to GitHub - Simple Steps

You already have a GitHub repository! Just follow these steps:

---

## Step 1: Commit Your Changes

Open Terminal and run:

```bash
cd /Users/ghaidaa/Phishing-Link-Detection-App
git add .
git commit -m "Add simplified app and GitHub Actions workflow"
```

---

## Step 2: Push to GitHub

```bash
git push origin main
```

**If asked for credentials:**
- **Username**: `ghaida-av`
- **Password**: Use a **Personal Access Token** (see below if needed)

---

## Step 3: Create Personal Access Token (If Needed)

If GitHub asks for a password, you need a token:

1. Go to: **https://github.com/settings/tokens**
2. Click **Generate new token** → **Generate new token (classic)**
3. Fill in:
   - **Note**: "APK Build"
   - **Expiration**: 90 days
   - **Scopes**: Check ✅ **repo** (all repo permissions)
4. Click **Generate token**
5. **COPY THE TOKEN** (you won't see it again!)
6. Use this token as your password when pushing

---

## Step 4: Build APK on GitHub

After pushing:

1. Go to: **https://github.com/ghaida-av/phishing-link-detection-app**
2. Click **Actions** tab (top menu)
3. You'll see **"Build APK"** workflow
4. Click **Run workflow** → **Run workflow** (green button)
5. Wait 5-10 minutes
6. When done, click on the completed run
7. Scroll down to **Artifacts**
8. Click **app-debug** to download
9. Extract ZIP - your APK is inside!

---

## ✅ That's It!

Your APK will be ready in 5-10 minutes!

---

## 🆘 Troubleshooting

**"Authentication failed"**
- Use Personal Access Token instead of password
- Make sure token has **repo** permissions

**"Workflow not showing"**
- Make sure you pushed the `.github/workflows/build-apk.yml` file
- Check Actions tab is enabled

**Need help?** Just ask!

