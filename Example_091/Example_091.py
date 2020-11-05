#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_091
# $ python3 Example_091.py
# $ python3 Example_091.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

091
Create an array which contains
five numbers (two of which
should be repeated). Display
the whole array to the user. Ask
the user to enter one of the
numbers from the array and
then display a message saying
how many times that number
appears in the list.

"""

from array import *

print(__doc__)

int_array = array('i', [1, 2, 3, 3, 4])
print(f'Here is an array: {int_array}')

try_again = ''
while try_again != 'n' :

    a_num = int(input('Enter one of the numbers from the array: '))
    print(f'The input for a number: {a_num}')
    if try_again != 'n' :
        print(f'The number occurs {int_array.count(a_num)} times in the array.')
        try_again = input('Try again (y/n)? ')
        print()
        print()

