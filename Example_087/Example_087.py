#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_087
# $ python3 Example_087.py
# $ python3 Example_087.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

087
Ask the user to type in a word and then
display it backwards on separate lines. For
instance, if they type in “Hello” it should
display as shown below:

o
l
l
e
H

"""

print(__doc__)

a_word = input('Enter a word : ')
print(f'Input for a word : {a_word}')
print()

for i in range(len(a_word), 0, -1) :
    print(a_word[i - 1])
    
