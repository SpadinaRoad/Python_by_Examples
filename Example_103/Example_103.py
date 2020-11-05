#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_103
# $ python3 Example_103.py
# $ python3 Example_103.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

103
Adapt program 102
to display the
names and ages of
all the people in
the list but do not
show their shoe
size.
    
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
    print(f'{i} : age: {the_dict[i]["age"]} ')
    

