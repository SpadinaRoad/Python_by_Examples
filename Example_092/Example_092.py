#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_092
# $ python3 Example_092.py
# $ python3 Example_092.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

092
Create two arrays (one
containing three numbers that
the user enters and one
containing a set of five random
numbers). Join these two arrays
together into one large array.
Sort this large array and display
it so that each number appears
on a separate line.

"""

from array import *
import random

print(__doc__)

array_user = array('i', [])
array_comp = array('i', [])

for i in range(3) : 
    a_num = int(input('Enter a number : '))
    print(f'The input for a number : {a_num}')
    print()
    array_user.append(a_num)
    
for i in range(5) : 
    array_comp.append(random.randint(0,100))

print(f'The random numbers: {array_comp}')
print()

array_combo = array('i', [])
array_combo.extend(array_user)
array_combo.extend(array_comp)
array_combo = sorted(array_combo)

for i in array_combo : 
    print(i)
    
