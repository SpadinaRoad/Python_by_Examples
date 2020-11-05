#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_083
# $ python3 Example_083.py
# $ python3 Example_083.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

083
Ask the user to type in a word in upper case. If they
type it in lower case, ask them to try again. Keep
repeating this until they type in a message all in
uppercase.

"""

print(__doc__)

a_word = ''
while not a_word.isupper() :
    a_word = input('Enter a word in uppercase : ')
    print(f'The input for word: {a_word}')
    print()
    
