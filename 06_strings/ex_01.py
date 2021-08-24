"""Write a while loop that starts at the last character in the
string and works its way backwards to the first character in the
string, printing each letter on a separate line, except backwards
"""
index = 0
fruit = 'banana'
while index < len(fruit):
    index = index - 1
    letter = fruit[index]
    print(letter)
