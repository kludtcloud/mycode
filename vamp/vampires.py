#!/bin/usr/env  Python3


infile = open("dracula.txt","r")

infile = infile.readlines()
count = 0
with open ("vamptime.txt", "a") as times:
    for line in infile:
        if "vampire" in line.lower():
            count += 1
            print(line)
            times.write(line)
            
print(count)