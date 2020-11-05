#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_099
# $ python3 Example_099.py
# $ python3 Example_099.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

099
Change your previous program
to ask the user which row they
want displayed. Display that
row. Ask which column in that
row they want displayed and
display the value that is held
there. Ask the user if they want
to change the value. If they do,
ask for a new value and change
the data. Finally, display the
whole row again.
    
"""

print(__doc__)

the_array = []
the_array.append([2, 5, 8])
the_array.append([3, 7, 4])
the_array.append([1, 6, 9])
the_array.append([4, 2, 0])

print(the_array)
print()

row = int(input('Enter a row number : '))
print(f'The input for the row : {row}')
print()

print(f'The values at row {row} are : {the_array[row]}')

col = int(input('Enter a column number : '))
print(f'The inpurt for the column {col}')
print()

print(f'The value at row {row} and column {col} is {the_array[row][col]}')
print()

change = input('Do you want to change the value (y/n)? ')
print(f'The input for changing value is {change}.')
change = change.lower()
print()

if change == 'y' : 
    value = int(input('Enter the new number : '))
    print(f'The input for a number: {value} ')
    the_array[row][col] = value
    print()
    
print(f'The array : {the_array}')
print()

