#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_043
# $ python3 Example_043.py
# $ python3 Example_043.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

043
Ask which direction the user wants to count (up or down). If they select up, then ask
them for the top number and then count from 1 to that number. If they select down, ask
them to enter a number below 20 and then count down from 20 to that number. If they
entered something other than up or down, display the message “I don’t understand”.

"""

print(__doc__)

direction = ''
while direction != 'x' : 

    direction = input('Do you want to count up or down (U/D)? ')
    print()
    print(f'The input for direction : {direction}.')
    
    if direction != 'x' : 
        if direction.lower() == 'u' :
            num = int(input('Enter a number : '))
            print()
            print(f'The input for a num : {num}.')
            for i in range(1, num + 1) :
                print(f'{i}')
        elif direction.lower() == 'd' :
            num = int(input('Enter a number below 20 : '))
            print()
            print(f'The input for a num : {num}.')
            for i in range(20, num - 1, -1) :
                print(f'{i}')
        else : 
            print('I don’t understand')
    
