import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client_socket.connect(('localhost', 12345))
print("Connected to server.")

while True:
    # Send message to server
    message = input("You: ")
    client_socket.send(message.encode('utf-8'))
    if message.lower() == 'exit':
        break
    
    # Receive server response
    response = client_socket.recv(1024).decode('utf-8')
    print("Server:", response)

# Close socket
client_socket.close()