#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_040
# $ python3 Example_040.py
# $ python3 Example_040.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

040
Ask for a number below 50 and then count down from
50 to that number, making sure you show the number
they entered in the output.

"""

print(__doc__)

num = ''
while num != 'x' : 

    num = input('Enter a number below 50 : ')
    print()
    print(f'The input for a number : {num}.')
    
    if num != 'x' : 
        num = int(num)
        for i in range(50, num - 1, -1) :
            print(f'{i}')
            print()
