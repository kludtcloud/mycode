#!/usr/bin/env python3

#i need to store this key securely
import time

print("Welcome, please wait while we load Paradisia, the next gen alternate reality.") 
time.sleep(1)
print("...")
time.sleep(1)
print("......")
print("Elysium: Loading up the backend. Okay don't laugh, its a real thing.")
time.sleep(1)
print(".........")
time.sleep(1)
print("Elysium: It's a big file, just give me a sec")
time.sleep(1)
print("............")
time.sleep(1)
print("Elysium: Okay were ready")

import threading

def input_with_timeout(prompt, timeout=10):
    # A container to store the user's input
    user_input = [None]


    def get_input():
        user_input[0] = input(prompt)

    # Create a thread to get user input
    input_thread = threading.Thread(target=get_input)
    input_thread.start()

    # Wait for the specified timeout
    input_thread.join(timeout)

    if input_thread.is_alive():
        # If the input_thread is still running, it means no input was given
        print("Elysium: I don't have all day. I am a pretty busy AI")
        time.sleep(3)
        print("Elysium: Seriously?")
        time.sleep(3)
        print("Elysium: This is what were gonna do then?")
   #I want to start calling from a list of insults in a file at this point.Maybe call them from LLM
   # Then generate and display them every 3 seconds.     


        input_thread.join()  # Clean up the thread
    else:
        # Return the user's input
        return user_input[0]

# Usage
user_input = input_with_timeout("Please enter your name: " '\n')

# Since the function only returns if input is given within the timeout,
# we need to handle the case when no input is provided.
if user_input is not None:
    print(f"Welcome: {user_input}")
#Something is wrong here, if you wait to the timeout prompts it 'wont' print the welcome message

print("Elysium: Asking your name was only a formality, I alreay knew this. My creator has asked me to be more relatable.")