import socket
import select

# Define the host and port
HOST = '127.0.0.1'
PORT = 8000

# Create a server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen()

# Add server socket to the list of readable sockets
sockets_list = [server_socket]

# Create an empty dictionary to store client sockets and their data
clients = {}

print(f'Server listening on {HOST}:{PORT}')

while True:
    # Use the select function to monitor sockets for input/output events
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

    # Handle sockets with incoming data
    for socket in read_sockets:
        # Handle new connection request
        if socket == server_socket:
            client_socket, client_address = server_socket.accept()
            sockets_list.append(client_socket)
            clients[client_socket] = {'data': b''}
            print(f'New client connected: {client_address}')

        # Handle existing client socket with incoming data
        else:
            data = socket.recv(1024)
            if data:
                clients[socket]['data'] += data
            else:
                # Remove closed socket from the list and dictionary
                sockets_list.remove(socket)
                print(f"Client disconnected: {clients[socket]['address']}")
                del clients[socket]

    # Handle sockets with exceptions
    for socket in exception_sockets:
        sockets_list.remove(socket)
        print(f"Socket exception: {socket.getpeername()}")

    # Handle client data
    for client_socket, data in [(s, c['data']) for s, c in clients.items()]:
        if data:
            # Process client data
            processed_data = data.decode().strip()
            print(f"Received from {clients[client_socket]['address']}: {processed_data}")
            response = f"Echo: {processed_data}\n".encode()

            # Send response to client
            client_socket.send(response)
            clients[client_socket]['data'] = b''

"""
This Python code creates a TCP socket client that can send and receive data from a server using the select module. The client uses the select function to wait for input from either the server or the user. The sys.stdin object represents input from the user, while client_socket represents input from the server.

The client continuously loops and waits for input from either the server or the user. If input is received from the server, it is printed to the console. If input is received from the user, it is sent to the server.

The select module allows the client to handle multiple socket connections concurrently, making it a more advanced implementation of a socket client.

Overall, this code demonstrates how to create a socket client that can handle multiple socket connections and wait for input from either the server or the user using the select module.
"""