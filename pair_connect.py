# Socket TCP
import threading, socket
from client import *
from server import *

host='localhost'
port=3000


# 配對邏輯
def client_connect(client_socket, gender):
   
    global males, females
    males = []
    females = []
   

    try:
        while True:
            # get client data
            request = client_socket.recv(1024)
            if not request:
                break
            
            #配對方法
            if gender=='male':
                if females: 
                    female = females.pop(0)
                    client_socket.send(female.encode())
                else:
                    client_socket.send("No female users available for pairing.".encode())
            elif gender == 'female':
                if males:
                    male =males.pop(0)
                    client_socket.send(male.encode(0))
                else:
                    client_socket.send("No male users available for pairing.".encode())
                    
    except Exception as e:
        print(f'error:{e}')
        
    finally:
        client_socket.close()
        
# server listen client
def server_connect():
    global server, males, females
    
    server.listen(10)
    print("Server started. Waiting for connections...")
    
    try:
        while True:
            client_socket, address = server.accept()
            gender = client_socket.recv(1024).decode('utf-8')
            if gender == 'male':
                males.append(client_socket)
            elif gender == 'female':
                females.append(client_socket)
            client_handler = threading.Thread(target=client_connect, args=(client_socket, gender))
            client_handler.start()
            
            
    except Exception as e:
        print(f"error: {e}")
        
    finally:
        server.close()
        
        
if __name__ == "__main__":
    server_connect()