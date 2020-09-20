import socket
import time
import random

server_socket = socket.socket()

server_socket.bind(('0.0.0.0', 8820))

server_socket.listen(1)

(client_socket, client_address) = server_socket.accept()

client_message = client_socket.recv(1024)
client_message = client_message.decode()
if client_message == "NAME":
    client_socket.send('My name is avi'.encode())
elif client_message == "TIME":
    freq_time = time.asctime(time.localtime(time.time()))
    time_to_send = str(freq_time)
    client_socket.send(time_to_send.encode())
elif client_message == "RAND":
    rand = str(random.randrange(0, 1009))
    client_socket.send(rand.encode())
elif client_message == "EXIT":
    client_socket.close()
else:
    client_socket.send("your command not exist yet, plese use one of those - NAME, TIME, RAND, EXIT")

client_socket.close()
server_socket.close()