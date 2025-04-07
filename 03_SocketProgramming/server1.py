import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to an address and port
server_socket.bind(('localhost', 12345))

# Listen for incoming connections
server_socket.listen(1)
print("Server is listening...")

# Accept client connection
client_socket, addr = server_socket.accept()
print(f"Connected to {addr}")

while True:
    # Receive message from client
    message = client_socket.recv(1024).decode('utf-8')
    if message.lower() == 'exit':
        print("Client disconnected.")
        break
    print("Client:", message)
    
    # Send response to client
    reply = input("You: ")
    client_socket.send(reply.encode('utf-8'))

# Close sockets
client_socket.close()
server_socket.close()