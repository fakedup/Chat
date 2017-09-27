import socket
from time  import ctime

if __name__ == '__main__':

    HOST = ''
    PORT = 5000
    ADDR = (HOST, PORT)
    bSize = 1024

    chatServer = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    chatServer.bind(ADDR)
    chatServer.listen(5)

    #connections = []

    exitFlag = False

    print ('Chat server started')

    while not exitFlag:
        client, cAddr = chatServer.accept()
        print ('Client connected from: ', cAddr)

        while True:
            msg = client.recv(bSize).decode()
            if not msg:
                print ('Disconnect client: ', cAddr)
                client.close()
                break
            elif msg=='quit':
                print ('Disconnect client: ', cAddr)
                client.close()
                break
            else:
                print ('Server on ' + ctime()+ ': ' + msg)

            msg = input('>')
            if not msg:
                print ('Disconnect client: ', cAddr)
                client.close()
            elif msg=='quit':
                print ('Disconnect client: ', cAddr)
                client.close()
                exitFlag = True
                break
            else:
                msg = msg.encode()
                client.send(msg)

    chatServer.close()
    print ('Chat server shut down')
            

        
