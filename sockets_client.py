import sys
import getopt
import socket
import threading
import time

host = "192.168.0.104" # Client IP
port = 4001 # By default

opts, args = getopt.getopt(sys.argv[1:], "p:", ["port"])

for opt, arg in opts:
    if opt == "-p":
        port = int(arg)

server = ('192.168.0.108', 4000)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))

def write_message():
    while True:
        message = input("-> ")
        s.sendto(message.encode('utf-8'), server)
        time.sleep(.5)

def get_message():
    while True:
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print("Received from server: " + data)


f1 = threading.Thread(target=write_message)
f2 = threading.Thread(target=get_message, daemon=True)

f1.start()
f2.start()