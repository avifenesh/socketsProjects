import socket

my_socket = socket.socket()

my_socket.connect(('127.0.0.1', 8820))
command = input("use one of those commands - TIME, NAME, RAND, EXIT.  please type your command here - ")
my_socket.send(command.encode())
receiving = True
data = ''
while receiving:
    message = my_socket.recv(1024).decode()
    if message == 'end of message':
        receiving = False
    else:
        data += message


print("The server sent: " + data)

my_socket.close()
