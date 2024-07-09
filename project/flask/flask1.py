#!/usr/bin/env Python3


from flask import Flask



app = Flask(__name__)


def openAIcall(prompt, user_input):
    # OpenAI API
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": user_input}
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

        global key_list
        key_list = message.split('"')  # Split into words (need to figure out how to split it into )
        key_list = [item for item in key_list if item]  # Remove empty strings

        # Append outputs to a file
        with open(f'./{file_out}', 'a') as f:
            for item in key_list:
                f.write(f"{item}")
        print(f"Written {user_input} to {file_out}")
        return message
    except Exception as e:
        print(f"An error occurred: {e}")



#decorator


app.add_url_rule("/openai", openAIcall)

@app.route("/")
def hello_world():
    return "Hello World"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
