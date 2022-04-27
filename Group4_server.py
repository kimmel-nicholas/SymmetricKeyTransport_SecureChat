# Server program
# Listens at port 7777
# Receives the client's message and replies to it and closes the connection
# Continues listening
# Use Python 3 to run

import socket
import rsa


global public_Key, private_Key

#create rsa public and private keys
public_Key, private_Key = rsa.newkeys(512)

# create a socket object that will listen
serverSocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)
# get local machine name
host = socket.gethostname()
# the socket will listen at port 7777
port = 7777

# bind the socket to the port
serverSocket.bind((host, port))

# start listening for requests
serverSocket.listen()

while True:
    print("Waiting for connection.....")
    # serverSocket accepts if there is a connection request
    # (note that serverSocket is listening).
    # Communictaion will be via the clientSocket
    clientSocket, addr_port = serverSocket.accept()

    # Print the address and port of the client
    # addr_port is a tuple that contains both the address and the port number
    print("Got a connection from " + str(addr_port))


    #Send public key n
    print(public_Key)
    n = public_Key.n
    print("sending n..")
    n = str(n)
    n = n.encode()
    clientSocket.send(n)

    ok = clientSocket.recv(1024)

    #send Public key e
    e = public_Key.e
    print("sending e..")
    e = str(e)
    e = e.encode()
    clientSocket.send(e)

    #get length of message - to handle long messages
    receivedBytes = clientSocket.recv(1024)
    messageLength = int(rsa.decrypt(receivedBytes, private_Key).decode())

    amountReceived = 0
    print("Decrypted message from client: ")
    while amountReceived < messageLength:
        receivedBytes = clientSocket.recv(1024)
        mes = len(receivedBytes)
        amountReceived += 52*8
        print(rsa.decrypt(receivedBytes, private_Key).decode())

    #Final message to client
    clientSocket.send("MESSAGE RECEIVED. Goodbye".encode())
