
#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findLastBinary' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.

def findLastBinary(string):
    string1 = ''.join(format(ord(c), '08b') for c in string)

    num = 0
    max_num = int("1" * len(string1), 2)
    last_binary = None
    while num <= max_num:
        binary = bin(num)[2:]
        if binary in string1:
            first_index = string1.find(binary)
            string1 = string1[:first_index] + string1[first_index:].replace(binary, '', 1)
            last_index = string1.rfind(binary)
            string1 = string1[:last_index] + string1[last_index:].replace(binary, '', 1)
            last_binary = binary
            num += 1
        else:
            break
    if last_binary is not None:
        decimal = 0
        power = len(last_binary) - 1
        for digit in last_binary:
            decimal += int(digit) * 2 ** power
            power -= 1
        print (decimal)
    else:
        print ("0")


userstring = input("Please enter your string: ")
findLastBinary(userstring)