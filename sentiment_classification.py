from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Get the API key
api_key = os.getenv("OPENAI_API_KEY")

# Debugging: Print a message if key isn't found
if api_key:
    print(f"API Key found")
else:
    print("API Key not found!")
