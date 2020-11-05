#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_074
# $ python3 Example_074.py
# $ python3 Example_074.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

074
Enter a list of ten colours.
Ask the user for a starting
number between 0 and 4
and an end number
between 5 and 9. Display
the list for those colours
between the start and end
numbers the user input.

"""

print(__doc__)

colours = ['yellow', 'orange', 'red', 'purple', 'blue', 'green', 'brown', 'black', 'mauve', 'rose']
print(f'The colours : {colours}')

start_num = int(input('Enter a starting number (0-4) : '))
print(f'The input for the starting number : {start_num}')
print()

end_num = int(input('Enter an ending number (5-9) : '))
print(f'The input for the ending number : {end_num}')
print()
print(f'The subset of colours: {colours[start_num:end_num]}')
