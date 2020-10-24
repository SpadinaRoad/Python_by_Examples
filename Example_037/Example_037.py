#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_037
# $ python3 Example_037.py
# $ python3 Example_037.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

037
Ask the user to enter their name and display each letter in
their name on a separate line.

"""

print(__doc__)

name = ''
while name != 'x' : 

    name = input('Enter your name : ')
    
    print()
    print(f'The input for your name : {name}.')
    
    if name != 'x' : 
        for c in name :
            print(c)
        print()
