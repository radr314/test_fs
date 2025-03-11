import socket

HOST='127.0.0.1'
PORT=12345

server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_socket.bind((HOST,PORT))

server_socket.listen(1)

print(f'Server is listening on {HOST}: {PORT}.........')

client_socket,client_address=server_socket.accept()
print(f"COnnection Established with {client_address}")


while True:
    message=client_socket.recv(1024).decode()

    if not message:
        break

    print(f"message from client: {message}")


    response=input("Enter your response:")
    client_socket.send(response.encode())

client_socket.close()

server_socket.close()
print("Connection closed")

