#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_038
# $ python3 Example_038.py
# $ python3 Example_038.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

038
Change program
037 to also ask for a
number. Display
their name (one
letter at a time on
each line) and
repeat this for the
number of times
they entered.

"""

print(__doc__)

name = ''
while name != 'x' : 

    name = input('Enter your name : ')
    
    print()
    print(f'The input for your name : {name}.')
    
    if name != 'x' : 
        num = int(input('Enter a number : '))
        print()
        print(f'The input for a number : {num}.')
        for i in range(num) :
            for c in name :
                print(c)
            print()
