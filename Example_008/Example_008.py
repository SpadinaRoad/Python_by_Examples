#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_008
# $ python3 Example_008.py
# $ python3 Example_008.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

008
Ask for the total price of the bill, then ask how
many diners there are. Divide the total bill by the
number of diners and show how much each
person must pay.

"""

print(__doc__)
total = input('What is the total amount of the bill : ')
diners = input('How many diners are there : ')
average = int(total) / int(diners)
print('')
print(f'The total amount of the bill is {int(total):.2f}')
print(f'The number of diners is {diners}')
print(f'The cost per diner is {average:.2f}')
