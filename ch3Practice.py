import sys


def collatz(number):  # does the math for Collatz Sequence
    if number % 2 == 0:
        n = number // 2
        return n

    elif number % 2 == 1:
        n = 3 * number + 1
        return n


try:
    print('Enter number:')
    number = int(input())

    while number != 1:
        collatz(number)
        print(collatz(number))
        number = collatz(number)

except:
    print('Please enter an integer')
