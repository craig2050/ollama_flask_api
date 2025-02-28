@echo off
setlocal

:: Step 1: Check if Ollama is installed
where ollama >nul 2>nul
if %errorlevel% neq 0 (
    echo ⚠️ Ollama is not installed. Installing...
    curl -fsSL https://ollama.com/install.sh | sh
) else (
    echo ✅ Ollama is already installed.
)

:: Step 2: Create and activate virtual environment
if not exist "venv" (
    echo 🚀 Creating virtual environment...
    python -m venv venv
)

echo ✅ Activating virtual environment...
call venv\Scripts\activate

:: Step 3: Install dependencies
echo 🚀 Installing dependencies...
pip install -r requirements.txt

:: Step 4: Start Ollama in the background
echo 🚀 Starting Ollama...
start /B ollama serve

:: Step 5: Wait a few seconds for Ollama to start
timeout /t 5 /nobreak >nul

:: Step 6: Start Flask API
echo 🚀 Starting Flask API...
python app.py
