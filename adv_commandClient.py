# client side
# Avi Fenesh
# mod for python 3, 2020

import socket
import time

IP = '127.0.0.1'
PORT = 8820

requests = ["TAKE_SCREENSHOT", "SEND_FILE", "DIR", "DELETE", "COPY", "EXECUTE", "EXIT"]


def valid_request(request):
    req_to_check = [] + request.split()
    if req_to_check[0] in requests:
        valid = True
    else:
        valid = False
    return valid


def send_request_to_server(my_socket, request):
    my_socket.send(request.encode())


def handle_server_response(my_socket, request):
    req_to_check = request.split()
    if req_to_check[0] != 'SEND_FILE':
        print(my_socket.recv(1024).decode())
    else:
        count = 0
        picture = b''
        while True:
            data = my_socket.recv(5120)
            if (len(data) < 1): break
            time.sleep(0.25)
            count = count + len(data)
            print(len(data), count)
            picture = picture + data
        pos = picture.find(b'\\r\\n\\r\\n\\')
        print('Header length', pos)
        print(picture[:pos].decode())

        picture = picture[pos + 4:]
        fhand = open('stuff.jpg', 'wb')
        fhand.write(picture)
        fhand.close()


def main():
    # open socket with the server
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect((IP, PORT))
    # print instructions
    print('Welcome to remote computer application. Available commands are:\n')
    print('TAKE_SCREENSHOT\nSEND_FILE\nDIR\nDELETE\nCOPY\nEXECUTE\nEXIT')
    done = False
    # loop until user requested to exit
    while not done:
        request = str(input("Please enter command:\n"))
        if valid_request(request):
            send_request_to_server(my_socket, request)
            handle_server_response(my_socket, request)
            if request == 'EXIT':
                done = True
        else:
            print('request not exist')
    my_socket.close()


if __name__ == '__main__':
    main()
