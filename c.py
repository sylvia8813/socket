import socket
from threading import Thread

name = input('Type ur name here: ')
host='127.0.0.1'
port=5050
addr = (host, port)
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(addr)

def receive():
    while True:
        try:
            msg = client.recv(1024).decode('utf-8')
            if msg == 'Sylvia':
                client.send(name.encode('utf-8'))
            else:
                print(msg)
        except:
            print('Error :(')
            client.close()
            break
        
def write():
    while True:
        msg = f'{name}: {input("")}'
        client.send(msg.encode('utf-8'))
        

receive_thread = Thread(target = receive)
receive_thread.start()
write_thread = Thread(target=write)
write_thread.start()
