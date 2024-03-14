import socket, random
from pair_connect import *


host='127.0.0.1'
port=3000
server = socket.socket()


try:
    server.connect((host, port))
    while True:
        data = input()
        server.sendall(data.encode('utf-8'))
        data = server.recv(1024)
        print('receive from server:\n', data.decode('utf-8'))
        data = input('leave a msg here:\n')
except socket.error as err:
    print(err)
finally:
    server.close()


#取得使用者性別
def getGender(_):
    user = ["female", "male"]
    return random.choice(user)

print(getGender())

client_connect(server, male)