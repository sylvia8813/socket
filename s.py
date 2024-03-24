import socket
import threading


host='127.0.0.1'
port=5050
addr = (host, port)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # 使用IPv4, TCP協定
server.bind(addr) 
server.listen()

clients=[]
names=[]

def broadCast(msg):
    for client in clients:
        client.send(msg)
        
def handle(client):
    connected = True
    while connected:
        try:
            msg = client.recv(1024)
            broadCast(msg)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            name = names[index]
            broadCast(f'{name} left this group '.encode('utf-8'))
            names.remove(name)
            break
        
def receive():
    while True:
        conn, addr = server.accept() #等待新連線，並儲存他資料，傳送連線到handleClient()
        print(f'Server cennected by {str(addr)}')  
        conn.send('Sylvia'.encode('utf-8'))
        name = conn.recv(1024).decode('utf-8')
        names.append(name)
        clients.append(conn)
        print(f'Name of user is {name}')
        broadCast(f'{name} joined'.encode('utf-8'))
        conn.send(f'Connected to the server!'.encode('utf-8'))
        thread = threading.Thread(target = handle, args = (conn, ))
        thread.start()
        print(f'Active connection: {len(clients)}') 
        
receive()