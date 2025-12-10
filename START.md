#  Start Guide



### Step 1: Backend Setup 
on terminal :
cd backend
python3 -m venv venv
source venv/bin/activate  
pip install -r requirements.txt
python train_model.py
python app.py


✅ Backend is now running on `http://localhost:5000`

### Step 2: Android Setup 

1. **Open Android Studio**
   - File → Open → Select `android-client` folder

2. **Wait for Gradle Sync**
  
3. 
   - Tools → Device Manager → Create/Start emulator
   - OR connect  Android device via USB

4. **Run the App**
   - Click the green  Run button
   

✅ App is now running!

## 🧪 Test It Out

1. Open the app 
2. Enter a test URL:
   - **Safe**: `https://www.google.com`
   - **Phishing**: `http://192.168.1.1/login.php`
3. Click "Check URL"
4. View the results!

