#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_050
# $ python3 Example_050.py
# $ python3 Example_050.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

050
Ask the user to enter a number between
10 and 20. If they enter a value under 10,
display the message “Too low” and ask
them to try again. If they enter a value
above 20, display the message “Too high”
and ask them to try again. Keep repeating
this until they enter a value that is
between 10 and 20 and then display the
message “Thank you”.

"""

print(__doc__)

num = 0
while num  < 10 or num > 20:

    num = int(input('Enter a number between 10 and 20: '))
    print()
    print(f'The input for a number : {num}.')
    if num < 10 :
        print('Too low.')
    elif num > 20 :
        print('Too high.')
    else :
        print()    
        print(f'Thank you')
    print()    
