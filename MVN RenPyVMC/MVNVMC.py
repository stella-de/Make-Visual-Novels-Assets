import socket

UDP_PORT = 11125  # One of the ports you'll request from the iPhone
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", UDP_PORT))

print(f"Listening on UDP port {UDP_PORT}")

while True:
    data, addr = sock.recvfrom(4096)
    print(f"From {addr}: {len(data)} bytes")
    # You'll decode `data` next
