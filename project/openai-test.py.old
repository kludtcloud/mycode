#env Python3, openai and dotenv
import openai
#import env and .env file
from dotenv import load_dotenv
import os
load_dotenv()

#call input from user: then yuse that for OpenAI message.
user_input = input("What are you looking for?" '\n')
user_prompt = "Here:"
from openai import OpenAI
api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI()

def response():
  completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": user_prompt},
    {"role": "user", "content": user_input}
  ]
)



print(completion.choices[0].message)

#dwarves = completion.choices[0].message

#print(f"Your request {dwarves}, are silly.")
