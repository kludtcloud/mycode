#!/bin/usr/env Python3

#99 bottles of beer on the wall!
 #   99 bottles of beer on the wall! 99 bottles of beer! You take one down, pass it around!
  #  98 bottles of beer on the wall!
   ##97 bottles of beer on the wall!
    #97 bottles of beer on the wall! 97 bottles of beer! You take one down, pass it around!
    #[...and so on...]
wall = "bottles of beer on the wall!"
beer = " bottles of beer! "
take = "You take one down, pass it around!"
bottles = 99

if bottles != 0:
    for wall in range(98):
        bottles -= 1
        print(f"{bottles} bottles of beer on the wall! ", end='')
        print(f"{bottles}{beer}" , end='')
        print(f"{take}")
        if bottles == 1:
            print("Only one left!")
    else:
        print("No more bottles")    

