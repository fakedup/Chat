import socket
#from time  import ctime
import sys
import os
from select import select

if __name__ == '__main__':
    #Подключение к удаленному серверу и создание локального сервера для многопоточности
    if len(sys.argv) == 3:
      
        tempLocalServ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tempLocalServ.bind(('localhost', 6000))
        tempLocalServ.listen(1)
        
        #Запуск в отдельном окне локального клиента для ввода сообщений
        os.system('start python tsClient.py ioClient')
        
        while True:
            
            inputClientSocket, inputAddr = tempLocalServ.accept()
                        
            if inputClientSocket:
                print ('input process accepted')
                tempLocalServ.close()
                break
            
            
        gHOST = sys.argv[1]
        gPORT = int(sys.argv[2])
        gADDR = (gHOST, gPORT)
        bSize = 1024
        
        gChangeSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        gChangeSocket.connect(gADDR)
        
        print ('Connected to: ', gADDR)
        
        while True:
            ready_to_read, ready_to_write, in_error = select([gChangeSocket, inputClientSocket], [],[])
            for sock in ready_to_read:
                if sock == gChangeSocket:
                    rmsg = gChangeSocket.recv(bSize)
                    if rmsg: print (rmsg.decode())
                if sock == inputClientSocket:
                    smsg = inputClientSocket.recv(bSize)
                    if smsg:
                        print (smsg.decode())
                        gChangeSocket.send(smsg)
            
    elif (len(sys.argv) == 2 and sys.argv[1]=='ioClient'):
        '''Если процесс запускался изнутри, он становится внутренним клиентом для ввода'''
        print ('Input client started')
        inputProcessSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        inputProcessSocket.connect(('localhost', 6000))
        
        while True:
            smsg = input('> ').encode()
            inputProcessSocket.send(smsg)
        
        
    else:
        print ('Usage: python tsClient.py hostname port') 
        sys.exit()
