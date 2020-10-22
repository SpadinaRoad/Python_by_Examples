#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_013
# $ python3 Example_013.py
# $ python3 Example_013.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

013
Ask the user to enter a
number that is under
20. If they enter a
number that is 20 or
more, display the
message “Too high”,
otherwise display
“Thank you”.

"""

print(__doc__)
num = int(input('Enter a number under 20: '))
print()

if num >= 20 :
    print(f'The number, {num}, is too high.')
else :
    print(f'For number, {num}, Thank you.')

