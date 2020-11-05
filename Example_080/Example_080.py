#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_080
# $ python3 Example_080.py
# $ python3 Example_080.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

080
Ask the user to enter their
first name and then display
the length of their first name.
Then ask for their surname
and display the length of
their surname. Join their first
name and surname together
with a space between and
display the result. Finally,
display the length of their full
name (including the space).

"""

print(__doc__)

fname = input('Enter your first name: ')
print(f'The input for first name : {fname}')
print(f'The length is {len(fname)}')
print()

lname = input('Enter your last name: ')
print(f'The input for last name: {lname}')
print(f'The length is {len(lname)}')
print()

full_name = fname + ' ' + lname
print(f'The full name: {full_name}')
print(f'The length is {len(full_name)}')
print()
