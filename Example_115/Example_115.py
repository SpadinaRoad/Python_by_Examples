#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_115
# $ python3 Example_115.py
# $ python3 Example_115.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

115
Using the Books.csv file, display the data in
the file along with the row number of each.

"""

import csv

print(__doc__)

filename = "Books.csv"
with open(filename, 'r') as fo:
    reader = csv.reader(fo, delimiter=',')
    line_num = 0
    for line in reader :
        if line[0] != 'Book' :
            line_num += 1
            print(f'Line number: {line_num}. Content {line}')
print()

