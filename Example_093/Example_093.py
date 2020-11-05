#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_093
# $ python3 Example_093.py
# $ python3 Example_093.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

093
Ask the user to enter five
numbers. Sort them into order
and present them to the user.
Ask them to select one of the
numbers. Remove it from the
original array and save it in a
new array.

"""

from array import *
import random

print(__doc__)

array_user = array('i', [])

for i in range(5) : 
    a_num = int(input('Enter an integer: '))
    array_user.append(a_num)
    print(f'The input for a number: {a_num}')
    print()
    
print(type(array_user))
array_user = sorted(array_user)
print('Type after applying sorted function.')
print(type(array_user))

print(f'The numbers entered: ', end = '')
for i in range(5) :
    if i != 4 : 
        print(f'{array_user[i]}, ', end = '')
    else : 
        print(f'{array_user[i]}')
print()

selected_num = int(input('Enter a number from the list: '))    
print(f'The input for the number: {selected_num}')
print()
array_user.remove(selected_num)
array_selected = array('i', [selected_num])

print(f'The array as adjusted : {array_user}')
print(f'The selected array    : {list(array_selected)}')
print()

