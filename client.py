import socket
# from pairFunc import getGender

host='172.16.14.184'
port=5050
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
        data = client.recv(1024)
        msg = data.decode('utf-8')
        print(f'receive from socket {msg}')
            
    except socket.error as err:
        print(err)
    # finally:
        # client.close()

clientStart()
# client.close()
