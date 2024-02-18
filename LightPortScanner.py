import socket

ip = input("IP you want to scan? \n")

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

for port in range(100):
    try:
        sock.connect_ex((ip,port))
        if sock.connect_ex == 0:
            print('--OPEN-- Port open :',ip,port)
    except:
        print('--CLOSED-- Port Closed :',ip,port)

