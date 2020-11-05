#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_048
# $ python3 Example_048.py
# $ python3 Example_048.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

048
Ask for the name of somebody the user wants to invite
to a party. After this, display the message “[name] has
now been invited” and add 1 to the count. Then ask if
they want to invite somebody else. Keep repeating this
until they no longer want to invite anyone else to the
party and then display how many people they have
coming to the party.

"""

print(__doc__)

count = 0
name = ''
keep_going = ''
while keep_going != 'n' :

    name = input('Enter the name of a party invitee : ')
    print()
    print(f'The input for a name : {name}.')
    print(f'{name} has been invited.')
    count = count + 1
    keep_going = input('Do you want to add another number? (y/n)')
    print()
    print()
    keep_going = keep_going.lower()

print(f'There are {count} people coming to the party.')
print()
