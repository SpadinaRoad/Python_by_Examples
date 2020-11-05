#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_122
# $ python3 Example_122.py
# $ python3 Example_122.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

122
Create the following menu:
    A. Add to file
    B. View all records
    X. Quit program
    Enter your selection : 
    
If the user selects 1, allow them to add to a file
called Salaries.csv which will store their name
and salary. If they select 2 it should display all
records in the Salaries.csv file. If they select 3 it
should stop the program. If they select an
incorrect option they should see an error
message. They should keep returning to the
menu until they select option 3.    
    
"""

import csv

print(__doc__)

filename = 'Salaries.csv'

def menu() : 
    print('Main Menu')
    print('A. Add to file')
    print('B. View all records')
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
        
def display_records() : 
    with open(filename, 'r') as fo : 
        reader = list(csv.reader(fo, delimiter=','))
    count = 1
    for i in reader :
        print(f'No. {count}. {i[0]}, {i[1]}')
        count += 1
    print()
        
choice = ''
while choice != 'x' :

    choice = menu().lower()
    print(f'The input for menu choice : {choice}')
    print()
    
    if choice == 'a' :
        add_record()
    elif choice == 'b' :
        display_records() 
    elif choice == 'x' :
        pass
        
        
