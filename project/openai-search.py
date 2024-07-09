#!/usr/bin/env python3
from openai import OpenAI
from dotenv import load_dotenv
import os

#THIS PROGRAM TAKES INPUT FILE AND THEN OUTPUTS IT deifning each object

#SETUP
# Load environment variables from .env file
load_dotenv()

# Get API key from environment variables
api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)
prompt = "Break down each JSON object, look up and give me detailed history on each object"
# Check if the API key is loaded
if not api_key:
    raise ValueError("API key not found. Make sure you have an OPENAI_API_KEY in your .env file.")
# Set the API key for OpenAI



#BEGIN


def openAIcall(prompt, file_content):
     # OpenAI API
    try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": file_content}
                ]
            )

            # Extract the message content
            message = response.choices[0].message.content
            return message
            print(message)

    except Exception as e:
        print(f"An error occured: {e}")


#end of OpenAI call
#This crates a list from the returned OPEN AI message


def main():
    #define file in and out
    file_in = input(f"Specify file input name:" '\n')
    file_out = input(f"Specify file output name:" '\n')

    try:
        #open both read and write files and define their object
        with open(file_in, 'r') as fileread, open(file_out, 'a') as filewrite:
            file_content = fileread.read()
#call OpenAI with file content
            response = openAIcall(prompt, file_content.strip())
            if response:
                #print response
                print(f"{response}" '\n')
                #write response to file
                filewrite.write(response + '\n')


                #ERRROR HANDLING
    except FileNotFoundError:
        print(f"File not found: {file_in}")
    except MessegeError as e:
        print(f"An error occured while processing: {e}")

if __name__ == "__main__":
    main()  # Run the main function
        
