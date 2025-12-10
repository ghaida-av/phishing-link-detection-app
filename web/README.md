# 🌐  Phishing Link Detection Web App 

 works on any device browser!


### Open Directly 

1. **Start  backend server:**
   
   cd backend
   python app.py
  

2. **Open `index.html` in your browser:**
   - Double-click `index.html`
   

3. **On iPhone:**
   - Make sure iPhone and computer are on same WiFi
   - Update `BACKEND_URL` in `index.html` to your computer's IP
   - Open the HTML file in Safari



## 🌍 Deploy to Web 

### 1: GitHub Pages 

1. Push `web` folder to GitHub
2. Go to repository Settings → Pages
3. Select source branch
4.  site will be at: `https://username.github.io/repo-name`

###  2: Netlify 

1. Go to https://netlify.com
2. Drag and drop the `web` folder
3. Get instant URL

###  3: Vercel 

1. Go to https://vercel.com
2. Import your repository
3. Deploy automatically

## 🔧 Configuration

### Update Backend URL

Edit `index.html` and change:
```javascript
const BACKEND_URL = 'http://localhost:5000/predict';
```

To  backend URL:
```javascript
const BACKEND_URL = 'https://-backend.com/predict';
```

