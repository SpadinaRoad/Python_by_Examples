#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_072
# $ python3 Example_072.py
# $ python3 Example_072.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

072
Create a list of six school subjects. Ask the user which of these
subjects they don’t like. Delete the subject they have chosen from the
list before you display the list again.

"""

print(__doc__)

subjects = ['math', 'physics', 'French', 'English', 'chemistry']
print(f'The subjects before : {subjects}')
hate = input('What course don\'t you like? ')
print()
subjects.remove(hate)
print(f'The subjects after : {subjects}')

