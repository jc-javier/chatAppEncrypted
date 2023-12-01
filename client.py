from PySide6.QtWidgets import QMainWindow, QMessageBox
from ui_mainwindow import Ui_MainWindow

import socket
import threading
import rsa


class ChatApp(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        self.app = app
        self.HOST = '127.0.0.1'
        self.PORT = 1234
        self.FORMAT = 'utf-8'
        self.public_partner = None

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.connect_button.clicked.connect(self.connect_server)
        self.actionQQuit.triggered.connect(self.quit)
        self.send_button.clicked.connect(self.send_message_to_server)
        self.message_lineedit.returnPressed.connect(self.send_message_to_server)
        self.message_lineedit.setEnabled(False)
        self.send_button.setEnabled(False)

    def quit(self):
        self.close()

    def connect_server(self):
        username = self.username_lineedit.text()
        print(username)
        if username != '':
            # Connect
            try:
                self.client.connect((self.HOST, self.PORT))
                self.chat_listwidget.clear()
                self.chat_listwidget.addItem('Connected Successfully')
            except:
                print(f'Unable to connect to server {self.HOST} {self.PORT}')
            public_key, private_key = rsa.newkeys(1024)
            self.public_partner = rsa.PublicKey.load_pkcs1(self.client.recv(1024))  # gets server's public key
            self.client.send(public_key.save_pkcs1("PEM"))  # send client public key to server
            self.client.send(rsa.encrypt(username.encode(self.FORMAT), self.public_partner))  # send username with server's public key
            # self.client.send(username.encode())

            threading.Thread(target=self.listen_for_messages, args=(self.client, private_key,)).start()

            self.username_lineedit.setReadOnly(True)
            self.connect_button.setEnabled(False)
            self.message_lineedit.setEnabled(True)
            self.send_button.setEnabled(True)
        else:
            QMessageBox.warning(self, 'Chat App', 'Username is empty.')

    def listen_for_messages(self, client, private_key):
        while True:
            response = client.recv(1024)
            message = rsa.decrypt(response, private_key).decode(self.FORMAT).strip()  # decrypt message with client private key
            # message = client.recv(1024).decode('utf-8')
            if message != '':
                username = message.split('~')[0]
                content = message.split('~')[1]
                self.chat_listwidget.addItem(f'{username}: {content}')
            else:
                break

    def send_message_to_server(self):
        message = self.message_lineedit.text()
        if message != '':
            # self.client.send(message.encode('utf-8'))
            self.client.send(rsa.encrypt(message.encode(self.FORMAT), self.public_partner))  # send message with server's public key
            self.message_lineedit.clear()
        else:
            pass

    def closeEvent(self, event):
        message = '!disconnect'
        self.client.send(rsa.encrypt(message.encode(self.FORMAT), self.public_partner))
        self.client.close()
        event.accept()
