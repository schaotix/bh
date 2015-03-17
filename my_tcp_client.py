import socket

target_host = input('Enter site: ')
target_port = int(input('Enter port: '))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host, target_port))

client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n".encode('utf-8'))

response = client.recv(4096)

print(response)
