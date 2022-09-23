import socket
import sys

try:
    s = socket.socket()
    print("socket successfully created")
except socket.error as e:
    print("socket creation failed with error %s" %(e))

#port = 80
port = 3000

try:
    host = socket.gethostname()
except socket.error as e:
    print('error getting host: %s' %(e))
    sys.exit()

s.connect((host, port))

print("socket successfully connected")

msgtxt = "hello from py"
msg = msgtxt + " ;"
s.send(msg.encode('utf-8'))

