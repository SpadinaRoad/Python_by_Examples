#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_119
# $ python3 Example_119.py
# $ python3 Example_119.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

119
Define a subprogram
that will ask the user to
pick a low and a high
number, and then
generate a random
number between those
two values and store it in
a variable called
“comp_num”.

Define another
subprogram that will
give the instruction “I am
thinking of a number...”
and then ask the user to
guess the number they
are thinking of.

Define a third
subprogram that will
check to see if the
comp_num is the same
as the user’s guess. If it
is, it should display the
message “Correct, you
win”, otherwise it should
keep looping, telling the
user if they are too low or
too high and asking them
to guess again until they
guess correctly.

"""

print(__doc__)

import random

def gen_rand_num() :
    low_num = int(input('Enter a low number: '))
    print(f'The input for the low number: {low_num}')
    high_num = int(input('Enter a higher number: '))
    print(f'The input for the high number: {high_num}')
    print()
    return random.randint(low_num, high_num)

def guess_a_num() :
    print('I am thinking of a number...')
    user_guess = int(input('Enter your guess: '))
    print(f'The input for a guess {user_guess}')
    print()
    return user_guess
    
def check_nums(a : 'target_num', b : 'guess') : 
    correct = False
    while correct != True :
        if a == b : 
            print('Correct, you win.')
            correct = True
        elif a > b :
            print('Your guess is too low.')
        elif a < b : 
            print('Your guess is too high.')
        if correct != True :
            b = int(input('Enter a new guess : '))
            print(f'The input for a guess: {b}')
        print()
           
def main() :
    comp_num = gen_rand_num()
    print(f'The random number is {comp_num}')
    print()

    guess = guess_a_num()
    check_nums(comp_num, guess)

main()

