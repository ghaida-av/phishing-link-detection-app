import re
from urllib.parse import urlparse

def extract_features_vector(url):
    """Simple feature extraction for the ML model"""
    parsed = urlparse(url)
    netloc = parsed.netloc.lower()
    
    # Simple ML features
    features = {
        "url_length": len(url),
        "num_dots": netloc.count('.'),
        "has_ip": 1 if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", netloc) else 0,
        "has_at_symbol": 1 if "@" in url else 0,
        "is_https": 1 if url.startswith("https") else 0
    }
    
    # Basic logic: If URL is long and has no HTTPS, it's risky
    is_phishing = False
    if features["url_length"] > 75 or features["has_at_symbol"] == 1 or features["is_https"] == 0:
        is_phishing = True
        
    return is_phishing, features

def predict_url(url):
    is_phishing, features = extract_features_vector(url)
    return {
        "verdict": "phishing" if is_phishing else "legitimate",
        "score": 0.88 if is_phishing else 0.12
    }





