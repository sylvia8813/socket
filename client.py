import socket
# from pairFunc import getGender

host='172.16.15.53'
port=3000
addr = (host, port)
DISCONNECT_MESSAGE = 'quit'
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


def clientStart():
    try:
        client.connect(addr)
        print("input female or male")
        data = str(input())
        # pair = "female" if data == "male" else "male"
        client.sendall(data.encode('utf-8'))
        while True:
            print(f'here')
            msg = client.recv(1024)
            msg = msg.decode('utf-8')
            if msg:
                print(f'receive from socket {msg}')
                break
            else:
                pass
                
            
    except socket.error as err:
        print(err)
    finally:
        client.close()

clientStart()
client.close()
