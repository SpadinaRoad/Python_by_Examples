#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_088
# $ python3 Example_088.py
# $ python3 Example_088.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

088
Ask the user for a list of five
integers. Store them in an array.
Sort the list and display it in
reverse order.

"""

from array import *

print(__doc__)

int_array = array('i', [])

for i in range(5) :
    a_num = int(input('Enter an integer: '))
    print(f'The input for an integer: {a_num}')
    print()
    int_array.append(a_num)
    
int_array = sorted(int_array)
int_array.reverse()
print(f'The list of integers: {int_array}')
