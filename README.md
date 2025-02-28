# 🚀 Ollama Local AI Chat API with Flask

This project sets up a **local AI chat API** using **Ollama** and **Flask**. The API allows you to interact with an **offline AI model** while keeping everything on your machine.

---

## 📌 Features
✅ **Runs AI models locally** (No cloud dependencies)  
✅ **Exposes a structured REST API**  
✅ **Handles requests & responses using Flask**  
✅ **Supports multi-device access over LAN**  
✅ **Includes automated install & start script**  

---

## 🛠 Installation & Setup

### **1️⃣ Install Dependencies**
Ensure you have **Python 3.x** installed.

For **Linux/macOS**:
```sh
curl -fsSL https://ollama.com/install.sh | sh
pip install flask
```

### **2️⃣ Run the Application**
For **Linux/macOS**:
```sh
./start.sh
```

For **Windows**:
```sh
start.bat
```

The API will be available at `http://localhost:5005`.

---

## 🔌 API Endpoints

### Status Check
- **URL**: `/status`
- **Method**: `GET`
- **Response**: 
  ```json
  {
    "message": "Ollama API is running!"
  }
  ```

### Chat with LLM
- **URL**: `/chat`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "prompt": "Your question or instruction here"
  }
  ```
- **Response**:
  ```json
  {
    "response": "The LLM's response will be here"
  }
  ```

---

## 🧩 Integrating with Other Applications

You can easily integrate this API into your own applications. Here are some examples:

### Python Example (using requests)

```python
import requests

def get_llm_response(prompt):
    api_url = "http://localhost:5005/chat"
    payload = {"prompt": prompt}
    
    try:
        response = requests.post(api_url, json=payload)
        response.raise_for_status()  # Raise exception for 4XX/5XX responses
        
        result = response.json()
        return result.get("response", "")
    except requests.exceptions.RequestException as e:
        print(f"Error communicating with LLM API: {e}")
        return None

# Example usage
user_message = "What are the main features of Python?"
ai_response = get_llm_response(user_message)
print(f"AI: {ai_response}")
```

### JavaScript/Node.js Example (using fetch)

```javascript
async function getLlmResponse(prompt) {
  const apiUrl = 'http://localhost:5005/chat';
  const payload = { prompt };
  
  try {
    const response = await fetch(apiUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(payload)
    });
    
    if (!response.ok) {
      throw new Error(`API error: ${response.status}`);
    }
    
    const data = await response.json();
    return data.response || '';
  } catch (error) {
    console.error('Error communicating with LLM API:', error);
    return null;
  }
}

// Example usage
async function handleUserMessage(userMessage) {
  const aiResponse = await getLlmResponse(userMessage);
  console.log(`AI: ${aiResponse}`);
  // Update your chat UI with the response
}
```

### React Frontend Example

```jsx
import { useState } from 'react';

function ChatComponent() {
  const [prompt, setPrompt] = useState('');
  const [response, setResponse] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true);
    
    try {
      const res = await fetch('http://localhost:5005/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ prompt })
      });
      
      const data = await res.json();
      setResponse(data.response || 'No response from AI');
    } catch (error) {
      console.error('Error:', error);
      setResponse('Error communicating with AI service');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="chat-container">
      <form onSubmit={handleSubmit}>
        <textarea 
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          placeholder="Type your message here..."
        />
        <button type="submit" disabled={isLoading}>
          {isLoading ? 'Sending...' : 'Send'}
        </button>
      </form>
      
      {response && (
        <div className="response">
          <h3>AI Response:</h3>
          <p>{response}</p>
        </div>
      )}
    </div>
  );
}
```

## 🔒 Production Considerations

When integrating this API into a production application, consider:

1. **API Security**: Add authentication if needed
2. **Error Handling**: Implement robust error handling
3. **Request Timeouts**: Set appropriate timeouts for LLM responses
4. **Rate Limiting**: Consider adding rate limiting for busy applications
5. **Networking**: Ensure network connectivity between your chat app and the API server

---

## 🔍 Testing

Use the included `test_endpoint.py` script to verify the API is working correctly:

```bash
python test_endpoint.py
```

This will test both the `/status` and `/chat` endpoints.
