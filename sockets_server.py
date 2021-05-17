import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.0.108', 55555))
s.listen()

while True:
    client, address = s.accept()
    print("Connected: {}".format(address))
    client.send("You are connected!".encode())
    client.close()
