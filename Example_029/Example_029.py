#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_029
# $ python3 Example_029.py
# $ python3 Example_029.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

029
Ask the user to enter an integer that is over 500. Work
out the square root of that number and display it to two
decimal places.

"""

print(__doc__)

num = ''
while num != 'x' : 
    num = input('Enter an integer over 500 : ')
    if num != 'x' : 
        num = int(num)
        print(f'The input for a number : {num}.')
        num = num ** (1/2)
        print(f'The square root is : {num:.2f}.')
        
