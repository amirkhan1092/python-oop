# Python Socket Programming - 

## What is Socket Programming?
Socket programming allows communication between **two or more devices** over a **network**. In Python, the `socket` module provides the necessary functions for creating **client-server applications**.

### Basic Terminology
- **Socket**: An endpoint for communication.
- **Server**: A program that listens for connections and responds to requests.
- **Client**: A program that initiates communication with the server.
- **IP Address**: Identifies a device on a network.
- **Port**: A numerical identifier for a specific process on a machine.

## Steps to Create a Client-Server Chat Application
1. **Server Side**:
   - Create a socket.
   - Bind the socket to an IP and port.
   - Listen for incoming connections.
   - Accept client connections and communicate.

2. **Client Side**:
   - Create a socket.
   - Connect to the server using IP and port.
   - Send and receive messages.

---

## Console-Based Client-Server Chat App

### **Server Code**
```python
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
```

### **Client Code**
```python
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
```

---

## Explanation
1. **Server**
   - Creates a socket and binds it to `localhost:12345`.
   - Listens for incoming connections.
   - Accepts a client connection.
   - Waits for messages from the client and responds accordingly.
   - Stops when 'exit' is received.

2. **Client**
   - Connects to the server.
   - Sends messages to the server.
   - Receives and prints the server’s responses.
   - Terminates when 'exit' is sent.

---

## Next Step: GUI-Based Chat with Tkinter
After completing the console version, students can try implementing a **GUI-based chat application** using `Tkinter`.

