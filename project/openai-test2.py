#env Python3, openai and dotenv
#!/usr/bin/env python3
import openai
#import env and .env file
from dotenv import load_dotenv
import os
load_dotenv()

from openai import OpenAI
api_key = os.getenv('OPEN_API_KEY')

client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "Help me test"},
    {"role": "user", "content": "Please indicate me API test is working"}
  ]
)

print(completion.choices[0].message)