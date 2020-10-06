# client side
# Avi Fenesh
# mod for python 3, 2020

import random
import socket

IP = '127.0.0.1'
FIRST_PORT = 8805


def randomise_port():
    return random.randrange(1111, 9999)


def send_message_to_server(my_socket, message):
    my_socket.send(message.encode())


def get_server_response(my_socket):
    response = my_socket.recv(1024).decode()
    return response


def main():
    port = FIRST_PORT
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        # open socket with the server
        my_socket.connect((IP, port))
        # print instructions
        print('if you want to stop the connection, please type "exit" \n')
        message = input('please type the message to the other side here:')
        port = randomise_port()
        if message == 'exit':
            my_socket.send(message.encode())
            my_socket.close()
            break
        send_message_to_server(my_socket, message + '#' + str(port))
        print(get_server_response(my_socket))
        my_socket.close()
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


if __name__ == '__main__':
    main()
