#!/usr/bin/env python3
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variables
api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)
# Check if the API key is loaded
if not api_key:
    raise ValueError("API key not found. Make sure you have an OPENAI_API_KEY in your .env file.")

# Set the API key for OpenAI

# Get input from the user
user_input = input("What are you looking for?\n")

# Define a system prompt (optional)
user_prompt = "Here:"

try:
    # Create the OpenAI client and request completion
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": user_prompt},
        {"role": "user", "content": user_input}
    ])

    # Extract the message content
    message = response.choices[0].message.content

    # Format the message
    formatted_message = message.strip()

    # Print the formatted message
    print("Formatted Response:")
    print(formatted_message)

except Exception as e:
    print(f"An error occurred: {e}")



#i want to call ansible playbook based off openai calls
    #def main()