#!/usr/bin/env python3
from openai import OpenAI
from dotenv import load_dotenv
import os 
import sys

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
user_prompt = "return list only, seperated by commas"

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
    #print("Formatted Response:")
    #thprint(formatted_message)
  

except Exception as e:
    print(f"An error occurred: {e}")

#i need to strip the numbers and commons out of the list for  formatting up above

key_list = []
key_list = formatted_message.split()
key_list = [item for item in key_list if item]

print(key_list)




#these are strips of code i dont know what im doing with yet


#this outputs to a file 'output.txt' that not functioning yet, i think i need echo?
"""sys.stdout = open('output.txt', 'wt')
print(crypto_list)"""

#I want to now define values based off the AI call and then create a 
# main() loop to do stuff, not sure what yet.... but atleast i have valuves in a list
#maybe create another API call from each item in the list and create a dictionary


"""def main()
    while len(crypto_list) < 10:
        try:
            

            
        except ValueError:
            print('Enter a valid integer')
            continue"""


#create a dictionary and assign the definitions into each value from GPT prompt

selected_key = input(f"Select and item and display defintion: '\n' {key_list}" '\n')

selected_key = key_list[1] #not sure how to call the list items yet, this only chooses positon one
print(f'{selected_key}')