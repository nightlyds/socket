import socket

host = "127.0.0.1" # "192.168.0.108" # Server IP
port = 4000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))

print("Server Started")

addrs = {}

def check_for_user(data, addr):
    data = data.decode('utf-8')

    print("Message from: " + addrs.get(addr))
    print("From connected user: " + data)
    print("Sending: " + data)

    data = f"{addrs.get(addr)}: {data}"

    for i in addrs.keys():
        s.sendto(data.encode('utf-8'), i)

while True:
    data, addr = s.recvfrom(1024)

    if addr not in addrs.keys():
        addrs[addr] = data.decode('utf-8')

    check_for_user(data, addr)
