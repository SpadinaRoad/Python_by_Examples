#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_035
# $ python3 Example_035.py
# $ python3 Example_035.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

035
Ask the user to enter
their name and then
display their name
three times.

"""

print(__doc__)

name = ''
while name != 'x' : 

    name = input('Enter your name : ')
    
    print()
    print(f'The input for your name : {name}.')
    
    if name != 'x' : 
        print(name * 3)
        print()
        
