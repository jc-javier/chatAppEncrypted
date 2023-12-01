# Chat App Encrypted

This is simple a chat application using Python-RSA and PyQT. Initially a console based chat application that 
I converted into a GUI version using PyQT. I then wanted to implement encryption to learn about 
cryptography and this application is the result.

The server can accept and keep track of multiple clients. The server and client each generate 
public and private keys, the server at runtime and the client upon connection, then exchanges 
public keys. This is an asymmetric encryption which means the public keys are used to encrypt 
messages and the private keys to decrypt messages.

To run this application yourself:
- Download all python files into a folder
- Open 2 or more console windows in that folder
- Run server.py in one
- Run main.py in the other(s)
- Enter your name and click connect
- Close chat window to disconnect

Screenshots:

![Screenshot 2023-12-01 151141.png](screenshots%2FScreenshot%202023-12-01%20151141.png)

![Screenshot 2023-12-01 151226.png](screenshots%2FScreenshot%202023-12-01%20151226.png)

![Screenshot 2023-12-01 151945.png](screenshots%2FScreenshot%202023-12-01%20151945.png)