import sys
import getopt
import socket

host = "192.168.0.104" # Client IP
port = 4001 # By default

opts, args = getopt.getopt(sys.argv[1:], "p:", ["port"])

for opt, arg in opts:
    if opt == "-p":
        port = arg

server = ('192.168.0.108', 4000)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host,port))

message = input("-> ")

while message != "q":
        s.sendto(message.encode('utf-8'), server)
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print("Received from server: " + data)
        message = input("-> ")

s.close()