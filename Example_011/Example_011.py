#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_011
# $ python3 Example_011.py
# $ python3 Example_011.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

011
Task the user to enter a number over 100 and then enter a number under
10 and tell them how many times the smaller number goes into the larger
number in a user-friendly format.

"""

print(__doc__)
num_1 = int(input('Enter a number greater than 100 : '))
num_2 = int(input('Enter a number less than 10: '))
answer = num_1 // num_2
print('')
print(f'The first number is  : {num_1}')
print(f'The second number is : {num_2}')
print(f'{num_2} goes into {num_1}: {answer} times.')
