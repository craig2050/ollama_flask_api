#!/bin/bash

# Check if Ollama is installed
if ! command -v ollama &> /dev/null; then
    echo "⚠️ Ollama is not installed. Installing..."
    curl -fsSL https://ollama.com/install.sh | sh
else
    echo "✅ Ollama is already installed."
fi

# Create and activate virtual environment if not exists
if [ ! -d "venv" ]; then
    echo "🚀 Creating virtual environment..."
    python3 -m venv venv
fi

echo "✅ Activating virtual environment..."
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start Ollama in the background
echo "🚀 Starting Ollama..."
ollama serve &

# Wait for Ollama to fully start (optional delay)
sleep 5

# Run Flask API
echo "🚀 Starting Flask API..."
python app.py
