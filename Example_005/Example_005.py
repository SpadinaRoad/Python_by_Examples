#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_005
# $ python3 Example_005.py
# $ python3 Example_005.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

005
Ask the user to enter three
numbers. Add together the first
two numbers and then multiply
this total by the third. Display the
answer as The answer is
[answer].

"""

print(__doc__)
num_1 = input('Enter a number : ')
num_2 = input('Enter a number : ')
num_3 = input('Enter a number : ')
answer = (int(num_1) + int(num_2)) * int(num_3)
print('')
print(f'The first number is  : {num_1}')
print(f'The second number is : {num_2}')
print(f'The third number is  : {num_3}')
print(f'The answer is {answer}')
