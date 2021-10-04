"""Change your socket program so that it counts the number of characters
it has received and stops displaying any text after it has shown 3000
characters. The program should retrieve the entire document and count
the total number of characters and display the count of the number of
characters at the end of the document.
"""
import socket

url = input('Enter url: ')

try:
    address = url.split('/')
    HOST = address[2]
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((HOST, 80))
    cmd = ('GET ' + url + ' HTTP/1.0\r\n\r\n').encode()
    mysock.send(cmd)

    count = 0
    while True:
        data = mysock.recv(512)

        for characters in data:
            count += 1

        if count > 3000 or len(data) < 1:
            break

    print(count)
    mysock.close()
except:
    print('Improper formatted url')
