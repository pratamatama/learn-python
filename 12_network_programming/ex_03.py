"""Use urllib to replicate the previous exercise of (1) retrieving the document from a URL,
(2) displaying up to 3000 characters, and (3) counting the overall number of characters in
the document. Don’t worry about the headers for this exercise, simply show the first 3000
characters of the document contents."""
import urllib.request

try:
    url = input('Enter url: ')
    fhand = urllib.request.urlopen(url)

    chars = 0
    char_limit = 3000
    for line in fhand:
        line = line.decode()
        next_count = chars + len(line)
        if next_count <= char_limit:
            print(line.rstrip('\n'))
        elif chars < char_limit:
            char_remain = char_limit - chars - 1
            print(line[:char_remain])
        chars = next_count

    print(chars)
except:
    print('Improper formatted url')
