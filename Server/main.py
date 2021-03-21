import cv2
import time
import pickle
import socket
import struct

# Socket Create
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print('HOST IP:', host_ip)
port = 9999
socket_address = (host_ip, port)

# Socket Bind
server_socket.bind(socket_address)

# Socket Listen
server_socket.listen(5)
print("LISTENING AT:", socket_address)

data = b""
payload_size = struct.calcsize("Q")
while True:
    client_socket, addr = server_socket.accept()
    print('GOT CONNECTION FROM:', addr)
    while True:

        while len(data) < payload_size:
            packet = client_socket.recv(4 * 1024)  # 4K
            # print(packet)
            if not packet:
                break
            data += packet
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("Q", packed_msg_size)[0]

        while len(data) < msg_size:
            data += client_socket.recv(4 * 1024)
        frame_data = data[:msg_size]
        data = data[msg_size:]
        frame = pickle.loads(frame_data)
        cv2.imshow("RECEIVING VIDEO", frame)
        key = cv2.waitKey(1) & 0xFF
        output = str(time.time)
        client_socket.sendall(output.encode('utf-8'))
        if key == ord('q'):
            break
client_socket.close()


# Socket Accept
"""while True:
    client_socket, addr = server_socket.accept()
    print('GOT CONNECTION FROM:', addr)
    if client_socket:
        vid = cv2.VideoCapture(0)

        while vid.isOpened():
            print(1)
            img, frame = vid.read()
            print(2)
            frame = imutils.resize(frame, width=320)
            print(3)
            a = pickle.dumps(frame)
            print(4)
            message = struct.pack("Q", len(a)) + a
            print(5)
            client_socket.sendall(message)

            cv2.imshow('TRANSMITTING VIDEO', frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                client_socket.close()
            break"""

