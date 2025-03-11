import socket

HOST='127.0.0.1'
PORT=12345

client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client_socket.connect((HOST,PORT))
print("connected to the server Type 'exit' to quit")

while True:
    message=input("You: ")
    if message.lower()=='exit':
        break
    client_socket.send(message.encode())

    response=client_socket.recv(1024).decode()

    print(f"Server: {response}")

client_socket.close()
print("Connection closed")


