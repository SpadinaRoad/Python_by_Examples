#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_022
# $ python3 Example_022.py
# $ python3 Example_022.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

022
Ask the user to enter their first name and surname in lower
case. Change the case to title case and join them together.
Display the finished result.

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
        fname = fname.title()
        lname = lname.title()
        print(f'Your full name : {fname} {lname}.')
        print()
    
