# 🌐 Web Version - Phishing Link Detector

Mobile-friendly web version that works on iPhone, Android, and any device with a browser!

## 🚀 Quick Start

### Option 1: Open Directly (Simplest)

1. **Start your backend server:**
   ```bash
   cd backend
   python app.py
   ```

2. **Open `index.html` in your browser:**
   - Double-click `index.html`
   - Or drag it into your browser
   - Or use a local web server (see below)

3. **On iPhone:**
   - Make sure iPhone and computer are on same WiFi
   - Update `BACKEND_URL` in `index.html` to your computer's IP
   - Open the HTML file in Safari

### Option 2: Use Local Web Server (Recommended)

**Python:**
```bash
cd web
python3 -m http.server 8000
```
Then open: http://localhost:8000

**Node.js:**
```bash
cd web
npx http-server -p 8000
```

**PHP:**
```bash
cd web
php -S localhost:8000
```

## 📱 Using on iPhone

### Step 1: Find Your Computer's IP Address

**Mac:**
```bash
ifconfig | grep "inet " | grep -v 127.0.0.1
```

**Windows:**
```bash
ipconfig
```
Look for IPv4 address (e.g., 192.168.1.100)

### Step 2: Update Backend URL

1. Open `index.html` in a text editor
2. Find this line:
   ```javascript
   const BACKEND_URL = 'http://localhost:5000/predict';
   ```
3. Change to your computer's IP:
   ```javascript
   const BACKEND_URL = 'http://192.168.1.100:5000/predict';
   ```
   (Replace 192.168.1.100 with your actual IP)

### Step 3: Start Backend

```bash
cd backend
python app.py
```

### Step 4: Start Web Server

```bash
cd web
python3 -m http.server 8000
```

### Step 5: Access from iPhone

1. On iPhone, open Safari
2. Go to: `http://YOUR_COMPUTER_IP:8000`
   - Example: `http://192.168.1.100:8000`
3. Make sure iPhone and computer are on **same WiFi network**

### Step 6: Add to Home Screen (Optional)

1. In Safari, tap the **Share** button (square with arrow)
2. Tap **"Add to Home Screen"**
3. Tap **"Add"**
4. Now you have an app icon on your home screen!

## 🌍 Deploy to Web (Production)

### Option 1: GitHub Pages (Free)

1. Push `web` folder to GitHub
2. Go to repository Settings → Pages
3. Select source branch
4. Your site will be at: `https://username.github.io/repo-name`

### Option 2: Netlify (Free)

1. Go to https://netlify.com
2. Drag and drop the `web` folder
3. Get instant URL

### Option 3: Vercel (Free)

1. Go to https://vercel.com
2. Import your repository
3. Deploy automatically

## 🔧 Configuration

### Update Backend URL

Edit `index.html` and change:
```javascript
const BACKEND_URL = 'http://localhost:5000/predict';
```

To your backend URL:
```javascript
const BACKEND_URL = 'https://your-backend.com/predict';
```

## ✨ Features

- ✅ Works on iPhone Safari
- ✅ Works on Android Chrome
- ✅ Works on desktop browsers
- ✅ Mobile-responsive design
- ✅ Beautiful UI
- ✅ Same ML backend
- ✅ Real-time analysis
- ✅ Detailed results

## 📋 Requirements

- Backend server running (Flask API)
- Web browser (Safari, Chrome, Firefox, etc.)
- Internet connection (for API calls)

## 🆘 Troubleshooting

### "Network error" on iPhone
- Make sure backend is running
- Check computer's IP address is correct
- Verify iPhone and computer are on same WiFi
- Check firewall isn't blocking port 5000

### "Can't connect to backend"
- Make sure Flask server is running: `python app.py`
- Check backend URL in `index.html`
- Try `http://` instead of `https://` for local testing

### "CORS error"
- Backend already has CORS enabled
- If still issues, check backend `app.py` has `CORS(app)`

## 🎯 That's It!

Your web app is ready to use on iPhone! 🎉

