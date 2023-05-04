import socket
import select
import sys

# Define the server address and port
HOST = '127.0.0.1'
PORT = 8000

# Create a client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.settimeout(2)

# Connect to the server
try:
    client_socket.connect((HOST, PORT))
except:
    print("Error: Unable to connect to the server.")
    sys.exit()

print("Connected to server.")

while True:
    # Wait for input from either the server or the user
    sockets_list = [sys.stdin, client_socket]
    read_sockets, write_sockets, error_sockets = select.select(sockets_list, [], [])

    for socket in read_sockets:
        if socket == client_socket:
            # Receive data from the server
            data = socket.recv(1024)
            if not data:
                print("Disconnected from server.")
                sys.exit()
            else:
                print(data.decode())
        else:
            # Read input from the user and send to the server
            message = sys.stdin.readline()
            client_socket.send(message.encode())
            sys.stdout.write("<You>")
            sys.stdout.write(message)
            sys.stdout.flush()
