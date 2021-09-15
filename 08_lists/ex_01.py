"""Write a function called chop that takes a list and modifies it,
removing the first and last elements, and returns None. Then write
a function called middle that takes a list and returns a new list
that contains all but the first and last elements.
"""


def chop(items):
    del items[0]
    del items[-1]


def middle(items):
    return items[1:-1]


list_1 = ['a', 'b', 'c', 'd']
list_2 = ['a', 'b', 'c', 'd']

chopped = chop(list_1)
print(list_1)        # Should be ['b', 'c']
print(chopped)       # Should be None

middled = middle(list_2)
print(list_2)        # Should be unchanged
print(middled)       # Should be ['b', 'c']
