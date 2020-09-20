import socket


my_socket = socket.socket()

my_socket.connect(('127.0.0.1', 8820))
name = input("please type your name here - ").encode()
my_socket.send(name)

data = my_socket.recv(1024)
print("The server sent: " + data.decode())

my_socket.close()