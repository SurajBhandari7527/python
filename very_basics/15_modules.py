''' here covered three modules......> math, os, random,time'''

import math           #THIS MODULE IS USED TO CALCULATE DIFFERENT MATHEMATICAL CALCULATIONS
print(math.pi)                 #output: pi
print(math.sqrt(625))          # Output: 25.0
print(math.ceil(4.3))          # Output: 5
print(math.floor(4.7))         # Output: 4
print(math.factorial(5))       # Output: 120
ratio = math.sqrt(3)
print(math.asin(ratio/2))   # Output: 1.0471975511965976 (approximately)
print(math.acos(0.5))       # Output: 1.0471975511965979 (approximately)
print(math.atan(1))         # Output: 0.7853981633974483 (approximately)
print(math.atan2(1, math.sqrt(3)),'\n')  # Output: 0.5235987755982989 (approximately

x = 1
print(math.erf(x))    # Output: 0.8427007929497148
print(math.erfc(x))   # Output: 0.15729920705028513
print(math.gamma(x))  # Output: 1.0

print('\n')


import random           #THIS MODULE IS USED TO GENERATE RANDOM THINGS
print(random.randint(1,100))
other_list=[1,2,3,4,5]
random.shuffle(other_list)  #while doing this first of all shuffle and print otherwise it will print none(that means it was shuffled)
print(other_list)


import time #This module uses the actual time and other things
print(time.time()) # this is printing the actual time of now in many numbers
'''
The time.time() function in Python returns the current time in seconds since the epoch. 
The epoch is defined as the point in time where the time starts, and it varies based on
 the platform but is typically January 1, 1970, 00:00:00 (UTC) for Unix-like systems.'''

print(time.ctime()) # this prints the current time of now

print("Hello")
time.sleep(10)       #this will pause the program for 2 seconds. first hello prints and after 2 seconds of pause brother prints
print("Brother")    

import os
print(os.getcwd())  #this will print the current directory location where we are coding cwd=current working directory
print('\n yes bro')
print(os.listdir())     #this will list all the directories that are present of the same directory where we are working
print('\n yes bro again')