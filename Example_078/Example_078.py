#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_078
# $ python3 Example_078.py
# $ python3 Example_078.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

078
Create a list containing the titles of
four TV programmes and display
them on separate lines. Ask the
user to enter another show and a
position they want it inserted into
the list. Display the list again,
showing all five TV programmes in
their new positions.

"""

print(__doc__)

list_tv_shows = ['The National', 'Mr. Dress-up', 'Schitt\'s Creek', 'Hockey Night In Canada']
print('The list of TV shows : ')
print('---------------------- ')
for i in list_tv_shows :
    print(i)
    
print()
new_show = input('Enter a TV show: ')
print(f'The input for a TV show {new_show}')
print()

insert_position = int(input('Enter a number to insert the show: '))
print(f'The input for position is {insert_position}')
print()

list_tv_shows.insert(insert_position, new_show)
print('The new list of TV shows.')
print('-------------------------')
for i in list_tv_shows :
    print(i)
