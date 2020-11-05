#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_108
# $ python3 Example_108.py
# $ python3 Example_108.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

108
Open the Names.txt file. Ask the user to input a
new name. Add this to the end of the file and
display the entire file.
    
"""

print(__doc__)

name_to_add = input('Enter a name: ')
print(f'The input for name: {name_to_add}')
print()

with open("Names.txt", 'a') as fo :
    fo.write(f'{name_to_add}\n')

reader = []
with open('Names.txt', 'r') as fo :
    reader.append(fo.read())

for i in reader :
    print(i)
    
    
