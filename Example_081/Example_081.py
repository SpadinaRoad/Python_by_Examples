#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_081
# $ python3 Example_081.py
# $ python3 Example_081.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

081
Ask the user to type in their favourite school subject.
Display it with “-” after each letter, e.g. S-p-a-n-i-s-h-.

"""

print(__doc__)

subject = input('What was your favourite school subject : ')
print(f'The input for first name : {subject}')
print()
for i in subject : 
    print(f'{i}-', end='')

print()
