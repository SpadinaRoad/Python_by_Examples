#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_120
# $ python3 Example_120.py
# $ python3 Example_120.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

120
Display the following menu to the user:

    1) Addition
    2) Subtraction
    Enter 1 or 2 : 

If they enter a 1, it should run a subprogram that will
generate two random numbers between 5 and 20, and
ask the user to add them together. Work out the correct
answer and return both the user’s answer and the
correct answer.

If they entered 2 as their selection on the menu, it
should run a subprogram that will generate one number
between 25 and 50 and another number between 1 and
25 and ask them to work out num1 minus num2. This
way they will not have to worry about negative answers.
Return both the user’s answer and the correct answer.

Create another subprogram that will check if the user’s
answer matches the actual answer. If it does, display
“Correct”, otherwise display a message that will say
“Incorrect, the answer is” and display the real answer.

If they do not select a relevant option on the first menu
you should display a suitable message.

"""

import random

print(__doc__)

def addition() :
    a = random.randint(5, 20)
    b = random.randint(5, 20)
    value = a + b 
    answer = int(input(f'What is {a} plus {b} : '))
    print(f'The input for the answer: {answer}')
    print()
    return (value, answer)

def subtraction() : 
    a = random.randint(25, 50)
    b = random.randint(1, 25)
    value = a - b
    answer = int(input(f'What is {a} less {b} : '))
    print(f'The input for the answer: {answer}')
    print()
    return(value, answer)
    
def check_answer(a: 'numbers') :
    if a[0] == a[1] :
        print('Correct.')
    else : 
        print('Incorrect.')
        
def main() : 

    print('1) Addition')
    print('2) Subtraction')
    choice = int(input('Enter 1 or 2 : '))
    print()
    print(f'The input for choice : {choice}')
    print()
    
    if choice not in range(1, 2) : 
        print('You choice cannot be processed.')
        print()
        return
    if choice == 1 : 
        to_check = addition()
    elif choice == 2 : 
        to_check = subtraction()
    check_answer(to_check)
    print()
    
main()

