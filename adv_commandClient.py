# client side
# Avi Fenesh
# mod for python 3, 2020

import socket

IP = '127.0.0.1'
PORT = 8820

requests = ["TAKE_SCREENSHOT", "SEND_FILE", "DIR", "DELETE", "COPY", "EXECUTE", "EXIT"]


def valid_request(request):
    if request in requests:
        valid = True
    else:
        valid = False
    return valid


def send_request_to_server(my_socket, request):
    send_request = str(len(request)) + request
    my_socket.send(send_request.encode())


def handle_server_response(my_socket, request):
    if request == "":
        recv_data_len = my_socket.recv(1024)
