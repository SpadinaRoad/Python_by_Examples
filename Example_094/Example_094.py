#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_094
# $ python3 Example_094.py
# $ python3 Example_094.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

094
Display an array of five
numbers. Ask the user to
select one of the numbers.
Once they have selected a
number, display the
position of that item in the
array. If they enter
something that is not in
the array, ask them to try
again until they select a
relevant item.

"""

from array import *
import random

print(__doc__)

array_rand = array('i', [])
for i in range(5) :
    array_rand.append(random.randint(0, 10))
    
print(f'List to choose from : {list(array_rand)}')
print()

index_found = False
while index_found != True :

    selected_num = int(input('Select a number from the list: '))
    print(f'The input for a selected number: {selected_num}')
    print()

    if selected_num in array_rand : 
        index_found = True
        print(f'The selected number is at index: {array_rand.index(selected_num)}')
        print()
    else :
        print('You\'re selection is not in the list.')
        print('Try another selection.')
