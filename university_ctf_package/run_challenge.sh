#!/bin/bash
echo "🚀 Starting GraphQL IDOR CTF Challenge..."
echo "📚 Perfect for cybersecurity education!"
echo ""

if command -v docker &> /dev/null; then
    echo "Using Docker (recommended)..."
    docker build -t university-ctf .
    docker run -p 5000:5000 university-ctf
else
    echo "Using Python directly..."
    python3 -m pip install -r requirements.txt
    python3 main.py
fi
