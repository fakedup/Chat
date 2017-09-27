import socket
from time  import ctime

HOST = '192.168.1.33'
PORT = 5000
ADDR = (HOST, PORT)
bSize = 1024

chatClient = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
chatClient.connect(ADDR)

print ('Connected to: ', ADDR)

exitFlag = False

while not exitFlag:
    msg = input ('> ')
    if msg == 'quit':
        break
    else:
        print ('You on ' + ctime() + ': ' + msg)
        msg = msg.encode()
        chatClient.send(msg)

    msg = chatClient.recv(bSize).decode()
    if not msg:
        break
    else:
        print ('Server on ' + ctime() + ': ' + msg)

print ('Disconnected from server')
chatClient.close()
