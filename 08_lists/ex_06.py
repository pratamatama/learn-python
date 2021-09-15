"""Rewrite the program that prompts the user for a list of numbers and prints out
the maximum and minimum of the numbers at the end when the user enters “done”.
Write the program to store the numbers the user enters in a list and use the max()
and min() functions to compute the maximum and minimum numbers after the loop
completes.
"""
numbers = []
while(True):
    try:
        value = input('Enter a number: ')
        if (value == 'done'):
            break
        numbers.append(float(value))
    except:
        print('Please enter a valid number or type "done" to end the program')

if (len(numbers) > 0):
    print('Maximum: ', max(numbers))
    print('Minimum: ', min(numbers))
else:
    print('Can\'t find any numbers from the given input, closing the program.')
