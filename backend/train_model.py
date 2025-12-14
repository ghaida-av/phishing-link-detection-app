
"""
Phishing Link Detection - Machine Learning Model

"""

import re
import joblib
import numpy as np
from urllib.parse import urlparse
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def generate_training_data():
    phishing_urls = [
        "http://192.168.1.1/login.php",
        "https://secure-account-update.verify-bank.com/confirm",
        "http://paypal-webscr.com/update",
        "https://appleid@fake.com/login",
        "http://123.45.67.89/paypal",
        "https://verify-account-bank.com",
        "http://login-secure-bank.com",
        "https://update-password-now.com"
    ]

    safe_urls = [
        "https://www.google.com",
        "https://www.github.com",
        "https://www.amazon.com",
        "https://www.apple.com",
        "https://www.microsoft.com",
        "https://www.wikipedia.org",
        "https://www.paypal.com",
        "https://www.youtube.com"
    ]

    urls = phishing_urls + safe_urls
    labels = [1] * len(phishing_urls) + [0] * len(safe_urls)

    return urls, labels



def extract_features(url):
    parsed = urlparse(url)
    domain = parsed.netloc.lower()
    path = parsed.path.lower()

    features = [
        len(url),                              # URL length
        url.count('.'),                        # number of dots
        url.count('-'),                        # number of hyphens
        1 if '@' in url else 0,                # has @
        1 if parsed.scheme == "https" else 0,  # HTTPS
        len(path),                             # path length
        1 if re.match(r"\d+\.\d+\.\d+\.\d+", domain) else 0,  # IP in URL
        sum(word in url.lower() for word in [
            "login", "verify", "update", "secure", "bank", "account"
        ])
    ]

    return np.array(features)



def train_model():
    urls, labels = generate_training_data()

    X = np.array([extract_features(url) for url in urls])
    y = np.array(labels)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    accuracy = accuracy_score(y_test, model.predict(X_test))
    print(f"Model Accuracy: {accuracy:.2%}")

    joblib.dump(model, "phishing_model.pkl")
    print("Model saved as phishing_model.pkl")


if __name__ == "__main__":
    train_model()








