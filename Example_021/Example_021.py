#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_021
# $ python3 Example_021.py
# $ python3 Example_021.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

021
Ask the user to enter their first name and then ask them to
enter their surname. Join them together with a space between
and display the name and the length of whole name.

"""

print(__doc__)

fname = ''
while fname != 'x' : 
    fname = input('What is your first name? ')
    if fname != 'x' : 
        lname = input('What is your last name? ')
        print()
        print(f'Input for first name     : {fname}')
        print(f'Input for last name      : {lname}')
        print(f'Your full name : {fname} {lname}.')
        print()
    
