#!/usr/bin/python

import socket

HOST = socket.gethostname()
PORT = 1464
s = socket.socket()

s.connect((HOST, PORT))

answer = s.recv(1024)
print answer

s.close()

