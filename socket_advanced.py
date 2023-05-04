import socket
import sys
import threading

# Define the server address and port
HOST = '127.0.0.1'
PORT = 8000

# Create a client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def receive():
    """
    Continuously receive data from the server.
    """
    while True:
        try:
            data = client_socket.recv(1024)
            if data:
                print(data.decode())
        except:
            # An error occurred, terminate the thread
            print("Error: unable to receive data from the server.")
            sys.exit()

def send():
    """
    Continuously send data to the server.
    """
    while True:
        try:
            message = input()
            client_socket.send(message.encode())
        except:
            # An error occurred, terminate the thread
            print("Error: unable to send data to the server.")
            sys.exit()

try:
    # Connect to the server
    client_socket.connect((HOST, PORT))
    print("Connected to server.")

    # Create and start the receive and send threads
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    send_thread = threading.Thread(target=send)
    send_thread.start()

except:
    # An error occurred, terminate the program
    print("Error: unable to connect to the server.")
    sys.exit()
