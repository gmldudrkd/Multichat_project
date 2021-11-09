from socket import *

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1', 8080)) #자기자신에게 8080포트로 연결

print('연결되었습니다.')

msg = "Hello, I'm client"
clientSock.send(msg.encode('utf-8'))
print('메세지 전송완료')

data = clientSock.recv(1024)
print('상대에게 온 메세지 : ', data.decode('utf-8'))