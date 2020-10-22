#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_009
# $ python3 Example_009.py
# $ python3 Example_009.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

009
Write a program
that will ask for a
number of days
and then will
show how many
hours, minutes
and seconds are
in that number of
days.

"""

print(__doc__)
days = input('Enter the number of days : ')
hours = int(days) * 24
minutes = hours * 60
seconds = minutes * 60
print('')
print(f'The number of days entered: {days}')
print(f'There are {hours} hours in {days} days.')
print(f'There are {minutes} minutes in {days} days.')
print(f'There are {seconds} seconds in {days} days.')
