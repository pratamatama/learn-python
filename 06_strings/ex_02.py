# Exercise 2: Given that fruit is a string, what does fruit[:] mean?
fruit = 'banana'
result = fruit[:]
print(result)

"""ANSWER:
It doesn't mean anything because we don't put a start, or an end
of indices to slice the string. In other words, it's a string slice
attempt that is used without giving indices and will return the full
string out of it.
"""
