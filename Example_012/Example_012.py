#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_012
# $ python3 Example_012.py
# $ python3 Example_012.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

012
Ask for two numbers. If
the first one is larger
than the second, display
the second number first
and then the first
number, otherwise show
the first number first and
then the second.

"""

print(__doc__)
num_1 = int(input('Enter a number : '))
num_2 = int(input('Enter a number : '))
print()

if num_1 > num_2 :
    print(f'The second number is : {num_2}.')
    print(f'The fist number is   : {num_1}.')
else :
    print(f'The fist number is   : {num_1}.')
    print(f'The second number is : {num_2}.')

