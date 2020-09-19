import socket

my_socket = socket.socket()

my_socket.connect(('127.0.0.1', 1729))
my_socket.send('Avi')

data = my_socket.recv(1024)
print("The server sent: " + data)

my_socket.close()