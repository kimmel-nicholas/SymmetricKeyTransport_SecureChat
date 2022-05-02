#Server side
#
#Server runs continuously. When a client connects, RSA key pair is created by the server.
#The server sends the public RSA key to the client. The client creates and AES key and encrypts
#it using RSA and sends it to the server. The server decrypts the AES key using the RSA private
#key. From there, the server and client have private communication through a chat where
#messages are encrypted using the shared AES key.
#
import socket
import rsa
import time
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


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
    print("Waiting for connection...")
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

    # Get and send e
    e = server_pub.e
    e = str(e)
    e = e.encode()
    print("sending e ...")
    clientSocket.send(e)

    # Recieve AES key
    encrypted_AES_Key = clientSocket.recv(1024)
    AES_key = rsa.decrypt(encrypted_AES_Key, server_priv)

    print("\nReceived AES key: ", AES_key)

    # create AES cipher
    cipher = AES.new(AES_key, AES.MODE_ECB)

    # chat between server and client using AES
    # chat continues until either side sends 'bye'
    # server continues running after chat is closed
    print("\nChat opening, waiting for message...\n")
    incoming_mes = ""
    message_to_send = ""
    while True:
        # receive message and decrypt
        incoming_bytes = clientSocket.recv(1024)
        incoming_mes = unpad(cipher.decrypt(incoming_bytes), AES.block_size)
        incoming_mes = incoming_mes.decode()
        print("Message from client: ", incoming_mes)
        if incoming_mes == "bye":
            print("Chat closing")
            break

        # encrypt and send message
        message_to_send = input("Enter a message or \'bye\' to close chat: ")
        message_bytes = message_to_send.encode()
        message_bytes = cipher.encrypt(pad(message_bytes, AES.block_size))
        clientSocket.send(message_bytes)
        print("Message sent", end = "")
        if message_to_send == "bye":
            print("\nChat closing\n")
            break
        print(", waiting for reply...\n")

