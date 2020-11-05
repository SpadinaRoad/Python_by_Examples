#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_077
# $ python3 Example_077.py
# $ python3 Example_077.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

077
Change program 076 so that once the user has completed their list of names, display the
full list and ask them to type in one of the names on the list. Display the position of that
name in the list. Ask the user if they still want that person to come to the party. If they
answer “no”, delete that entry from the list and display the list again.

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
        print('Adding another name to the list.')
        invitee = input('Enter the name the person to invite : ')
        print(f'The input for invitee: {invitee}')
        print()
        list_of_invitees.append(invitee)
    else : 
        print('Stopped adding names to the party.')

print(f'The list of invitees: {list_of_invitees}')
print(f'The number of invitees: {len(list_of_invitees)}')
print()

name_picked = input('Enter a name from a list? ')
print(f'The input for a name {name_picked}')

delete_from = input(f'Do you {name_picked} to come to the party (y/n)? ')
delete_from.lower()
print(f'The input for inviting {delete_from}')
print()

if delete_from == 'n' :
    print(f'{name_picked} removed from the list.')
    list_of_invitees.remove(name_picked)
    
print(f'The list of invitees: {list_of_invitees}')
print(f'The number of invitees: {len(list_of_invitees)}')




