# client side
# Avi Fenesh
# mod for python 3, 2020

import socket

IP = '127.0.0.1'
PORT = 8805


def handle_client_message(client_socket):
    full_message = client_socket.recv(1024).decode().split('#')
    message = full_message[0]
    port = full_message[1]
    return message, port


def send_response_to_client(client_socket):
    client_socket.send("wow, that so interesting".encode())


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = PORT
    while True:
        server_socket.bind((IP, port))
        server_socket.listen()
        client_socket, addres = server_socket.accept()
        message, port = handle_client_message(client_socket)
        port = int(port)
        if message == 'exit':
            server_socket.close()
            break
        send_response_to_client(client_socket)
        server_socket.close()
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


if __name__ == '__main__':
    main()


