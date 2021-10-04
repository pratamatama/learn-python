"""(Advanced) Change the socket program so that it only shows data after the headers
and a blank line have been received. Remember that recv receives characters (newlines
and all), not lines."""
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

data = mysock.recv(512)
message = data.decode()

# Finds the end of header
# Adds four to exclude: '\r\n\r\n'
header_end_pos = message.find('\r\n\r\n') + 4
print(message[header_end_pos:], end='')

while True:
    data = mysock.recv(512)
    if not data:
        break
    print(data.decode())

mysock.close()
