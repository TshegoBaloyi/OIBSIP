# Server
import socket
import threading

def handle_client(client_socket, address):
    while True:
        message = client_socket.recv(1024).decode()
        # Broadcast the message to other clients
        for client in clients:
            client.send(message.encode())

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 1234))
    server_socket.listen(5)
    
    while True:
        client_socket, address = server_socket.accept()
        clients.append(client_socket)
        client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
        client_thread.start()

# Client
def receive_messages(client_socket):
    while True:
        message = client_socket.recv(1024).decode()
        print(message)

def send_messages(client_socket):
    while True:
        message = input()
        client_socket.send(message.encode())

def run_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 1234))
    
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()
    
    send_thread = threading.Thread(target=send_messages, args=(client_socket,))
    send_thread.start()

clients = []

if __name__ == '__main__':
    server_thread = threading.Thread(target=run_server)
    server_thread.start()
