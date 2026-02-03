import socket

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print(f"\n\nLocal host IP address = {ip_address}\n\n")