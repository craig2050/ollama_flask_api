#!/usr/bin/env python3
import requests
import json
import sys
import time

# Configuration
API_URL = "http://localhost:5005"
STATUS_ENDPOINT = f"{API_URL}/status"
CHAT_ENDPOINT = f"{API_URL}/chat"

def test_status():
    """Test the status endpoint."""
    print("Testing /status endpoint...")
    try:
        response = requests.get(STATUS_ENDPOINT)
        if response.status_code == 200:
            print("✅ Status endpoint is working!")
            print(f"Response: {response.json()}")
            return True
        else:
            print(f"❌ Status endpoint returned code {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Connection error! Is the Flask API running?")
        return False

def test_chat(prompt="Hello, how are you today?"):
    """Test the chat endpoint with a sample prompt."""
    print(f"\nTesting /chat endpoint with prompt: '{prompt}'")
    payload = {"prompt": prompt}
    
    try:
        response = requests.post(CHAT_ENDPOINT, json=payload)
        if response.status_code == 200:
            result = response.json()
            print("✅ Chat endpoint is working!")
            
            # Access the response from the updated API format
            llm_response = result.get("response", "")
            if llm_response:
                print(f"Response from LLM: {llm_response}")
                return True
            else:
                print("⚠️ Chat endpoint returned a successful status code but no response from the LLM.")
                return False
        else:
            print(f"❌ Chat endpoint returned code {response.status_code}")
            print(f"Error message: {response.text}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Connection error! Is the Flask API running?")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")
        return False

def main():
    """Run all tests."""
    print("🚀 Starting API tests...\n")
    
    # Test status endpoint
    status_ok = test_status()
    
    # Abort if status check fails
    if not status_ok:
        print("\n❌ Status check failed. Please make sure the API is running.")
        sys.exit(1)
    
    # Wait a moment
    time.sleep(1)
    
    # Test chat endpoint
    chat_prompt = "Explain what the Flask framework is in one sentence."
    chat_ok = test_chat(chat_prompt)
    
    # Report summary
    print("\n📊 Test Summary:")
    print(f"Status endpoint: {'✅ PASS' if status_ok else '❌ FAIL'}")
    print(f"Chat endpoint: {'✅ PASS' if chat_ok else '❌ FAIL'}")
    
    if status_ok and chat_ok:
        print("\n✨ All tests passed! Your Ollama Flask API is working correctly.")
    else:
        print("\n⚠️ Some tests failed. Please check the logs above.")

if __name__ == "__main__":
    main()
