#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_028
# $ python3 Example_028.py
# $ python3 Example_028.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

028
Update program 027 so that it will display the answer to
two decimal places.

"""

print(__doc__)

num = ''
while num != 'x' : 
    num = input('Enter a number with lots of decimals places: ')
    if num != 'x' : 
        num = float(num)
        print(f'The input for a number : {num}.')
        num = num * 2
        print(f'Multiplied by two : {num:.2f}.')
        
