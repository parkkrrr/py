import socket

# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the IP address and port number to connect to
ip_address = '127.0.0.1' # localhost
port = 8000

# Connect to the server
sock.connect((ip_address, port))

# Send data to the server
data = 'Hello, server!'
sock.send(data.encode())

# Receive data from the server
received_data = sock.recv(1024).decode()
print('Received data:', received_data)

# Close the socket
sock.close()


"""
inet is a module in the Python standard library that provides functions and classes for working with IP addresses and networked services. Specifically, it provides functions for working with IPv4 and IPv6 addresses, as well as functions for working with socket addresses.

The inet module is a part of the broader socket module, which provides low-level access to the BSD socket interface. BSD sockets are a standardized interface for networking in Unix-like operating systems, and they provide a way to establish communication between processes over a network. The inet module provides a more user-friendly interface to the socket module, specifically for working with IP addresses and networked services.

Some of the key functions and classes provided by the inet module include:

inet_aton: Convert an IPv4 address in string format to a 32-bit packed binary format.
inet_ntoa: Convert a 32-bit packed binary format IPv4 address to a string.
inet_pton: Convert an IP address string to its packed binary representation.
inet_ntop: Convert a packed binary representation of an IP address to a string.
socket.getaddrinfo: Get address information for a given hostname and service.
Overall, the inet module provides a convenient and Pythonic way to work with IP addresses and networking in Python.
"""