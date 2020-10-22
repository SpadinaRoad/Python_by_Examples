#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_016
# $ python3 Example_016.py
# $ python3 Example_016.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

016
Ask the user if it is raining and convert their answer to lower case
so it doesn’t matter what case they type it in. If they answer “yes”,
ask if it is windy. If they answer “yes” to this second question,
display the answer “It is too windy for an umbrella”, otherwise
display the message “Take an umbrella”. If they did not answer yes
to the first question, display the answer “Enjoy your day”.

"""

print(__doc__)

is_raining = input('Is it raining? ')
is_raining = is_raining.lower()
print()

print(f'Is raining answer: {is_raining}')
if is_raining == 'yes' : 
    is_windy = input('Is it windy? ')
    is_windy = is_windy.lower()
    print()
    print(f'Is windy answer: {is_windy}')
    if is_windy == 'yes' :
        print(f'It is too windy for an umbrella.')
    else :
        print(f'Take an umbrella.')
else : 
    print(f'It is not raining: {is_raining}. Enjoy your day.')
