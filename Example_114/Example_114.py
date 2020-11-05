#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_114
# $ python3 Example_114.py
# $ python3 Example_114.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

114
Using the Books.csv file, ask the user
to enter a starting year and an end
year. Display all books released
between those two years.

"""

import csv

print(__doc__)

start_year = int(input('Enter the start year : '))
print(f'The input for the start year : {start_year}')
print()

end_year = int(input('Enter the end year : '))
print(f'The input for the end year : {end_year}')
print()

filename = "Books.csv"
with open(filename, 'r') as fo:
    reader = csv.reader(fo, delimiter=',')
    for line in reader :
        try : 
            year = int(line[2])
            if year in range(start_year, end_year) : 
                print(f'"{line[0]}" by {line[1]} published in {line[2]}')
        except :
            pass
print()

