#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_049
# $ python3 Example_049.py
# $ python3 Example_049.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

049
Create a variable called
compnum and set the value
to 50. Ask the user to enter a
number. While their guess
is not the same as the
compnum value, tell them if
their guess is too low or too
high and ask them to have
another guess. If they enter
the same value as
compnum, display the
message “Well done, you
took [count] attempts”.

"""

print(__doc__)

compnum = 50
guess = 0
count = 0
while compnum != guess :

    guess = int(input('Enter a number: '))
    print()
    print(f'The input for a number : {guess}.')
    count += 1
    if guess > compnum :
        print('Your guess is too high.')
    elif guess < compnum :
        print('Your guess is too low.')
    else :
        print()    
        print(f'Well done, you took {count} attempts.')
    print()    
