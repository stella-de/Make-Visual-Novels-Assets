import socket

PORT = 11125  # Choose any free port from your request list
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', PORT))

print(f"Listening for tracking data on UDP port {PORT}...")

while True:
    data, addr = sock.recvfrom(4096)
    print(data)
