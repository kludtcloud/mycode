#!/bin/usr/env  Python3


with open("dracula.txt","r") as infile:
    infile = infile.readlines()
    count = 0
    with open ("vamptime.txt", "a") as times:
        for line in infile:
            if "vampire" in line.lower():
                count += 1
                print(line)
                times.write(line + "\n")
            
print(count)