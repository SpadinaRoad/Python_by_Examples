#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_106
# $ python3 Example_106.py
# $ python3 Example_106.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

106
Create a new file called “Names.txt”. Add five names to the
document, which are stored on separate lines. Once you have
run the program, look in the location where your program is
stored and check that the file has been created properly.
    
"""

print(__doc__)

names = ['Bruce', 'Allen', 'James', 'Angus', 'William']

with open('Names.txt', 'w') as fo :
    for i in range(5) :
        fo.write(f'{names[i]}\n')


    
    
