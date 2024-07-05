from openai import OpenAI
from dotenv import load_dotenv
import os


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
