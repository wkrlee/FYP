import socket

s = socket.socket()
host = '192.168.1.102'
port = 12345
s.bind((host,port))

s.listen(5)
while True:
    c, addr = s.accept()
    print('addr = ', addr)
    output = 'Thnak you for conecting'
    c.sendall(output.encode('utf-8'))
    c.close()
