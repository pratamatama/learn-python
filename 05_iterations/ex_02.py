"""
Write another program that prompts for a list of numbers as above
and at the end prints out both the maximum and minimum of the numbers
instead of the average.
"""
numbers = []
while True:
    try:
        value = input('Enter a number: ')
        if value == 'done':
            break
        numbers.append(int(value))
    except:
        print('Invalid input')

print(max(numbers), min(numbers))
