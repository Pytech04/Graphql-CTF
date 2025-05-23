#!/bin/bash
# University CTF Package Creator
# Creates a complete offline package for distribution

echo "🎓 Creating University CTF Package..."

# Create package directory
mkdir -p university_ctf_package
cd university_ctf_package

# Copy all necessary files
cp -r ../templates .
cp -r ../static .
cp ../app.py .
cp ../main.py .
cp ../models.py .
cp ../schema.py .
cp ../seed.py .
cp ../pyproject.toml .
cp ../uv.lock .
cp ../Dockerfile .
cp ../docker-compose.yml .
cp ../nginx.conf .
cp ../README_UNIVERSITY_DEPLOYMENT.md ./README.md

# Create data directory
mkdir -p data

# Create simple run script for students
cat > run_challenge.sh << 'EOF'
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
EOF

chmod +x run_challenge.sh

# Create Windows batch file
cat > run_challenge.bat << 'EOF'
@echo off
echo 🚀 Starting GraphQL IDOR CTF Challenge...
echo 📚 Perfect for cybersecurity education!
echo.

where docker >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    echo Using Docker (recommended)...
    docker build -t university-ctf .
    docker run -p 5000:5000 university-ctf
) else (
    echo Using Python directly...
    python -m pip install -r requirements.txt
    python main.py
)
pause
EOF

echo "✅ University package created in 'university_ctf_package/' directory"
echo "📦 Ready for distribution to students!"
echo ""
echo "Distribution options:"
echo "1. Zip the 'university_ctf_package' folder"
echo "2. Upload to your university's learning management system"
echo "3. Deploy on Cisco CTF platform"
echo "4. Share via Git repository"