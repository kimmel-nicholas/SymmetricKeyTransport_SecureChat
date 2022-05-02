import socket
import rsa
import time


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

clientSocket, addr_port = serverSocket.accept()

# Print the address and port of the client
# addr_port is a tuple that contains both the address and the port number
print("Got a connection from " + str(addr_port))

# Generate and send RSA Key pair
server_pub, server_priv = rsa.newkeys(512)

# Get and send n
n = server_pub.n
n = str(n)
n = n.encode()
print("sending n ...")
clientSocket.send(n)
time.sleep(1)

#Get and send e
e = server_pub.e
e = str(e)
e = e.encode()
print("sending e ...")
clientSocket.send(e)

#Recieve
encrypted_AES_Key = clientSocket.recv(1024)

AES_key = rsa.decrypt(encrypted_AES_Key, server_priv)

print(AES_key)
