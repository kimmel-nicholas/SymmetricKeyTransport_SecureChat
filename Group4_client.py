# Client program
# Connects to the server at port 7777
# Sends a message to the server, receives a reply and closes the connection
# Use Python 3 to run

import socket
from time import sleep
import rsa

# create a socket object
connectionSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()
# This port is where the server is listening
port = 7777

# connect to hostname on the port. Note that (host,port) is a tuple.
connectionSocket.connect((host, port))
# Receive  the message from the server (receive no more than 1024 bytes)
receivedBytes = connectionSocket.recv(1024)
# Decode the bytes into a string (Do this only for strings, not keys)
n = bytes.decode(receivedBytes)
n = int(n)
# Print the message
print("n value: ", n)

connectionSocket.send('ok'.encode())

receivedBytes = connectionSocket.recv(1024)
e = receivedBytes.decode()
e = int(e)
print("e value:", e)

server_PublicKey = rsa.PublicKey(n, e)

#get user message
user_Input = input("Please enter a message: ")
user_Input = user_Input.encode()

#get message length and send to server as an encrypted string
messageLength = str((len(user_Input)*8)).encode()
messageLength = rsa.encrypt(messageLength, server_PublicKey)
connectionSocket.send(messageLength)


while True:
    try:
        to_Send = rsa.encrypt(user_Input, server_PublicKey)
        connectionSocket.send(to_Send)
        break
    except OverflowError:                                           #when a message is too long to be encrypted, an OverflowError is thrown
        to_Send = rsa.encrypt(user_Input[:52], server_PublicKey)    #encrypts 52 because that is the minimum key size
        user_Input = user_Input[52:]
        connectionSocket.send(to_Send)
    sleep(0.5)                                                      #sleep for 0.5 seconds as to not overload the server

receivedBytes = connectionSocket.recv(1024)
goodbyeMessage = receivedBytes.decode()
print(goodbyeMessage)

# Close the connection
connectionSocket.close()
