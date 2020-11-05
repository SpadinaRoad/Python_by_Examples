#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_123
# $ python3 Example_123.py
# $ python3 Example_123.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

123
123
In Python, it is not technically possible to directly
delete a record from a .csv file. Instead you need
to save the file to a temporary list in Python,
make the changes to the list and then overwrite
the original file with the temporary list.
Change the previous program to allow you to do
this. Your menu should now look like this:

Create the following menu:
    A. Add to file
    B. View all records
    C. Delete a record
    X. Quit program
    Enter your selection : 
    
"""

import csv

print(__doc__)

filename = 'Salaries.csv'

def menu() : 
    print('Main Menu')
    print('A. Add to file')
    print('B. View all records')
    print('C. Delete a record')
    print('X. Quit program')
    print()
    return input('Enter your selection : ')

def add_record() :
    name = input('Enter a name : ')
    print(f'The input for a name is {name}')
    print()
    salary = int(input('Enter the salary : '))
    print(f'The input for a salary {salary}')
    print()
    with open(filename, 'a') as fo : 
        fo.write(f'{name},{salary}\n')
        
def read_file() : 
    with open(filename, 'r') as fo : 
        return list(csv.reader(fo, delimiter=','))
        
def display_records() : 
    file_contents = read_file()
    count = 1
    for i in file_contents :
        print(f'No. {count}. {i[0]}, {i[1]}')
        count += 1
    print()
        
def delete_record() : 
    file_contents = read_file()
    display_records()
    index = int(input('Enter the index number for the record to delete: '))
    print(f'The input for the index: {index}')
    print()
    del file_contents[index - 1]
    with open(filename, 'w') as fo : 
        for i in file_contents : 
            fo.write(f'{[i][0][0]},{[i][0][1]}\n')
    display_records()
    
choice = ''
while choice != 'x' :

    choice = menu().lower()
    print(f'The input for menu choice : {choice}')
    print()
    
    if choice == 'a' :
        add_record()
    elif choice == 'b' :
        display_records() 
    elif choice == 'c' :
        delete_record()
    elif choice == 'x' :
        pass
        
        
