# Python Socket TCP 伺服器
import socket
import threading


host=socket.gethostbyname(socket.gethostname()) # 確保在自己的IPv4 aAdress底下運行
port=5050
addr = (host, port)
DISCONNECT_MESSAGE = 'quit'

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # 使用IPv4, TCP協定
server.bind(addr) 
server.listen(100) #listens for 100 active connections.
print('Server start at host: %s port: %s \nWaiting for connection...' % (host, port))

 
def handleClient(conn, addr):
    print(f'New thread: {addr} connected.')
    connected = True
    while connected:
        if conn.recv(1024).decode('utf-8') == DISCONNECT_MESSAGE:
            connected == False
            break
        else:
            #接收資料
            getData = conn.recv(1024) #連接字數極限
            print("getData: "+ getData.decode('utf-8'))
            
            #傳送資料
            sentData = getData.decode('utf-8')
            conn.send(sentData.encode('utf-8'))
    conn.close()
    
def serverStart():
    while True:
        conn, addr = server.accept() #等待新連線，並儲存他資料，傳送連線到handleClient()
        print(f'Server cennected by {str(addr)}')  
        
        thread = threading.Thread(target = handleClient, args = (conn, addr))
        thread.start()
        print(f'Active connection: {threading.active_count()-1}') #(Not include server)  
        
serverStart()
server.close()
