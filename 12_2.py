import socket
from urllib.parse import urlsplit

url = urlsplit(input("Enter a URL: ").strip())
count = 0
host = url.hostname
path = url.path
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    print(f'Connecting to {host} and fetching {path}')
    s.connect((host, 80))
    cmd = f'GET {path} HTTP/1.1\nHost: {host}\n\n'.encode('utf-8')
    s.send(cmd)
except:
    print("Enter a valid URl")
    exit()

while True:
    data = s.recv(512)
    count += len(data)
    if len(data) < 1:
        break
    print(data.decode())

s.close()