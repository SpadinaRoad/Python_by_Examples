#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_076
# $ python3 Example_076.py
# $ python3 Example_076.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

076
Ask the user to enter the names of three people they want to
invite to a party and store them in a list. After they have entered
all three names, ask them if they want to add another. If they do,
allow them to add more names until they answer “no”. When
they answer “no”, display how many people they have invited to
the party.

"""

print(__doc__)

list_of_invitees = []
for i in range(3) :
    invitee = input('Enter the name the person to invite : ')
    print(f'The input for invitee: {invitee}')
    print()
    list_of_invitees.append(invitee)
    
add_to = ''
while add_to != 'n' :
    add_to = input('Do you want to invite another person? (y/n) ')
    print()
    add_to.lower()
    if add_to != 'n' : 
        invitee = input('Enter the name the person to invite : ')
        print(f'The input for invitee: {invitee}')
        print()
        list_of_invitees.append(invitee)

print(f'The list of invitees: {list_of_invitees}')
print(f'The number of invitees: {len(list_of_invitees)}')

