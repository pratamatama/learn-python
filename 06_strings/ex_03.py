"""Encapsulate this code in a function named count, and generalize
it so that it accepts the string and the letter as arguments.
"""


def count(word, letter):
    count = 0
    for char in word:
        if char == letter:
            count = count + 1
    return count


print(count('banana', 'a'))
