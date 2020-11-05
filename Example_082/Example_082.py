#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_082
# $ python3 Example_082.py
# $ python3 Example_082.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

082
Show the user a line of text from your favourite poem
and ask for a starting and ending point. Display the
characters between those two points.

"""

print(__doc__)

poem_line = 'Here is a line of text from a poem.'
print(poem_line)
start_position = int(input('Enter a starting postion: '))
print(f'The input for the start : {start_position}')
print()

end_position = int(input('Enter an end position: '))
print(f'The input for the end : {end_position}')
print()
print(f'A slice of the poem : {poem_line[start_position:end_position]}')
print

