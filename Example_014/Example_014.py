#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_014
# $ python3 Example_014.py
# $ python3 Example_014.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

014
Ask the user to enter a
number between 10 and 20
(inclusive). If they enter a
number within this range,
display the message “Thank
you”, otherwise display the
message “Incorrect
answer”.

"""

print(__doc__)
num = int(input('Enter a number between 10 and 20: '))
print()

if num >= 10 and num <=20 :
    print(f'For number, {num}, Thank you.')
else :
    print(f'For number, {num}. Incorrect answer.')

