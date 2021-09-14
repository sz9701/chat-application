import socket
s=socket.socket()
s.connect(('127.0.0.1',5111))

while True:
    msgc1=s.recv(1024)
    print "[CLIENT-1] >> %s"%msgc1
    msgc2=raw_input("Enter your msg: ")
    s.send(msgc2)
    print "waiting for reply..."
