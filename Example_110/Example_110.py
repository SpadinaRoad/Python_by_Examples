#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_110
# $ python3 Example_110.py
# $ python3 Example_110.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

110
Using the Names.txt file you
created earlier, display the list of
names in Python. Ask the user to
type in one of the names and then
save all the names except the one
they entered into a new file called
Names2.txt.

"""

print(__doc__)

filename = 'Names.txt'
filename2 = 'Names2.txt'

file_line = []
with open(filename, 'r') as fo :
    for i in fo :
        file_line.append(i)
print(file_line)    

name_to_delete = input('Enter a name to delete : ')    
print(f'The input for a {name_to_delete}')
print()

name_to_delete += '\n'
with open(filename2, 'w') as fo : 
    for i in file_line :
        if i != name_to_delete : 
            print(i)
            fo.write(i)
        

