#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_041
# $ python3 Example_041.py
# $ python3 Example_041.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

041
Ask the user to enter their
name and a number. If the
number is less than 10, then
display their name that
number of times; otherwise
display the message “Too
high” three times.

"""

print(__doc__)

name = ''
while name != 'x' : 

    name = input('Enter your name : ')
    print()
    print(f'The input for a name : {name}.')
    print()
    
    if name != 'x' : 
        num = int(input('Enter a number : '))
        print()
        print(f'The input for a number : {num}.')
        print()
        if num < 10 : 
            for i in range(num) :
                print(f'{name}')
                print()
        else :
            for i in range(3) :
                print(f'Too high.')
                print()
        
