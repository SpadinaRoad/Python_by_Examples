#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_113
# $ python3 Example_113.py
# $ python3 Example_113.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

113
Using the Books.csv file, ask the user how many records
they want to add to the list and then allow them to add
that many. After all the data has been added, ask for an
author and display all the books in the list by that author.
If there are no books by that author in the list, display a
suitable message.

"""

import csv

print(__doc__)

count = int(input('How many books to add to the list: '))
print(f'The input for the number of books: {count}.')
print()

for i in range(count) : 
    
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

choice = input('Choose an author : ')
print(f'The input for author choice : {choice}')
print()

author_found = False
with open(filename, 'r') as fo:
    for row in fo : 
        if choice in row :
            print(row, end='')
            author_found = True

if not author_found : 
    print(f'The author {choice} not found in list.')


