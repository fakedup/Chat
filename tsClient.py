import socket
import sys
from select import select
from threading import Thread

def msgRecv(ChangeSocket, size):
    while True:
        ready_to_read, ready_to_write, in_error = select([ChangeSocket], [],[])
        for sock in ready_to_read:
            msg = sock.recv(size)
            if msg: print (msg.decode())

if __name__ == '__main__':
    #Проверка параметров запуска и подключение к удаленному серверу
    if len(sys.argv) == 3:
        
        gHOST = sys.argv[1]
        gPORT = int(sys.argv[2])
        gADDR = (gHOST, gPORT)
        bSize = 1024
        
        gChangeSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        gChangeSocket.connect(gADDR)

        print ('Connected to: ', gADDR)
        
        #Создание потока для приема и вывода сообщений
        
        t = Thread(target=msgRecv, args=(gChangeSocket, bSize))
        t.start()
        

        while True:
            smsg = input('> ').encode()
            gChangeSocket.send(smsg)
        
        
    else:
        print ('Usage: python tsClient.py hostname port') 
        sys.exit()
