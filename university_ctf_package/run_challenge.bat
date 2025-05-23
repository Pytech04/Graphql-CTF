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
