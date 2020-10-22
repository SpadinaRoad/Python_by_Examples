#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_019
# $ python3 Example_019.py
# $ python3 Example_019.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

019
Ask the user to enter 1, 2 or 3. If they enter a 1, display
the message “Thank you”, if they enter a 2, display
“Well done”, if they enter a 3, display “Correct”. If
they enter anything else, display “Error message”.

"""

print(__doc__)

num = 1
while num != 0 : 
    num = int(input('Enter a 1, 2 or 3: '))
    print()
    print(f'Input for number : {num}')
    
    if num != 0 :
        if num == 1 :
            print(f'Thank you.')
        elif num == 2 :
            print('Well done.')
        elif num == 3 :
            print('Correct.')
        else :
            print('Error message.')
    print()
    
