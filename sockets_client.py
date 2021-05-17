import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.0.108', 5555))
message = s.recv(1024)
s.close()

print(message.decode())
