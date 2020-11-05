#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_098
# $ python3 Example_098.py
# $ python3 Example_098.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

098
Using the 2D list from program 096, ask the user
which row they would like displayed and display
just that row. Ask them to enter a new value and
add it to the end of the row and display the row
again.
    
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
