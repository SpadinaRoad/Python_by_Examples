#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_051
# $ python3 Example_051.py
# $ python3 Example_051.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

051
Using the song “10 green bottles”, display the lines “There are [num] green bottles
hanging on the wall, [num] green bottles hanging on the wall, and if 1 green bottle
should accidentally fall”. Then ask the question “how many green bottles will be
hanging on the wall?” If the user answers correctly, display the message “There will be
[num] green bottles hanging on the wall”. If they answer incorrectly, display the
message “No, try again” until they get it right. When the number of green bottles gets
down to 0, display the message “There are no more green bottles hanging on the wall”.

"""

print(__doc__)

num = 10
while num  != 0 :

    print(f'There are {num} green bottles hanging on the wall, '
    f'{num} green bottles hanging on the wall, '
    f'and if 1 green bottle should accidentally fall.')
    print()
    num -= 1
    guess = int(input('How many green bottles will be hanging on the wall?'))
    print()
    print(f'The input for a number : {num}.')

    if guess == num : 
        print(f'There will be {num} green bottles hanging on the wall.')
    elif guess != num : 
        print('No, try again.')
    elif num == 0 :
        print('There are no more green bottles hanging on the wall.')
        
    print()    
