#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_107
# $ python3 Example_107.py
# $ python3 Example_107.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

107
Open the
Names.txt
file and
display
the data
in Python.
    
"""

print(__doc__)

reader = []
with open('Names.txt', 'r') as fo :
    reader.append(fo.read())

for i in reader :
    print(i)
    
    
