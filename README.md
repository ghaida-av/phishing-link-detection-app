# Phishing Link Detection App

A simple Android app to check whether a URL is phishing or safe using a Python Flask backend.  


---

## 🏗 Architecture

| Layer | Technology | Purpose |
|-------|------------|---------|
| Frontend (Mobile) | Android + Kotlin | Collect URL input and display results |
| Network Library | OkHttp | Send HTTP POST requests to backend |
| Backend | Python Flask | Evaluate URLs and return JSON verdicts |
| Tunnel | ngrok | Expose local Flask server to the internet |

---

## ⚙️ Setup

### Backend (Flask)

1. Create virtual environment and activate:

```bash
python3 -m venv venv
source venv/bin/activate


