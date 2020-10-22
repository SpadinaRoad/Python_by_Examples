#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_007
# $ python3 Example_007.py
# $ python3 Example_007.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

007
Ask the user for their name and their age. Add 1 to their age
and display the output [Name] next birthday you
will be [new age] .

"""

print(__doc__)
name = input('Please enter your name : ')
age = input('How old are you : ')
next_age = int(age) + 1
print('')
print(f'{name}, on your next birthday, you will be {next_age} years old.')
