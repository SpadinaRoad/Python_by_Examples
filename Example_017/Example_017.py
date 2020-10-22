#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_017
# $ python3 Example_017.py
# $ python3 Example_017.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

017
Ask the user’s age. If they
are 18 or over, display the
message “You can vote”, if
they are aged 17, display the
message “You can learn to
drive”, if they are 16, display
the message “You can buy a
lottery ticket”, if they are
under 16, display the
message “You can go Trick-
or-Treating”.

"""

print(__doc__)

age = 1
while age != 0 : 
    age = int(input('What is your age? '))
    print()
    print(f'Input for age: {age}')
    
    if age != 0 :
        if age >= 18 :
            print(f'You can vote.')
        elif age == 17 :
            print('You can learn to drive.')
        elif age == 16 :
            print('You can buy a lottery ticket.')
        else :
            print('You can go Trick-or-Treating.')
    print()
    
