#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_036
# $ python3 Example_036.py
# $ python3 Example_036.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

036
Alter program 035 so that it will ask the user to enter their
name and a number and then display their name that
number of times.

"""

print(__doc__)

from math import pi

name = ''
while name != 'x' : 

    name = input('Enter your name : ')
    
    print()
    print(f'The input for your name : {name}.')
    
    if name != 'x' : 
        num = int(input('How many times to display your name : '))
        print()
        print(f'The input for number : {num}.')
        print(name * num)
        print()
