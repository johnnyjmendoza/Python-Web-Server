#!/usr/bin/env python3
# Johnny Mendoza - JohnnyMendoza@gmail.com
# This python3 program creates a simple web server

import socket

# Connect to port

HOST, PORT = '', 8888

# Open socket connection. AF_INET indicates we are using IPV4

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)

# Display message in Python shell after running program

print("Listening on port %s" % PORT)

# When connection is made, return HTTP response text

while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print (request)

    http_response = (
    """Hello. You are now connected. This is a simple web server
    created with Python 3.""")

    client_connection.sendall(bytes(http_response.encode('utf-8')))
    client_connection.close()
