#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_086
# $ python3 Example_086.py
# $ python3 Example_086.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

086
Ask the user to enter a new password. Ask
them to enter it again. If the two passwords
match, display “Thank you”. If the letters are
correct but in the wrong case, display the
message “They must be in the same case”,
otherwise display the message “Incorrect”.

"""

print(__doc__)

new_password = ''
while new_password != 'x' :
    new_password = input('Enter a new password : ')
    print(f'The input for password : {new_password}')

    if new_password != 'x' : 
        re_entered = input('Re-enter the password : ')
        print(f'The input for the re-entry : {re_entered}')

        if new_password == re_entered :
            print('Thank you.')
        elif new_password.lower() == re_entered.lower() :
            print('The passwords must be in the same case.')
        else : 
            print('Incorrect')
    print()
    
