#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_016
# $ python3 Example_015.py
# $ python3 Example_015.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

015
Ask the user to enter their favourite colour. If they enter “red”, “RED” or
“Red” display the message “I like red too”, otherwise display the message
“I don’t like [colour], I prefer red”.

"""

print(__doc__)

choice = ''
while choice != 'x' :
    colour = input('What is your favourite colour? ')
    choice = colour.lower()
    print()
    print(f'Your colour is {colour}')
    if colour.lower() == 'red' :
        print(f'I like the colour red too.')
    else :
        print(f'I do not like the colour {colour}, I prefer red.')


