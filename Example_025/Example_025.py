#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_025
# $ python3 Example_025.py
# $ python3 Example_025.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

025
Ask the user to enter their first name. If the length
of their first name is under five characters, ask
them to enter their surname and join them
together (without a space) and display the name
in upper case. If the length of the first name is five
or more characters, display their first name in
lower case.

"""

print(__doc__)

fname = ''
while fname != 'x' : 
    fname = input('Enter your first name: ')
    if fname != 'x' : 
        print(f'Input for first name : {fname}')
        print()
        if len(fname) < 5 :
            lname = input('Enter your last name: ')
            print(f'Input for last name : {lname}')
            print()
            combo = fname + lname
            combo = combo.upper()
            print(f'The names combined: {combo}.')
        else :
            print(f'You first name in lower case is {fname.lower()}.')
        print()
        
