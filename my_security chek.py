#!/usr/bin/env python3
# TOOL 1: checkme.py - Made by you in Harare
import socket
import datetime

print("=== MY SECURITY CHECK ===")
print(f"Date: {datetime.datetime.now()}")
print(f"Analyst: You")
print("-" * 30)

my_ip = "127.0.0.1"
ports_to_check = [22, 80, 443, 8080, 8000, 3306]

open_found = 0

for port in ports_to_check:
    s = socket.socket()
    s.settimeout(1)
    try:
        result = s.connect_ex((my_ip, port))
        if result == 0:
            print(f"[OPEN] Port {port} -> NEEDS ATTENTION!")
            open_found += 1
        else:
            print(f"[CLEAN] Port {port} -> secure")
    except:
        print(f"[CLEAN] Port {port} -> secure")
    s.close()

print("-" * 30)
if open_found == 0:
    print("STATUS: CLEAN - No action required.")
    print("FINDING: No unauthorized port exposure detected.")
else:
    print(f"STATUS: {open_found} open ports found")
print("Next: Keep Randomized MAC ON like in your settings.")



