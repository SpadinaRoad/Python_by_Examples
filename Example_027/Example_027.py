#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_027
# $ python3 Example_027.py
# $ python3 Example_027.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

027
Ask the user to enter a
number with lots of
decimal places. Multiply
this number by two and
display the answer.

"""

print(__doc__)

num = ''
while num != 'x' : 
    num = input('Enter a number with lots of decimals places: ')
    if num != 'x' : 
        num = float(num)
        print(f'The input for a number : {num}.')
        num = num * 2
        print(f'Multiplied by two : {num}.')
        
