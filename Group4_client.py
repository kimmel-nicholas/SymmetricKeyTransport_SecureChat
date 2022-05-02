import socket

import Cryptodome
import rsa
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


# create a socket object
connectionSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()
# This port is where the server is listening
port = 7777

# connect to hostname on the port. Note that (host,port) is a tuple.
connectionSocket.connect((host, port))
# Receive  the message from the server (receive no more than 1024 bytes)
n = connectionSocket.recv(1024)
n = n.decode()
n = int(n)
print("n: ", n)

e = connectionSocket.recv(1024)
e = e.decode()
e = int(e)
print("e: ", e)

public_Key = rsa.PublicKey(n, e)

# generate AES key
key = get_random_bytes(16)

encrypted_key = rsa.encrypt(key, public_Key)

connectionSocket.send(encrypted_key)



