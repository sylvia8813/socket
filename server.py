# Python Socket TCP 伺服器
from pair_connect import *
import socket

host=''
port=3000

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # 使用IPv4, TCP協定
server.bind((host, port)) 
server.listen(5)

print('server start at host: %s port: %s' % (host, port))
print('wait for connection...')

while True:
    connect, address = server.accept()
    print("cennected by (= Client address)" + str(address))
    
    if connect.recv(1024).decode('utf-8') == 'exit':
        break
    else:
        
        #接收資料
        getData = connect.recv(1024) #連接字數極限
        print("getData: "+ getData.decode())
        
        #傳送資料
        sentData = getData.decode()
        connect.send(sentData.encode())
    
server.close()