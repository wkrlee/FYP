import RPi.GPIO as GPIO
import time
import motor
from motor import DRV8825
import socket


hostname = socket.gethostname()
print("Hostname = ", hostname)
IP = socket.gethostbyname(hostname)
print("IP address = ", IP)
"""
s = socket.socket()
#host = '192.168.0.117'
#host = '192.168.242.180'
#host = '192.168.242.233'S
host = '192.168.0.118'H

port = 12349

s.connect((host, port))
"""
i=0
j=0
while (i<1000):
    """
    print(s.recv(1024))
    direction_input= s.recv(1024)
    s.close()
    """
    j=0
    print(j)
    
    #if __name__ == "__main__":
    while (j<1):
        #direction_input = 'w'
        s = socket.socket()
        #host = '192.168.0.117'
        #host = '192.168.242.180'
        host = '192.168.1.104'
        port = 12349

        s.connect((host, port))
        i+=1
        j+=1
        #print(s.recv(1024))
        #direction_input= s.recv(1024)
        print(s.recv(1024))
        motor.control(s.recv(1024))
        #s.close()
        print(i)
        print(j)
    #time.sleep(1) 
