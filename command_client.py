import socket

my_socket = socket.socket()

my_socket.connect(('127.0.0.1', 8820))
command = input("use one of those commands - TIME, NAME, RAND, EXIT.  please type your command here - ")
my_socket.send(command.encode())
data = my_socket.recv(1024)
print("The server sent: " + data.decode())

my_socket.close()
