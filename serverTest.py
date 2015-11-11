import socket
import threading

HOST = '127.0.0.1'
PORT = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

conn, addr = s.accept()
print 'Connected by', addr
conn.sendall('connection OK')

def gettingMsg():
    while True:
        data = conn.recv(1024)
        
        if not data:
            break
        else:
            data = data.decode("utf-8","ignore")
            print(data)

	
threading._start_new_thread(gettingMsg,())

while True:
    pass
