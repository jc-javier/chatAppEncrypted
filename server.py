import socket
import threading
import rsa


HOST = '127.0.0.1'
PORT = 1234
listen_limit = 5
active_clients = []

FORMAT = 'utf-8'
public_key, private_key = rsa.newkeys(1024)


# Listen for any upcoming message from client
def listen_for_messages(client, username, public_partner_key):
    while True:
        try:
            response = client.recv(1024)
            message = rsa.decrypt(response, private_key).decode(FORMAT).strip()  # decrypt message with server private key
            # message = client.recv(1024).decode('utf-8')
        except ConnectionResetError:
            continue
        if message == '!disconnect':
            final_msg = f'[SERVER]~{username} has left the chat.'
            try:
                send_messages_to_all(final_msg)
            except ConnectionResetError:
                print(f'{username} disconnected.')
            active_clients.remove((username, client, public_partner_key))
        else:
            final_msg = f'{username}~{message}'
            send_messages_to_all(final_msg)


def send_message_to_client(client, message, public_partner_key):
    client.send(rsa.encrypt(message.encode(FORMAT), public_partner_key))
    # client.send(message.encode())


# Send message to all clients connected
def send_messages_to_all(message):
    for user in active_clients:
        send_message_to_client(user[1], message, user[2])  # send message using each client's respective public key


# Handling client
def client_handler(client, public_partner_key):
    # Server will listen for client message that will contain username
    while True:
        username = rsa.decrypt(client.recv(1024), private_key).decode(FORMAT)
        # username = client.recv(1024).decode('utf-8')
        if username != '':
            active_clients.append((username, client, public_partner_key))
            prompt_message = f'[SERVER]~{username} has entered the chat.'
            send_messages_to_all(prompt_message)
            break
        else:
            print('Username is empty.')
    threading.Thread(target=listen_for_messages, args=(client, username, public_partner_key,)).start()


def main():
    # AF_INET = IPv4 address
    # SOCK_STREAM = TCP packets for communication
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Provide server with host ip and port
        server.bind((HOST, PORT))
        print(f'Server {HOST} {PORT} is running')
    except:
        print(f'Bind to host failed.\n'
              f'Host: {HOST}\n'
              f'Port: {PORT}')

    # Server limit
    server.listen(listen_limit)

    # while loop keeps listening to client connections
    while True:
        client, address = server.accept()
        print(f'Connection to client {address[0]} {address[1]} successfully.')
        client.send(public_key.save_pkcs1("PEM"))  # send server public key to client
        public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024))  # gets client's public key
        threading.Thread(target=client_handler, args=(client, public_partner,)).start()


if __name__ == '__main__':
    main()
