import openai

# Set your OpenAI API key
openai.api_key = 'YOUR_API_KEY'

def get_openai_response(prompt):
    try:
        # Call the OpenAI API with your prompt
        response = openai.Completion.create(
            engine="davinci-codex",   # You can replace this with other available engines like 'text-davinci-003'
            prompt=prompt,
            max_tokens=150,           # Adjust the number of tokens as needed
            n=1,                      # Number of completions
            stop=None,                # Change based on if you want specific stopping sequences
            temperature=0.7           # Adjust the randomness and creativity
        )

        # Extract and return the generated text
        return response.choices[0].text.strip()
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage
prompt = "Once upon a time in a land far, far away"
response = get_openai_response(prompt)
print(response)


#steps to Integrate OpenAI:
#Sign Up and Get API Key:
#Sign up at OpenAI and obtain an API key from your API settings.
#Install OpenAI Python Client Library:
#If you haven't already, you can install the OpenAI Python client library using pip:
#pip install openai
#Use the OpenAI API in Your Code:


#Key Details:
#API Key: Replace 'YOUR_API_KEY' with the API key you obtained from OpenAI.
#Engine: Various engines are available like davinci-codex, text-davinci-003, etc. Choose according to your use case.
#Parameters:
#prompt: Your initial text input to the model.
#max_tokens: The maximum number of tokens (words or parts of words) to generate.
#n: The number of responses to generate.
#stop: Specify any stopping sequences if needed.
#temperature: Controls randomness. Lower values make the output more deterministic.
#Additional Tips:
#Handling Sensitive Data: Never hardcode API keys in your code. Consider using environment variables or secure key management services.
#Error Handling: Enhance error handling to manage API rate limits, network issues, or other potential errors.
#Documentation: Refer to the OpenAI API documentation for more details and advanced configurations.
#This example will get you set up and running with basic text generation using OpenAI's API in Python. You can explore more features and models as needed for your specific application.