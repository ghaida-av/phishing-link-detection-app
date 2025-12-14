from urllib.parse import urlparse

# Simple keyword list (basic phishing indicators)
PHISHING_KEYWORDS = [
    "login", "verify", "bank", "secure",
    "update", "account", "password", "signin"
]

def check_url(url):
    parsed = urlparse(url)
    full_url = url.lower()

    # Rule 1: suspicious keywords
    for word in PHISHING_KEYWORDS:
        if word in full_url:
            return "Phishing link ❌"

    # Rule 2: too many subdomains
    if parsed.netloc.count('.') > 3:
        return "Phishing link ❌"

    # Rule 3: no HTTPS
    if parsed.scheme != "https":
        return "Phishing link ❌"

    return "Safe ✅"





