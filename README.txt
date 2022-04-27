Task 3: Symmetric Key Transport and Secure Chat


In this last part of the project, you will implement a secure chat program between a client and a server program. The application will be closer to how the key exchange works in practice. You will build on your work in the second part of the project where you learned how RSA works. You will also use the AES key generation step from your work in the first step of the project. Here are the expectations in the project:

1. The server generates an RSA key pair.
2. Server sends the public key to the client. 
3. The client receives the public key from the server.
4. The client generates an AES key.
5. Client encrypts the AES key with the server's public key.
6. Clients sends the encrypted AES key to the server.
7. The server receives the encrypted AES key from the server
8. The server decrypts it. (using which key?)
9. At this point the client and the server share a (AES) key that no one knows. They can use this key for secure (encrypted)  communication.



In the rest of the project, the following steps are repeated until the user on the client  side enters "Bye". 

1. The client gets an input from the user. 
2. The client encrypts the user input using the AES key.
3. The client sends the encrypted message to the server.
4. The server receives the encrypted message.
5. The server decrypts the message. (using which key?)
6. The server displays the plain message on the screen.
7. The server gets an input from the user.
8. The server encrypts the user input using the AES key.
9. The server sends the encrypted message to the client.
10. The client receives the encrypted message.
11. The client decrypts the message. (using which key?)
12. The client displays the plain message on the screen.
13. The client gets an input from the user.
14. Submit only your well documented source code (.java and .py files) along with a Word document, that includes 



a screenshot of the server and the client's  communication with graceful ending.
a screenshot of the server and client when a very long message is entered on the client side.
a statement on group work: How did the group members contribute to the project? Did everyone do their fair share of the work?
the challenges you have faced with when completing this part of the assignment (other than arranging meeting times with the group members or other challenges about working in a group).
how is the assignment helpful in for you in understanding cryptographic algorithms?
any other comments/suggestions.
