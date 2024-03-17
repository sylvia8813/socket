import socket, random
from connectDB import *

host=socket.gethostbyname(socket.gethostname())
port=5050
addr = (host, port)
DISCONNECT_MESSAGE = 'quit'
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

''' 等取資料庫欄位內容--取得使用者性別'''
def getGender():
    global user
    user = ["female", "male"]
    return random.choice(user)



def clientStart():
    try:
        client.connect(addr)
    
        while True:
            data = getGender()
            print(data)
            client.sendall(data.encode('utf-8'))
            msg = client.recv(1024)
            print('receive from socket:\n', msg.decode('utf-8'))
            
    except socket.error as err:
        print(err)
    finally:
        client.close()

clientStart()
client.close()