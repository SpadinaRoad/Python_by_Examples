#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_104
# $ python3 Example_104.py
# $ python3 Example_104.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

104
After gathering the four names, ages and shoe sizes, ask the
user to enter the name of the person they want to remove from
the list. Delete this row from the data and display the other rows
on separate lines.
    
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
    print(f'{i} : {the_dict[i]} ')
print()

name = input('Enter a name to remove : ')
print(f'The input for name: {name}')
print()
del the_dict[name]

print('The list of data: ')
for i in the_dict :
    print(f'{i} : {the_dict[i]} ')
print()



