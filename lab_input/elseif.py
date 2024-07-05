#!/usr/bin/env Python3

lenght_int = ""
target_lenght = 256

user_input = input("Generate key, enter characters:" '\n')
lenght_int += user_input


if: len(lenght_int) > target_length
    lenght_int = lenght_string[:target_length]
    print("Key generated")
    print(f"Key: {lenght_int}")
else:
    while len(lenght_int) < target_lenght:
        user_input = input("Keep going:" '\n').strip()
        lenght_int += user_input
        if len(lenght_int) > target_lenght:
            lenght_int = lenght_int[:target_lenght]
            break

print("Key generated" '\n')
print(f"Key: {lenght_int}")

