from socket import *

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1', 8080))

# 서버와 다른점은, bind, listen, accept가 없고 connect만 추가됐다.
# 127.0.0.1은 자기 자신이라는 의미이다. 따라서 여기서는 자기자긴이 8080 포트로 연결하라는 뜻이다.


print('연결 확인 됐습니다.')
clientSock.send('I am a client'.encode('utf-8'))
# send는 메세지를 보내는 것이다. 이 때 보낼 내용을 send에 넣어주면 된다.
# encode('utf-8')을 포함시켜 문자열을 byte로 인코딩 하지 않으면 오류가 뜬다. 

print('메시지를 전송했습니다.')

data = clientSock.recv(1024)
print('받은 데이터 : ', data.decode('utf-8'))

# recv(1024)는 소켓에서 1024바이트만큼을 가져오겠단 소리입니다. 만일 소켓에 도착한 데이터가 1024바이트보다 많다면, 다시 recv(1024)를 실행할 때 전에 미처 가져오지 못했던 것을 끌어오게 됩니다.
# recv는 메세지가 수실 될 때 까지 대기하는 코드이다.
# 우리는 데이터를 byte로 받아오기 때문에 문자를 읽기 위해서는 decode('utf-8')로 디코드를 꼭 해줘야한다,

# + 소켓에서 주고 받는 것은 데이터기 때문에 문자열을 말고 이미지나 동영상 파일을 byte단위로 전송해도 전송이 가능하다.