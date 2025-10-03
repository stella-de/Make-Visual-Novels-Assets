import json
import socket
import time

IP = "192.168.0.155"  # your iPhone IP
PORT = 21412         # default port, can change
TARGET_PORTS = [11125]  # where your UDP listener is running

msg = {
    "messageType": "iOSTrackingDataRequest",
    "time": 5.0,
    "sentBy": "RenPyPlugin",
    "ports": TARGET_PORTS
}

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    sock.sendto(json.dumps(msg).encode(), (IP, PORT))
    print("Sent tracking request.")
    time.sleep(1)
