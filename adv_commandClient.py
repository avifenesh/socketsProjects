# client side
# Avi Fenesh
# mod for python 3, 2020

import socket
import PIL
from PIL import Image

IP = '127.0.0.1'
PORT = 8820

requests = ["TAKE_SCREENSHOT", "SEND_FILE", "DIR", "DELETE", "COPY", "EXECUTE", "EXIT"]


def valid_request(request):
    req_to_check = request.split('#')
    if req_to_check[0] in requests:
        valid = True
    else:
        valid = False
    return valid


def send_request_to_server(my_socket, request):
    my_socket.send(request.encode())


def handle_server_response(my_socket, request):
    req_to_check = request.split('#')
    if req_to_check[0] != "SEND_FILE":
        print(my_socket.recv(1024).decode())
    else:
        with open('recived_file.png','wb') as f:
            print('file opened')
            while True:
                print('receiving data...')
                data = my_socket.recv(1024)
                print('data=%s', (data))
                if not data:
                    break
                else:
                    f.write(data)
        f.close()
        print('Successfully get the file')

def main():
    # open socket with the server
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect((IP, PORT))
    # print instructions
    print('Welcome to remote computer application. Available commands are:\n')
    print('TAKE_SCREENSHOT\nSEND_FILE\nDIR\nDELETE\nCOPY\nEXECUTE\nEXIT')
    print('before adding a path please type # before, instead of space')
    done = False
    # loop until user requested to exit
    while not done:
        request = str(input('Please enter command:\n'))
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