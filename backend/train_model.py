"""
Training script for Phishing URL Detection ML Model
This script trains a Random Forest classifier on URL features
"""

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib
from detector import extract_features
import re
from urllib.parse import urlparse

# Sample dataset - In production, use a larger, real dataset
# Format: (url, label) where label is 1 for phishing, 0 for legitimate

def generate_training_data():
    """Generate synthetic training data based on known patterns"""
    phishing_urls = [
        "http://192.168.1.1/login.php",
        "https://secure-account-update.verify-bank.com/confirm",
        "http://paypal-webscr.com/update",
        "https://appleid-verify.apple.com@malicious.com/login",
        "http://very.long.subdomain.example.com/login",
        "https://bank-verify-secure.com/account/update",
        "http://123.45.67.89/paypal/login",
        "https://suspicious-site.com/verify-account-now",
        "http://login-secure-bank.com/confirm",
        "https://update-account-verify.com/password/reset",
        "http://paypal@fake.com/webscr",
        "https://very.very.long.subdomain.example.com/login",
        "http://192.168.0.1/secure/login",
        "https://account-update-verify-bank.com",
        "http://ebay-secure-login.com/verify",
        "https://appleid@phishing.com/confirm",
        "http://long-url-with-many-characters-to-make-it-suspicious.com/path/to/resource",
        "https://secure.bank.update.verify.com/login",
        "http://123.123.123.123/paypal",
        "https://suspicious-keyword-login-verify.com"
    ]
    
    legitimate_urls = [
        "https://www.google.com",
        "https://github.com",
        "https://stackoverflow.com/questions",
        "https://www.wikipedia.org",
        "https://www.youtube.com",
        "https://www.amazon.com",
        "https://www.microsoft.com",
        "https://www.apple.com",
        "https://www.paypal.com",
        "https://www.ebay.com",
        "https://www.facebook.com",
        "https://www.twitter.com",
        "https://www.linkedin.com",
        "https://www.reddit.com",
        "https://www.netflix.com",
        "https://www.spotify.com",
        "https://www.instagram.com",
        "https://www.tiktok.com",
        "https://www.dropbox.com",
        "https://www.cloudflare.com"
    ]
    
    # Create labeled dataset
    urls = phishing_urls + legitimate_urls
    labels = [1] * len(phishing_urls) + [0] * len(legitimate_urls)
    
    return urls, labels

def extract_features_vector(url):
    """Extract features as a vector for ML model"""
    parsed = urlparse(url)
    netloc = parsed.netloc.lower()
    path = parsed.path or ''
    query = parsed.query or ''
    full_url = url.lower()
    
    # Feature extraction
    features = []
    
    # URL length
    features.append(len(url))
    
    # Has IP address
    ip_pattern = r'^\d{1,3}(\.\d{1,3}){3}$'
    netloc_clean = netloc.split(':')[0]
    features.append(1 if re.match(ip_pattern, netloc_clean) else 0)
    
    # Number of dots in domain
    features.append(netloc.count('.'))
    
    # Has @ symbol
    features.append(1 if '@' in url else 0)
    
    # Has HTTPS
    features.append(1 if parsed.scheme.lower() == 'https' else 0)
    
    # Number of subdomains
    parts = netloc.split('.')
    features.append(len(parts))
    
    # Suspicious keywords count
    suspicious_keywords = ['login', 'secure', 'account', 'update', 'verify', 'bank', 
                          'confirm', 'webscr', 'signin', 'password', 'ebay', 'paypal', 
                          'appleid', 'confirm']
    keyword_count = sum(1 for keyword in suspicious_keywords if keyword in full_url)
    features.append(keyword_count)
    
    # Path length
    features.append(len(path))
    
    # Query length
    features.append(len(query))
    
    # Number of slashes
    features.append(url.count('/'))
    
    # Number of hyphens
    features.append(url.count('-'))
    
    # Number of underscores
    features.append(url.count('_'))
    
    # Has port number
    features.append(1 if ':' in netloc and not netloc.endswith(':') else 0)
    
    return np.array(features)

def train_model():
    """Train the ML model"""
    print("Generating training data...")
    urls, labels = generate_training_data()
    
    print("Extracting features...")
    X = np.array([extract_features_vector(url) for url in urls])
    y = np.array(labels)
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    print("Training Random Forest model...")
    # Use Random Forest classifier
    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=10,
        random_state=42,
        n_jobs=-1
    )
    
    model.fit(X_train, y_train)
    
    # Evaluate
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\nModel Accuracy: {accuracy:.2%}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=['Legitimate', 'Phishing']))
    
    # Save model
    model_path = 'phishing_model.pkl'
    joblib.dump(model, model_path)
    print(f"\nModel saved to {model_path}")
    
    return model

if __name__ == '__main__':
    train_model()

