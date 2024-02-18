import socket

ip = input("IP you want to scan? \n")

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

for port in range(100):
    try:
        sock.bind((ip,port))
        if sock.bind:
            print('--OPEN-- Port open :',ip,port)
    except:
        print('--CLOSED-- Port Closed :',ip,port)

