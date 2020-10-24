#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_039
# $ python3 Example_039.py
# $ python3 Example_039.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

039
Ask the user to enter a number between 1
and 12 and then display the times table for
that number.

"""

print(__doc__)

num = ''
while num != 'x' : 

    num = input('Enter a number between 1 and 12 : ')
    print()
    print(f'The input for a number : {num}.')
    
    if num != 'x' : 
        num = int(num)
        for i in range(1, 13) :
            print(f'{i} x {num} = {i * num}')
            print()
