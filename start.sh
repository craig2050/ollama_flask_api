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

# Display API information and usage instructions
echo ""
echo "📡 ============================================================="
echo "📡 API ENDPOINT INFORMATION"
echo "📡 ============================================================="
echo ""
echo "🔗 Local API will be available at: http://localhost:5005"
echo ""
echo "📌 Available Endpoints:"
echo "   - GET  /status : Check if API is running"
echo "   - POST /chat   : Send prompts to the LLM"
echo ""
echo "📝 Example curl command:"
echo "   curl -X POST http://localhost:5005/chat -H \"Content-Type: application/json\" -d '{\"prompt\":\"Tell me about Flask\"}'"
echo ""
echo "🚀 For more detailed documentation, see the README.md file."
echo "📡 ============================================================="
echo ""

# Run Flask API
echo "🚀 Starting Flask API..."
python app.py
