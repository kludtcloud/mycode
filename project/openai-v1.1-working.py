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
user_prompt = "return list in JSON"

# Check if the API key is loaded
if not api_key:
    raise ValueError("API key not found. Make sure you have an OPENAI_API_KEY in your .env file.")

# Set the API key for OpenAI
print(f"Welcome to the show, a few functional and purpose notes:" '\n' 
"1: This program will call OpenAI LLM to generate a list of defintions for you" '\n'
 "2: These answers will output to a text file." '\n'
 "3: On exit the program and it will encrypt and hash your answers.(pending)" '\n')



def main():
    while True:
        user_input = input("At any time you may reset the program at this prompt" '\n' "'reset' to" '\n' "'exit' to quit" '\n' "'yes' to contuine" '\n').strip().lower()
        if user_input == "yes":
            user_input2 = input("What are you looking for?\n")
            openAIcall(user_prompt, user_input2)
            continue
        if user_input == "reset":
            print("Resetting the program...")
            continue  # Restart the loop, effectively resetting the program
        
        if user_input == "exit":
            print("Exiting.")
            reset_input = input("Do you want to exit the program? (yes/no): ").strip().lower()
            if reset_input != "no":
                    print("Exiting the program...")
            #break  # Exit the outer loop and end the program
        break  # Exit the loop and end the program
        
        # Proceed if not reset or exit
        #user_input2 = input("What are you looking for?\n")
        #user_prompt = "return list in JSON"



def openAIcall(prompt, user_input2):
     # OpenAI API
    try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": user_prompt},
                    {"role": "user", "content": user_input2}
                ]
            )

            # Extract the message content
            message = response.choices[0].message.content

            # Format the message
            formatted_message = message.strip()
            reformat = '}{[],"'
            for char in reformat:
                formatted_message = formatted_message.replace(char, "")
            print(formatted_message)

            key_list = message#.split('"')  # Split into words (need to figure out how to split it into )
            key_list = [item for item in key_list if item]  # Remove empty strings

            #this appends outputs to a file 'output.txt'
            with open('output.txt', 'a') as f:
                for item in key_list:
                    f.write(f"{item}")
            print(f"Written {user_input2} to {f}")
            # print(key_list)
           # print(f"You typed: {user_input2}")

    except Exception as e:
        print(f"An error occured: {e}")

#end of OpenAI call
#This crates a list from the returned OPEN AI message




"""#I may create a dictionary instead of a list
#I need to strip the numbers and commons out of the list for  formatting up above"""


if __name__ == "__main__":
    main()  # Run the main function
        









#these are strips of code i dont know what im doing with yet
#thoughts, not sure if i want to impletment this yet.

#I want to now define values based off the AI call and then create a 
# main() loop to do stuff, not sure what yet.... but atleast i have valuves in a list
#maybe create another API call from each item in the list and create a dictionary


#maybe ?select a key from dictonary and then display the defintions this is broken still
#selected_key = input(f"Select and item and display defintion: '\n' {key_list}" '\n')

#print_def = key_list[0].get(selected_key)
#print_key = key_list[selected_key] 
#not sure how to call the list items yet, this only chooses positon one
#print(f'{print_def}')

