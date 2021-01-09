import socket
import threading

HEADER=64
PORT=5050
SERVER=socket.gethostbyname(socket.gethostname())
ADDR=(SERVER,PORT)
FORMAT='utf-8'
DISSCONECT_MESSAGE ="Disconnect"

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn,addr):
    print("[NEW CONNECTION]", addr,"connected")

    connected=True
    while connected:
        msg=conn.recv(32).decode(FORMAT)
        if msg==DISSCONECT_MESSAGE:
            connected = False

        print(addr,msg)
        conn.send("Msg recievd".encode(FORMAT))    
    conn.close()

def start():
    server.listen()
    print("LISTENING Server is listening on",SERVER)
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print("[ACTIVE CONNECTIONS]",threading.activeCount() - 1)

print("[STARTING] server is starting...")
start()