from socket import *

# First set up the IP and Port Number
serverName = '127.0.0.1'
serverPort = 12000

# Creates the client socket. AF_INET mean IPv4, SOCK_DGRAM mean UDP rather than TCP
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Collect the message from user input.
message = input('Input lowercase sentence:').encode('utf-8')

# Here is a tuple includes the information of Server, then send message to that server
serverInfo = (serverName, serverPort)
clientSocket.sendto(message, serverInfo)

# 2048 mean buffer size, modifiedMessage will receive the message from server,
# and the server info will stored into serverAddress
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

# print the modifiedMessage from server
print(modifiedMessage.decode('utf-8'))

# Close the Socket
clientSocket.close()
