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
    echo "Installing dependencies..."
    python3 -m pip install -r requirements.txt
    echo "Starting challenge server..."
    python3 main.py
fi

echo ""
echo "🎯 Challenge should now be running at: http://localhost:5000"
echo "📖 Visit /graphql for the GraphQL interface"
echo "🏆 Find the flag by exploiting the IDOR vulnerability!"
