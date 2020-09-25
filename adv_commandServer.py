# server side
# Avi Fenesh
# mod for python 3, 2020

import socket

IP = '127.0.0.1'
PORT = 8820

def recive_client_request(client_socket):
    client_message = client_socket.recv(1024)
