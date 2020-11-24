from socket import *

serverSock = socket(AF_INET, SOCK_STREAM) # 객체 생성 => 소켓 생성
serverSock.bind(('', 8080)) # bind는 소켓을 만들때 서버에서만 필요하다. client에서는 필요없다. 튜블로 ip와 port 가 들어간다. 
#  8080번 포트에서 모든 인터페이스에게 연결하도록 한다
serverSock.listen(1) # 서버만 필요. 몇 개의 동시 접속을 허용하는지를 알려준다. 

############# 여기까지하면 서버는 접속이 올 때까지 기다린다. 그 다음 단계는 접속을 수락 후에 통신을 주고 받기위해 아래의 accept를 쓴다

connectionSock, addr = serverSock.accept()
# accecpt는 연결이 되어야 return값을 내보내 준다. return은 새로운 소켓과 상대방 주소를 준다.
# 상대방 주소를 받았기 때문에 위의 serverSock은 이용하지 않고 주고 connectionSock를 이용한다.

print(str(addr),'에서 접속이 확인되었습니다.')

data = connectionSock.recv(1024)
print('받은 데이터 : ', data.decode('utf-8'))

connectionSock.send('I am a server.'.encode('utf-8'))
print('메시지를 보냈습니다.')