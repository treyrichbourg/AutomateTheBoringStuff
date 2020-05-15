numbers = []

# def sum_of_low(n):
#     n.sort()
#     return n[0] + n[1]
def sum_two_smallest_numbers(numbers):
    """
        Sorts integers in ascending order, returns sum of first 2.
    """
    return sum(sorted(numbers)[:2])

while True:
    print('Enter number ' + str(len(numbers) + 1) + ':(enter nothing to continue)')
    input_string = input()
    if input_string == '':
        break
    input_int = int(input_string)
    numbers = numbers + [input_int]

print(f'The sum of the 2 lowest integers in {numbers} is:')
#print(sum_of_low(numbers))
print(sum_two_smallest_numbers(numbers))