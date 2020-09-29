# server side
# Avi Fenesh
# mod for python 3, 2020

import glob
import os
import shutil
import socket
import subprocess

import PIL
from PIL import ImageGrab
from PIL import Image

IP = '127.0.0.1'
PORT = 8820
requests = ['TAKE_SCREENSHOT', "SEND_FILE", "DIR", "DELETE", "COPY", "EXECUTE", "EXIT"]


def receive_client_request(client_socket):
    client_message = client_socket.recv(1024).decode()
    split_message = client_message.split('#')
    command = split_message[0]
    if len(split_message) == 2:
        param = split_message[1]
        return command, param
    elif len(split_message) == 3:
        param = [] + split_message[1] + split_message[2]
        return command, param
    return command, None


def check_client_request(command, param=None):
    valid = False
    error_message = ""
    if command not in requests:
        valid = True
        error_message += "command not exist. "
    if param is not None:
        if isinstance(param, str):
            if not os.path.exists(param):
                valid = True
                error_message += "Path not exist."
        else:
            if not (os.path.exists(r'' + param[0]) + os.path.exists(r'' + param[1])):
                valid = True
                error_message += "Path not exist."

    if valid:
        return valid, error_message
    else:
        return valid, None


def take_screenshot():
    im = PIL.ImageGrab.grab()
    im.save('C:\\Users\\Avi Fenesh\\OneDrive\שולחן העבודה\\networks\\netProjs\\image\\screen_shoot.png')


def send_file(client, params):
    o = open(params, "rb")
    data = o.read()
    chunks, chunk_size = len(data), 1024
    for i in range(0, chunks, chunk_size):
        client.send(data[i:i + chunk_size])
    o.close()
    client.send('done'.encode())


def handle_client_request(command, params=None):
        if command == 'TAKE_SCREENSHOT':
            take_screenshot()
            return 'm - screen shoot toked'
        elif command == 'SEND_FILE':
            return params
        elif command == 'DIR':
            files_list = glob.glob(r'' + params + '\*.*')
            return 'm - ' + str(files_list)
        elif command == 'DELETE':
            os.remove(r'' + params)
            return 'm - file has been deleted'
        elif command == 'COPY':
            shutil.copy(r'' + params[0], r'' + params[1])
            return 'm - file copied'
        elif command == 'EXECUTE':
            subprocess.call(r'' + params)
            return 'm - app has ben executed'
        elif command == 'EXIT':
            return 'm - server closed'
        else:
            return 'please send an exist command from the list'


def send_response_to_client(response, client_socket):
    if response[0] == 'm':
        client_socket.send(response.encode())
        client_socket.send('done'.encode())
    else:
        send_file(client_socket, response)


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP, PORT))
    server_socket.listen()
    client_socket, addres = server_socket.accept()
    done = False
    while not done:
        command, params = receive_client_request(client_socket)
        valid, error_message = check_client_request(command, params)
        if not valid:
            response = handle_client_request(command, params)
            send_response_to_client(response, client_socket)
        else:
            send_response_to_client('m - ' + error_message, client_socket)
        if command == 'EXIT':
            done = True

    client_socket.close()
    server_socket.close()


if __name__ == '__main__':
    main()
