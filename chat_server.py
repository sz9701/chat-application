import socket
s=socket.socket()
s.bind(('0.0.0.0',5111))
s.listen(3)
client1,(ip1,port1)=s.accept()
client2,(ip2,port2)=s.accept()

while True:
    msgc1=client1.recv(1024)
    client2.send(msgc1)
    msgc2=client2.recv(1024)
    client1.send(msgc2)
