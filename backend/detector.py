import re
from urllib.parse import urlparse

SUSPICIOUS_KEYWORDS = [
    'login', 'secure', 'account', 'update', 'verify', 'bank', 'confirm',
    'webscr', 'signin', 'password', 'ebay', 'paypal', 'appleid', 'confirm'
]

def has_ip_address(netloc):
    # checks if netloc is an IP (v4)
    return re.match(r'^\d{1,3}(\.\d{1,3}){3}$', netloc) is not None

def count_dots(s):
    return s.count('.')

def long_url(url, threshold=75):
    return len(url) > threshold

def suspicious_words_in_path(path):
    path = path.lower()
    return any(word in path for word in SUSPICIOUS_KEYWORDS)

def uses_at_symbol(url):
    return '@' in url

def suspicious_subdomain(netloc):
    # many-labeled subdomains (e.g., very.long.sub.domain.example.com)
    parts = netloc.split('.')
    return len(parts) > 4

def has_ip_as_host(url):
    try:
        netloc = urlparse(url).netloc.split(':')[0]
        return has_ip_address(netloc)
    except:
        return False

def extract_features(url):
    parsed = urlparse(url)
    netloc = parsed.netloc.lower()
    path = parsed.path or ''
    query = parsed.query or ''

    features = {
        'url_length': len(url),
        'has_ip': has_ip_as_host(url),
        'num_dots': count_dots(netloc),
        'has_at': uses_at_symbol(url),
        'suspicious_keyword': suspicious_words_in_path(path + query + netloc),
        'many_subdomains': suspicious_subdomain(netloc),
        'has_https_scheme': parsed.scheme.lower() == 'https',
    }
    return features

def heuristic_score(url):
    """Return a score between 0 and 1 (higher = more suspicious) and reasons."""
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

    return round(score, 3), reasons

