#!/bin/bash

echo " Setting up Phishing Link Detection App Backend..."

# Create virtual environment (Python 3.11)
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3.11 -m venv venv
fi

# Activate virtual environment
echo " Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo " Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo " Setup complete!"
echo ""
echo "To start the server, run:"
echo "  source venv/bin/activate"
echo "  python app.py"


