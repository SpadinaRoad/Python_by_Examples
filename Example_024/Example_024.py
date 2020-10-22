#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_024
# $ python3 Example_024.py
# $ python3 Example_024.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

024
Ask the user to type in any word and display it in
upper case.

"""

print(__doc__)

text = ''
while text != 'x' : 
    text = input('Enter a word: ')
    if text != 'x' : 
        print()
        print(f'Input for a word : {text}')
        text_up = text.upper()
        print(f'The word in uppercase is : {text_up}')
        print()
            
