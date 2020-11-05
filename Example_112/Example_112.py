#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_112
# $ python3 Example_112.py
# $ python3 Example_112.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

112
Using the Books.csv file
from program 111, ask
the user to enter another
record and add it to the
end of the file. Display
each row of the .csv file
on a separate line.

"""

import csv

print(__doc__)

title = input('Enter a book title : ')
print(f'The input for a title : {title}')
author = input('ENter the author\'s name : ')
print(f'The input for the author : {author}')
year = input('Enter the year published : ')
print(f'The inpur for the year published : {year}')
print()

filename = 'Books.csv'
with open(filename, 'a') as fo :
    fo.write(f'{title}, {author}, {year}\n')

print('The CSV contents:')
with open(filename, 'r') as fo :
    for row in fo : 
        print(row, end = '')

