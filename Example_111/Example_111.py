#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_111
# $ python3 Example_111.py
# $ python3 Example_111.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

111
Create a .csv file that will store the following data. Call it “Books.csv”.

"""

import csv

print(__doc__)

filename = 'Books.csv'

with open(filename, 'r') as fo :
    for row in fo : 
        print(row)
        

