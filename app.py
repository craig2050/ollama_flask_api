from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Ollama local API
OLLAMA_API = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:3b"  # Change this to any other downloaded model

@app.route("/status", methods=["GET"])
def status():
    """Check if the API is running."""
    return jsonify({"message": "Ollama API is running!"})

@app.route("/chat", methods=["POST"])
def chat():
    """Send a prompt to the Ollama model and return the response."""
    data = request.json
    prompt = data.get("prompt", "").strip()

    if not prompt:
        return jsonify({"error": "Prompt cannot be empty"}), 400

    ollama_request = {"model": MODEL_NAME, "prompt": prompt, "stream": False}
    
    try:
        response = requests.post(OLLAMA_API, json=ollama_request)
        
        if response.status_code != 200:
            return jsonify({"error": f"Ollama API returned status code {response.status_code}"}), 500
        
        # Parse the JSON response from Ollama
        try:
            result = response.json()
            return jsonify({"response": result.get("response", "No response from model")})
        except Exception as e:
            return jsonify({"error": f"Failed to parse Ollama response: {str(e)}"}), 500
            
    except requests.RequestException as e:
        return jsonify({"error": f"Failed to connect to Ollama: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005, debug=True)
