"""Find all unique words in a file
Shakespeare used over 20,000 words in his works. But how would you determine that?
How would you produce the list of all the words that Shakespeare used? Would you
download all his work, read it and track all unique words by hand?

Let’s use Python to achieve that instead. List all unique words, sorted in
alphabetical order, that are stored in a file romeo.txt containing a subset of
Shakespeare’s work.

To get started, download a copy of the file www.py4e.com/code3/romeo.txt. Create
a list of unique words, which will contain the final result. Write a program to open
the file romeo.txt and read it line by line. For each line, split the line into a
list of words using the split function. For each word, check to see if the word is
already in the list of unique words. If the word is not in the list of unique words,
add it to the list. When the program completes, sort and print the list of unique
words in alphabetical order.
"""
try:
    filename = input('Enter file: ')
    fhand = open(
        'C:\\Users\\Rin\\Documents\\Learn\\py4e\\08_lists\\' + filename)
    unique_words = []
    for line in fhand:
        words = line.split()
        for word in words:
            if (word in unique_words):
                continue
            unique_words.append(word)
    unique_words.sort()
    print(unique_words)
except:
    print('Error, failed to open the file named:', filename)
