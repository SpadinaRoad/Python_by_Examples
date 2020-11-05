#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_055
# $ python3 Example_055.py
# $ python3 Example_055.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

055
Randomly choose a number between 1 and 5. Ask the user to pick a
number. If they guess correctly, display the message “Well done”,
otherwise tell them if they are too high or too low and ask them to pick a
second number. If they guess correctly on their second guess, display
“Correct”, otherwise display “You lose”.

"""

import random

print(__doc__)

your_choice = ''
attempt = 1
rand_num = random.randint(1, 5)

while your_choice != 'x' : 
    print()
    your_choice = input('Enter a number between 1 and 5: ')
    new_choice = False
     
    if your_choice != 'x' :
        print(f'The input for the number {your_choice}')
        your_choice = int(your_choice)
        
        if your_choice == rand_num :
            new_choice = True
            if attempt == 1 :
                print('Well done.')
            else : 
                print('Correct')
        elif your_choice < rand_num :
            if attempt == 1 :
                print('Your choice is too low.')
            else :
                print('You lose.')
                new_choice = True
        else :
            if attempt == 1 :
                print('Your choice is too high.')
            else : 
                print('You lose.')
                new_choice = True

        if new_choice == True :
            print(f'The number to pick {rand_num}')
            print()
            attempt = 1
            rand_num = random.randint(1, 5)
        else : 
            attempt = 2
