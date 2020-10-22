#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_004
# $ python3 Example_004.py
# $ python3 Example_004.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

004
Ask the user to enter
two numbers. Add
them together and
display the answer as
The total is [answer]
"""

print(__doc__)
num_1 = input('Enter a number : ')
num_2 = input('Enter a number : ')
answer = int(num_1) + int(num_2)
print('')
print(f'The first number is  : {num_1}')
print(f'The second number is : {num_2}')
print(f'The answer is {answer}')
