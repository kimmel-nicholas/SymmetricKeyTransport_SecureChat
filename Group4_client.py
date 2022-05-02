#Client side
#
#The server runs continuously waiting for a connection. When a client connects, an RSA key pair
#is created by the server. The server sends the public RSA key to the client. The client
#creates an AES key and encrypts it using RSA and sends it to the server. The server
#decrypts the AES key using the RSA private key. From there, the server and client have
#private communication through a chat where messages are encrypted using the shared AES key.
#
import socket
import rsa
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


# create a socket object
connectionSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()
# This port is where the server is listening
port = 7777

# connect to hostname on the port. Note that (host,port) is a tuple.
connectionSocket.connect((host, port))
print("Connected to server")

print("Server public key: ")
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

# Sends AES key encrypted with RSA
connectionSocket.send(encrypted_key)

# create AES cipher
cipher = AES.new(key, AES.MODE_ECB)

# chat between server and client using AES
# chat continues until either side sends 'bye'
print("\nChat opening...")
message_to_send = ""
incoming_mes = ""
while True:
    # encrypt and send message
    message_to_send = input("Enter a message or \'bye\' to close chat: ")
    message_bytes = message_to_send.encode()
    message_bytes = cipher.encrypt(pad(message_bytes, AES.block_size))
    connectionSocket.send(message_bytes)
    print("Message sent", end = "")
    if message_to_send == "bye":
        print("\nChat closing")
        break
    print(", waiting for reply...\n")

    # receive message and decrypt
    incoming_bytes = connectionSocket.recv(1024)
    incoming_mes = unpad(cipher.decrypt(incoming_bytes), AES.block_size)
    incoming_mes = incoming_mes.decode()
    print("Message from server: ", incoming_mes)
    if incoming_mes == "bye":
        print("Chat closing\n")
        break




