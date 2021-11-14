import time
from socket import *
import threading

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1', 8080)) #자기자신에게 8080포트로 연결

print('연결되었습니다.')

def send(sock):
    while True:
        sendData = input('>>>')
        sock.send(sendData.encode('utf-8'))

def receive(sock):
    while True:
        recvData = sock.recv(1024)
        print('상대방 : ', recvData.decode('utf-8'))

sender = threading.Thread(target=send, args=(clientSock,))
receiver = threading.Thread(target=receive, args=(clientSock,))

sender.start()
receiver.start()

while True:
    time.sleep(1)
    pass

'''
msg = "Hello, I'm client"
clientSock.send(msg.encode('utf-8'))
print('메세지 전송완료')

data = clientSock.recv(1024)
print('상대에게 온 메세지 : ', data.decode('utf-8'))
'''