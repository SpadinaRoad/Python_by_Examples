#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_047
# $ python3 Example_047.py
# $ python3 Example_047.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

047
Ask the user to enter a
number and then enter
another number. Add these
two numbers together and
then ask if they want to add
another number. If they
enter “y", ask them to enter
another number and keep
adding numbers until they
do not answer “y”. Once the
loop has stopped, display
the total.

"""

print(__doc__)

num_1 = int(input('Enter a number : '))
print()
print(f'The input for a number : {num_1}.')
print()
total = num_1

keep_going = ''
while keep_going != 'n' :

    num_2 = int(input('Enter another number : '))
    print()
    print(f'The input for another number : {num_2}.')
    print()

    total = total + num_2

    keep_going = input('Do you want to add another number? (y/n)')
    print()
    keep_going = keep_going.lower()

print(f'The total of is {total}')
print()
