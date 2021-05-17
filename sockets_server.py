import socket
import asyncio

host = "192.168.0.108" # Server IP
port = 4000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))

print("Server Started")

addrs = []

async def check_for_user(data, addr):
    addrs.append(addr)
    data = data.decode('utf-8')

    print("Message from: " + str(addr))
    print("From connected user: " + data)
    data = data.upper()
    print("Sending: " + data)

    for i in addrs:
        task = asyncio.Task(s.sendto(data.encode('utf-8'), i))
        await task

while True:
    data, addr = s.recvfrom(1024)
    print(s.family)
    check_for_user(data, addr)
