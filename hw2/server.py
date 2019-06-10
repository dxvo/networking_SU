
#import socket module

from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
#Fill in start

host = '172.25.143.121'
# print(host)
serverPort = 6787
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind((host,serverPort))
serverSocket.listen(1)

#Fill in end
while True:
    #Establish the connection
    print ('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        f.close()
        #Send one HTTP header line into socket
        #connectionSocket.send("<html><head></head><body><h1>Hello World</h1></body></html>\r\n")
        connectionSocket.send('\nHTTP/1.1 200 OK\n\n')

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        #Fill in start
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n")
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n")
        connectionSocket.close()
        #Fill in end
serverSocket.close()