#! Python3
# Write a function that uses regex to make sure a password string it is passed is strong
# should be at least eight characters long, contain uppercase and lowercase and have at least one digit

import re, sys

eight_char_long = re.compile(r"\S{8,}")  # Check for 8 characters
lower_case = re.compile(r"[a-z]+")  # Check for at least one lower case
upper_case = re.compile(r"[A-Z]+")  # check for at least one upper case
one_or_more_digit = re.compile(r"\d+")  # check for at least one digit


def strong_pw_detection(password):
    if eight_char_long.search(password) == None:
        print("Please enter a password that at least eight characters long.")
    elif lower_case.search(password) == None:
        print("Please add at least one lower case letter.")
    elif upper_case.search(password) == None:
        print("Please add at least one upper case letter.")
    elif one_or_more_digit.search(password) == None:
        print("Please add one or more digit.")
    else:
        print("This password is stronk!")


# strong_pw_detection('IsThisAGoodPW123')
# strong_pw_detection('WhatdOyounotlikDe12')
# strong_pw_detection('howboutthis1')
# strong_pw_detection('Orthis1')
# strong_pw_detection('Orthis')

while True:
    try:
        print("Please enter a strong password:\n(Press Ctrl+c to exit at any time)")
        password = input()
        strong_pw_detection(password)
    except KeyboardInterrupt:
        sys.exit()
