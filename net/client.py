import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
sock.connect(server_address)

try:
	sock.sendall(bytes("asdfg", 'utf-8'))
finally:
	sock.close()