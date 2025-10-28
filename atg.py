import socket
import socket

def tls350(host, port=10001):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10)
    sock.connect((host, port))
    
    # REAL TLS-350: Ctrl+A (0x01) + command
    commands = [
    b"\x01EGTG\r",           # **System Log**
]
    
    for cmd in commands:
        print(f"\n=== Sending: {cmd!r} ===")
        sock.sendall(cmd )
        try:
            resp = sock.recv(4096)
            print(f"RECV ({len(resp)} bytes): {resp!r}")
            print(f"ASCII: {resp.decode('ascii', errors='ignore')}")
            # Show hex breakdown
            print("HEX: ", ' '.join(f'{b:02X}' for b in resp))
        except:
            print("TIMEOUT")
    
    sock.close()



HOST = "71.58.134.154"  # Replace with target IP (e.g., a test GasPot instance)
response = tls350(HOST)
print("\nResponse:\n")
print(response)
