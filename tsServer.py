import socket
from select import select 
from time  import ctime
from sys import exit

if __name__ == '__main__':

    HOST = ''
    PORT = 5000
    ADDR = (HOST, PORT)
    bSize = 1024

    chatServer = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    chatServer.bind(ADDR)
    chatServer.listen(5)

    connections = [chatServer]
    
    def broadcast(sender, data):
        for sock in connections:
            if sock != sender and sock != chatServer:
                sock.send(data.encode())
            

    print ('Chat server started on port ', PORT)

    while True:
        ready_to_read, ready_to_write, in_error = select(connections,[],[])
        
        for sock in ready_to_read:
            if sock == chatServer:
                client, cAddr = chatServer.accept()
                print ('Client connected from: ', cAddr)
                connections.append(client)
            else:
                msg = sock.recv(bSize).decode()
                if not msg or msg == '&quit':
                    broadcast(sock, str(sock.getpeername()) + ' disconnected')
                    print (str(sock.getpeername()) + ' disconnected')
                    connections.remove(sock)
                    sock.close()
                elif msg=='&shutdown':
                    for s in connections:
                        s.close()
                    print ('Shutting down')
                    exit()
                    
                else:
                    broadcast(sock, str(sock.getpeername()) + ' on ' + ctime() + ': ' + msg)