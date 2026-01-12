import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError(
        "❌ GROQ_API_KEY not found! Please set it in .env file\n"
        "Get your free key from: https://console.groq.com/keys"
    )

GROQ_MODEL = "llama-3.3-70b-versatile"  # Fast and powerful free model

API_CONFIG = {
    "api_key": GROQ_API_KEY,
    "model": GROQ_MODEL,
    "temperature": 0.7,  # Balanced creativity and consistency
    "max_tokens": 2048,  # Enough for detailed output
}
