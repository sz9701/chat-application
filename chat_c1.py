import socket
s=socket.socket()
s.connect(('127.0.0.1',5111))

while True:
    msgc1=raw_input("Enter your msg: ")
    s.send(msgc1)
    print "Waiting for reply..."
    msgc2=s.recv(1024)
    print "[CLIENT-2] >> %s"%msgc2
