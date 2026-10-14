import socket
print("=== MY SECURITY CHECK ===")
print("Scanning my own phone 127.0.0.1")

for port in [22, 80, 443, 8080, 8000]:
    s = socket.socket()
    s.settimeout(0.5)
    result = s.connect_ex(("127.0.0.1", port))
    if result == 0:
        print(f"Port {port} is OPEN")
    else:
        print(f"Port {port} is closed - secure!")
    s.close()

print("Done! All closed = you are safe")

