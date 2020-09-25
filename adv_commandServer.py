# server side
# Avi Fenesh
# mod for python 3, 2020

from PIL import ImageGrab
import glob
import shutil
import socket
import os
import subprocess

IP = '127.0.0.1'
PORT = 8820
requests = ["TAKE_SCREENSHOT", "SEND_FILE", "DIR", "DELETE", "COPY", "EXECUTE", "EXIT"]

def recive_client_request(client_socket):
    client_message = client_socket.recv(1024).decode()
    split_message = client_message.split()
    command = split_message[0]
    command_len = command[0:2]
    command = command[2:-1]
    if len(split_message) > 1:
        param = split_message[1]
        return command, param
    return command

def check_client_request(command, param=None):
    valid = False
    error_message = ""
    if command not in requests:
        valid = True
        error_message += "command not exist. "
    if param is not None:
        if not os.path.exists(param):
            valid = True
            error_message += "Path not exist."
    if valid:
        return error_message
    else:
        return None

def take_screenshot():
    im = ImageGrab.grab()
    im.save('C:\\Users\\Avi Fenesh\\OneDrive\שולחן העבודה\\networks\\netProjs\\image')

    def send_file(client, params):
        o = open(params, "rb")
        data = o.read()
        chunks, chunk_size = len(data), 1024
        for i in range(0, chunks, chunk_size):
            client.send(data[i:i+chunk_size])
        o.close()
        client.send('done'.encode())


def handle_client_request(client, command, params=None):
    if check_client_request(command, params):
        if command == 'TAKE_SCREENSHOT':
            take_screenshot()
        else:
            if command == SEND_FILE:
                send_file(client, params)




