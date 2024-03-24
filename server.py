# Python Socket TCP 伺服器
import socket
import threading
# from pairFunc import *


host=socket.gethostbyname(socket.gethostname()) # 確保在自己的IPv4 aAdress底下運行
port=5050
addr = (host, port)
DISCONNECT_MESSAGE = 'quit'

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # 使用IPv4, TCP協定
server.bind(addr) 
server.listen(100) #listens for 100 active connections.
print('Server start at host: %s port: %s \nWaiting for connection...' % (host, port))

global males, females
males = []
females = []
lock = threading.Lock() 
clients = []
'''
def getDBGender:
    // 增加資料庫連接設置
    return gender
'''    
 
def handleClient(conn, addr):
    print(f'New thread: {addr} connected.')
    try:
        gender = conn.recv(1024).decode('utf-8') 
        print(f"Client {addr} is a {gender}")
        
        if gender == 'male':
            males.append(conn)
        elif gender == 'female':
            females.append(conn)
        print('male:')
        for male in males:
            print(male)
        print('female:')
        for female in females:
            print(female)
        
        if len(females)>0 and len(males)>0:
            if gender == 'male':
                pairedF = females[0]
                if pairedF.fileno() != -1:
                    
                    server.sendall((f'paired with a {pairedF}').encode('utf-8'))
                    females.pop(0)
            else:
                pairedM = males[0]
                server.sendall((f'paired with a {pairedM}').encode('utf-8'))
                males.pop(0)
        else:
            print("No available pair for", addr)
            
    except Exception as e:
        print(f"Error handling client {addr}: {e}")
    finally:
        conn.close()
    
def serverStart():
    while True:
        conn, addr = server.accept() #等待新連線，並儲存他資料，傳送連線到handleClient()
        print(f'Server cennected by {str(addr)}')  
        clients.append(conn)
        thread = threading.Thread(target = handleClient, args = (conn, addr))
        thread.start()
        print(f'Active connection: {len(clients)}') #(Not include server) #threading.active_count()  
        
serverStart()
server.close()
