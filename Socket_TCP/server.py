import socket

s = socket.socket()
print("socket created ")


s.bind(('localhost', 9999))
s.listen(3) # means 3 clients can connect
print("waiting for client")
while True:
    c, addr = s.accept()
    print("connected to ", addr)
    c.send(bytes("Hi Varun!!",'utf-8'))
    c.close()

    