#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_097
# $ python3 Example_097.py
# $ python3 Example_097.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

097
Using the 2D list from program 096, ask the user to
select a row and a column and display that value.
    
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
col = int(input('Enter the column : '))
print(f'The input for a column : {col}')
print()

print(f'The value at row {row} and column {col} is: {the_array[row][col]}')
