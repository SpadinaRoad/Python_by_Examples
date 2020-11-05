#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_109
# $ python3 Example_109.py
# $ python3 Example_109.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

109
Display the following menu to the user:
    1) Create a new file
    2) Display the file
    3) Add a new item to the file
Make a selection 1, 2, 3 :

Ask the user to enter 1, 2 or 3. If they select
anything other than 1, 2 or 3 it should display a
suitable error message.

If they select 1, ask the user to enter a school
subject and save it to a new file called
“Subject.txt”. It should overwrite any existing file
with a new file.

If they select 2, display the contents of the
“Subject.txt” file.

If they select 3, ask the user to enter a new
subject and save it to the file and then display
the entire contents of the file.
Run the program several times to test the
options.    

"""

print(__doc__)

filename = 'Subjects.txt'

choice = ''
while choice != 'x' :

    print('1) Create a new file.')
    print('2) Display the file')
    print('3) Add a new item to the file')
    print()
    choice = input('Make a selection 1, 2, 3 : ')
    print(f'The input for selection is : {choice}')
    print()
    
    if choice != 'x' :
        if choice not in '123' :
            print('Select from 1, 2, or 3')
            print()
        else :
            if choice == '1' : 
                subject = input('Enter a school subject: ')
                print(f'Input for a subject {subject}')
                print()
                with open(filename, 'w') as fo :
                    fo.write(f'{subject}\n')
            elif choice == '2' :
                with open(filename, 'r') as fo :
                    file_contents = fo.read()
                    print('The contents of the file: ')
                    print(file_contents)
                print()
                
            elif choice == '3' : 
                subject = input('Enter a school subject: ')
                print(f'Input for a subject {subject}')
                print()
                with open(filename, 'a') as fo :
                    fo.write(f'{subject}\n')
                with open(filename, 'r') as fo :
                    file_contents = fo.read()
                    print('The contents of the file: ')
                    print(file_contents)
                print()
            
