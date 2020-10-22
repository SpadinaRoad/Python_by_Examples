#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_002
# $ python3 Example_002.py
# $ python3 Example_002.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

002
Ask for the user’s first name and then ask for
their surname and display the output message
Hello [First Name] [Surname] .

"""

print(__doc__)
fname = input('What is your first name? ')
lname = input('What is your last name? ')
print(f'Hello {fname} {lname}')
