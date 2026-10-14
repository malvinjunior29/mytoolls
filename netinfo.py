import socket

print("=== MY NETWORK INFO ===")

# Get my hostname
hostname = socket.gethostname()
print(f"Device: {hostname}")

# Get my IP on this WiFi (like 10.201.126.246)
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    my_ip = s.getsockname()[0]
    s.close()
    print(f"My IP on this WiFi: {my_ip}")
    print(f"Gateway is usually.241 like you saw")
except:
    print("Not connected to WiFi, using 127.0.0.1")
    my_ip = "127.0.0.1"

# Test if we are secure on this WiFi IP too
print(f"\nChecking if {my_ip} is secure...")
for port in [22, 80, 443]:
    sock = socket.socket()
    sock.settimeout(0.5)
    r = sock.connect_ex((my_ip, port))
    if r == 0:
        print(f"Port {port} OPEN on WiFi")
    else:
        print(f"Port {port} closed - safe on WiFi")
    sock.close()

print("\nTOOL 2 DONE")

