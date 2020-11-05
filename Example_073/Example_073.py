#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_073
# $ python3 Example_073.py
# $ python3 Example_073.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

073
Ask the user to
enter four of their
favourite foods
and store them in
a dictionary so
that they are
indexed with
numbers starting
from 1. Display
the dictionary in
full, showing the
index number
and the item. Ask
them which they
want to get rid of
and remove it
from the list. Sort
the remaining
data and display
the dictionary.

"""

print(__doc__)

food_dict = dict()
for i in range(1, 5) : 
    food_choice = input('Enter a favourite food: ')
    food_dict[i] = food_choice
    print()
    print(f'Input for food : {food_choice}')
    
print()
print(f'Here is the dictionary: {food_dict}')
to_remove = int(input('What item do you want to remove? Enter the number: '))
print(f'Input for number to remove: {to_remove}')
print()
del food_dict[to_remove]
print(sorted(food_dict.values()))
