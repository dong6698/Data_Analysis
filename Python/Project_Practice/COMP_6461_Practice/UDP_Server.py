from socket import *

# Set up the server information and bind the server
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('127.0.0.1', serverPort))

print("The server is ready to receive")

# While loop will keep receive the message upper them then resend back to client
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode('utf-8').upper().encode('utf-8')
    serverSocket.sendto(modifiedMessage, clientAddress)
