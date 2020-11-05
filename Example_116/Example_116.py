#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_116
# $ python3 Example_116.py
# $ python3 Example_116.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

116
Import the data from the Books.csv file into a list. Display the
list to the user. Ask them to select which row from the list
they want to delete and remove it from the list. Ask the user
which data they want to change and allow them to change it.
Write the data back to the original .csv file, overwriting the
existing data with the amended data.

"""

import csv

print(__doc__)

#Read the csv file into a list and display it.
filename = "Books.csv"
with open(filename, 'r') as fo:
    reader = list(csv.reader(fo, delimiter=','))
    # Remove header data
    del reader[0]
    row_num = 1
    for row in reader :
        print(f'Row {row_num}: {row}')
        row_num += 1
print()

#Delete a row.
row_to_delete = int(input('Enter a row to delete: '))        
print(f'The input for row to delete: {row_to_delete}')
if row_to_delete in range(0, len(reader)) : 
    print(f'The row was deleted.')
    del reader[row_to_delete - 1]
else : 
    print(f'Your entry, {row_to_delete}, is not in the list.')
    print('No row deleted.')
print()

# List the books.
row_num = 1
for row in reader :
    print(f'For the row {row_num} the value is : {row}')
    row_num += 1
print()

#Row to change.
row_to_change = int(input('Enter a row to change: '))
print(f'The input for the row to change: {row_to_change}')
row_to_change -= 1
print(f'The row to change: {reader[row_to_change]}')
print()

#Change title.
change = input('Change the title (y/n)? ')
if change.lower() == 'y' :
    title = input('Enter new title: ')
    print(f'The input for title {title}')
    reader[row_to_change][0] = title
    print()
    
#Change author.
change = input('Change the author (y/n)? ')
if change.lower() == 'y' :
    author = input('Enter author name: ')
    print(f'The input for author {author}')
    reader[row_to_change][1] = author
    print()
    
#Change year.
change = input('Change the year (y/n)? ')
if change.lower() == 'y' :
    year = input('Enter year: ')
    print(f'The input for year {year}')
    reader[row_to_change][2] = year
    print()
    
# List the books
row_num = 1
for row in reader :
    print(f'For the row {row_num} the value is : {row}')
    row_num += 1
print()

#Write changes to the csv file
row_num = 0
with open(filename, 'w') as fo : 
    fo.write('Book, Author, Year Released\n')
    for row in reader : 
        fo.write(f'{reader[row_num][0]},{reader[row_num][1]},{reader[row_num][2]}\n')
        row_num += 1
    print('The csv file was updated.')

print()
    
