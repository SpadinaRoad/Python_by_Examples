#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_102
# $ python3 Example_102.py
# $ python3 Example_102.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

102
Ask the user to enter the name, age and shoe size for four
people. Ask for the name of one of the people in the list and
display their age and shoe size.
    
"""

print(__doc__)

the_dict = {}

for i in range(4) :
    name = input('Enter a name : ')
    print(f'The input for a name : {name}')
    age = input('Enter an age : ')
    print(f'The input for an age : {age}')
    shoe_size = input('Enter a shoe size : ')
    print(f'The input for a shoe size : {shoe_size}')
    print()
    the_dict[name] = {'age' : age, 'size' : shoe_size}
    
print('The list of data: ')
for i in the_dict :
    print(f'{i} : {the_dict[i]}')
    
choice = input('Enter a name from the list: ')
print(f'The input for a name {choice}')
print(f'The person\'s age       : {the_dict[choice]["age"]} ')
print(f'The perons\'s shoe size : {the_dict[choice]["size"]}')
print()

