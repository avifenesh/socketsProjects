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
    request_len = str(len(request))
    if len(request_len) <= 9:
        request_len = '0'+request_len
    request_to_send = request_len + request
    my_socket.send(request_to_send.encode())


def handle_server_response(my_socket, request):
    if request != 'SEND_FILE':
        print(my_socket.recv(1024).decode())
    else:
        get_data = True
        image = None
        while get_data:
            i = my_socket.recv(1024)
            if i.encode() == "done":
                get_data = False
                print('saving file end')
                pass
            image += i
            image.save('C:\\Users\\Avi Fenesh\\OneDrive\שולחן העבודה\\networks\\netProjs\\image\\file_got.png')
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
        request = input("Please enter command:\n")
        if valid_request(request):
            send_request_to_server(my_socket, request.encode())
            handle_server_response(my_socket, request)
            if request == 'EXIT':
                done = True
    my_socket.close()


if __name__ == '__main__':
    main()