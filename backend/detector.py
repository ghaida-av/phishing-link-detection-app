import re
import os
import joblib
import numpy as np
from urllib.parse import urlparse

# Try to load ML model, fallback to heuristic if not available
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'phishing_model.pkl')
ml_model = None

try:
    if os.path.exists(MODEL_PATH):
        ml_model = joblib.load(MODEL_PATH)
        print(f"Loaded ML model from {MODEL_PATH}")
    else:
        print(f"ML model not found at {MODEL_PATH}, using heuristic fallback")
except Exception as e:
    print(f"Error loading ML model: {e}, using heuristic fallback")

SUSPICIOUS_KEYWORDS = [
    'login', 'secure', 'account', 'update', 'verify', 'bank', 'confirm',
    'webscr', 'signin', 'password', 'ebay', 'paypal', 'appleid', 'confirm'
]

def has_ip_address(netloc):
    # checks if netloc is an IP (v4)
    return re.match(r'^\d{1,3}(\.\d{1,3}){3}$', netloc) is not None

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
    keyword_count = sum(1 for keyword in SUSPICIOUS_KEYWORDS if keyword in full_url)
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

def extract_features(url):
    """Legacy feature extraction for heuristic fallback"""
    parsed = urlparse(url)
    netloc = parsed.netloc.lower()
    path = parsed.path or ''
    query = parsed.query or ''

    features = {
        'url_length': len(url),
        'has_ip': has_ip_address(netloc.split(':')[0]) if netloc else False,
        'num_dots': netloc.count('.'),
        'has_at': '@' in url,
        'suspicious_keyword': any(word in (path + query + netloc).lower() for word in SUSPICIOUS_KEYWORDS),
        'many_subdomains': len(netloc.split('.')) > 4,
        'has_https_scheme': parsed.scheme.lower() == 'https',
    }
    return features

def ml_predict(url):
    """Use ML model to predict phishing probability"""
    if ml_model is None:
        return None
    
    try:
        features = extract_features_vector(url)
        features = features.reshape(1, -1)
        
        # Get probability of phishing (class 1)
        proba = ml_model.predict_proba(features)[0]
        phishing_prob = proba[1] if len(proba) > 1 else proba[0]
        
        # Get prediction
        prediction = ml_model.predict(features)[0]
        
        return float(phishing_prob), int(prediction)
    except Exception as e:
        print(f"ML prediction error: {e}")
        return None

def get_reasons(url, score):
    """Generate reasons for the prediction"""
    reasons = []
    f = extract_features(url)
    
    if f['has_ip']:
        reasons.append('URL uses an IP address as host')
    
    if not f['has_https_scheme']:
        reasons.append('No HTTPS scheme detected')
    
    if f['num_dots'] >= 4:
        reasons.append('Many subdomains detected')
    
    if f['has_at']:
        reasons.append('Contains @ symbol (suspicious)')
    
    if f['suspicious_keyword']:
        reasons.append('Contains suspicious keywords (login/verify/etc.)')
    
    if f['url_length'] > 75:
        reasons.append('URL unusually long')
    
    if f['many_subdomains']:
        reasons.append('Multiple subdomains detected')
    
    if score >= 0.7:
        reasons.append('High ML confidence score indicates phishing')
    elif score >= 0.5:
        reasons.append('Moderate risk detected by ML model')
    
    return reasons if reasons else ['URL appears legitimate']

def ml_score(url):
    """Return ML-based score and reasons"""
    ml_result = ml_predict(url)
    
    if ml_result is not None:
        score, prediction = ml_result
        reasons = get_reasons(url, score)
        return round(score, 3), reasons
    else:
        # Fallback to heuristic
        return heuristic_score(url)

def heuristic_score(url):
    """Fallback heuristic scoring method"""
    f = extract_features(url)
    score = 0.0
    reasons = []

    if f['has_ip']:
        score += 0.25
        reasons.append('URL uses an IP address as host')

    if not f['has_https_scheme']:
        score += 0.15
        reasons.append('No HTTPS scheme')

    if f['num_dots'] >= 4:
        score += 0.12
        reasons.append('Many subdomains/labels')

    if f['has_at']:
        score += 0.18
        reasons.append('Contains @ symbol')

    if f['suspicious_keyword']:
        score += 0.15
        reasons.append('Contains suspicious keyword (login/verify/etc.)')

    if f['url_length'] > 75:
        score += 0.10
        reasons.append('URL unusually long')

    # clamp score
    if score > 1.0:
        score = 1.0

    return round(score, 3), reasons if reasons else ['URL appears legitimate']

