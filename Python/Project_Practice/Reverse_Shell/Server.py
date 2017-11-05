import socket
import sys


# create socket for connection
def socket_create():
    try:
        global host
        global port
        global s
        host = ''
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error: " + str(msg))


# bind socket to port and wait for connection from client
def socket_bind():
    try:
        global host
        global port
        global s
        print("binding socket to port: " + str(port))
        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print("Socket binding error: " + str(msg) + "\n" + "Retrying.....")
        socket_bind()


# Establish a connection with client(socket must listening)
def socket_accept():
    conn, address = s.accept()
    print("Connection has been established | IP: "+ address[0] + "| Port: " + str(address[1]))
    send_commend(conn)
    conn.close()


# sending comments
def send_commend(conn):
    while True:
        cmd = input()
        if cmd == "quit":
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "UTF-8")
            print(client_response, end="")


def main():
    socket_create()
    socket_bind()
    socket_accept()


main()
