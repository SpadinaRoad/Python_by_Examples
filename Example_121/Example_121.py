#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_121
# $ python3 Example_121.py
# $ python3 Example_121.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

121
Create a program that will allow the user to easily manage a list of names. You should
display a menu that will allow them to add a name to the list, change a name in the
list, delete a name from the list or view all the names in the list. There should also be a
menu option to allow the user to end the program. If they select an option that is not
relevant, then it should display a suitable message. After they have made a selection
to either add a name, change a name, delete a name or view all the names, they
should see the menu again without having to restart the program. The program
should be made as easy to use as possible.

"""

print(__doc__)

def menu() :
    print('Main Menu')
    print('----------')
    print('A. List names')
    print('B. Add a name')
    print('C. Change a name')
    print('D. Delete a name')
    print('X. Exit')
    print()
    return input('Enter menu item : ')
    
def list_names() :
    print('List of Names.') 
    count = 1
    for i in names_list : 
        print(f'{count} : {i}')
        count += 1
        
def add_name() :
    new_name = input('Enter a new name: ')
    print(f'The input for a name : {new_name}')
    names_list.append(new_name)

def change_name() : 
    list_names()
    index = int(input(f'Enter the number for the name to change: '))
    print(f'The input for the index: {index}')
    new_name = input('Enter the new name: ')
    print(f'The input for a name : {new_name}')
    print()
    names_list[index - 1] = (new_name)
    list_names()
    
def delete_name() : 
    list_names()
    index = int(input(f'Enter the number for the name to change: '))
    print(f'The input for the index: {index}')
    del names_list[index - 1]
    
names_list = []

choice = ''
while choice != 'x' : 
    choice = menu().lower()
    print(f'The input for the choice: {choice}')
    print()
    
    if choice == 'a' : 
        list_names()

    elif choice == 'b' :
        add_name()
        
    elif choice == 'c' :
        change_name()
        
    elif choice == 'd' :
        delete_name()
        
    elif choice == 'x' :
        pass
    else : 
        print('Please enter one of A, B, C, D or X.')
        
    print()
    

