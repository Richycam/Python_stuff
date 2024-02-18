import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
target = input('IP to Scan: \n ')
target_ip = socket.gethostbyname(target)
print('SCANNING:', target_ip)

def port_scan(port):
    try:
        sock.connect((target_ip, port))
        return True
    except:
        return False

start = time.time()
for port in range(5000): 
    if port_scan(port):
        print(f'Port {port} is open')
    else:
        print(f'Port {port} is closed')

end = time.time()
print(f'Time taken: {end - start:.2f} seconds')
