import time
from socket import *
import threading

#소켓의 객체 생성, AF_INET:어드레스패밀리/SOCK_STREAM:소켓타입 (거의 고정)
## AF(address family) : 주소체계, 현시대에는 인터넷 통신이 대부분 > IP, AF_INET > IPv4
serverSock = socket(AF_INET, SOCK_STREAM)

#생성된 소켓에 실제 AF를 연결(서버에만 필요)
#서버가 소켓을 포트에 맵핑하는 행위를 바인딩 bind(ip,port), ip가 빈값일 경우 모든 인터페이스에 연결
port = 8080
serverSock.bind(('', 8080)) #8080 포트에서 모든 인터페이스(소켓)에게 연결
serverSock.listen(1) #상대방의 접속을 기다림

print('%d번 포트로 접속 대기중...'%port)

#accept는 누군가 접속 시 return됨
connectionSock, addr = serverSock.accept()
print(str(addr),'에서 접속하였습니다.')

def send(sock):
    while True:
        sendData = input('>>>')
        sock.send(sendData.encode('utf-8'))

def receive(sock):
    while True:
        recvData = sock.recv(1024)
        print('상대방 : ', recvData.decode('utf-8'))

# target : 스레드 실행함수, args : 함수에 전달할 인자자 > (var,)로 입력해야 튜플로 인지
sender = threading.Thread(target=send, args=(connectionSock,))
receiver = threading.Thread(target=receive, args=(connectionSock,))

sender.start()
receiver.start(),

while True:
    time.sleep(1)
    pass

'''
data = connectionSock.recv(1024) #수신할 바이트크기, 수신이 올 때 까지 대기함
print('상대로 부터 온 메세지 : ',data.decode('utf-8'))

msg = "Hello, I'm Server"
connectionSock.send(msg.encode('utf-8')) #클라이언트 접속 시 데이터 보냄
print("메세지 전송완료")
'''
