#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_020
# $ python3 Example_020.py
# $ python3 Example_020.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

020
Ask the user to enter
their first name and
then display the
length of their name.

"""

print(__doc__)

name = ''
while name != 'x' : 
    name = input('What is your name? ')
    if name != 'x' :
        print()
        print(f'Input for name     : {name}')
        print(f'Length of the name : {len(name)}')
        print()
    
